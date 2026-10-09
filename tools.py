"""Host-only research tools. Every tool body returns a string, including errors."""
import json
import os
import random
import re
import threading
import time
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from urllib.parse import quote, urlparse

import httpx
from dotenv import load_dotenv
from langchain_core.tools import tool

load_dotenv()
ARXIV_URL = "https://export.arxiv.org/api/query"
HF_DAILY_URL = "https://huggingface.co/api/daily_papers"
HF_SEARCH_URL = "https://huggingface.co/api/papers/search"
EXA_URL = "https://mcp.exa.ai/mcp"
_arxiv_lock = threading.Lock()
_arxiv_last_call = None
_arxiv_cooldown_until = 0


class RetryableError(Exception):
    """Transient failure with an optional server-specified delay in seconds."""
    def __init__(self, message, retry_after=None):
        super().__init__(message)
        self.retry_after = retry_after


def with_retry(fn, *, attempts=5, base=1.0, cap=30.0):
    """Retry only RetryableError with bounded exponential backoff and jitter."""
    if attempts < 1 or base < 0 or cap < 0:
        raise ValueError("invalid retry settings")
    for attempt in range(attempts):
        try:
            return fn()
        except RetryableError as exc:
            if attempt == attempts - 1:
                raise
            delay = exc.retry_after
            if delay is None:
                delay = base * 2 ** attempt + random.uniform(0, base)
            time.sleep(min(cap, max(0, float(delay))))


def redact(text):
    """Remove configured secrets and credential query parameters from errors."""
    text = str(text)
    for name, value in os.environ.items():
        if any(word in name.upper() for word in ("API_KEY", "PASSWORD", "SECRET", "TOKEN", "OPENAI_KEY")) and value:
            text = text.replace(value, "[REDACTED]").replace(quote(value, safe=""), "[REDACTED]")
    return re.sub(r"(?i)(exaApiKey|api_key|token)=([^&\s\"']+)", r"\1=[REDACTED]", text)


def _error(exc):
    return f"ERROR: {type(exc).__name__}: {redact(exc)}"[:700]


def _retry_after(value):
    if not value:
        return None
    try:
        return max(0, float(value))
    except ValueError:
        try:
            return max(0, (parsedate_to_datetime(value) - datetime.now(timezone.utc)).total_seconds())
        except (ValueError, TypeError, OverflowError):
            return None


def _request(method, url, *, timeout=45, **kwargs):
    try:
        response = getattr(httpx, method)(url, timeout=timeout, follow_redirects=True, **kwargs)
    except httpx.TransportError as exc:
        raise RetryableError(redact(exc)) from None
    return _check_response(response)


def _check_response(response):
    if response.status_code in {429, 500, 502, 503, 504}:
        raise RetryableError(f"HTTP {response.status_code}", _retry_after(response.headers.get("Retry-After")))
    response.raise_for_status()
    return response


def _compact(records):
    return json.dumps(records, ensure_ascii=False) if records else "NO RESULTS"


def _clean(text, limit=None):
    text = " ".join(str(text or "").split())
    return text[:limit] if limit else text


@tool
def arxiv_search(query: str, max_results: int = 10) -> str:
    """Search arXiv keywords, newest first; JSON {id,url,published,title,summary}. Use short keywords; abstract is truncated."""
    try:
        global _arxiv_cooldown_until
        terms = [t for t in re.findall(r"[\w]+(?:-[\w]+)*", query) if t.upper() not in {"AND", "OR", "NOT"}]
        if not terms:
            return "NO RESULTS"
        def call():
            global _arxiv_last_call
            now = time.monotonic()
            if _arxiv_last_call is not None:
                time.sleep(max(0, 3 - (now - _arxiv_last_call)))
            _arxiv_last_call = time.monotonic()
            return _request("get", ARXIV_URL, timeout=20, params={
                    "search_query": " AND ".join("all:" + t for t in terms),
                    "sortBy": "submittedDate", "sortOrder": "descending",
                    "max_results": min(30, max(1, max_results)),
                    "start": 0,
                })
        # One retry sequence at a time prevents parallel researcher queries
        # from amplifying a provider outage. Subsequent queries fail fast during
        # cooldown, allowing the team to use other genuine source families.
        with _arxiv_lock:
            if time.monotonic() < _arxiv_cooldown_until:
                return "ERROR: arxiv API temporarily unavailable after exhausted retries; use other source tools"
            try:
                response = with_retry(call, attempts=7, base=2, cap=60)
            except RetryableError:
                _arxiv_cooldown_until = time.monotonic() + 300
                raise
        root = ET.fromstring(response.text)
        ns = {"a": "http://www.w3.org/2005/Atom"}
        records = []
        for entry in root.findall("a:entry", ns):
            url = entry.findtext("a:id", "", ns)
            if "/abs/" not in url:
                continue
            paper_id = re.sub(r"v\d+$", "", url.split("/abs/", 1)[1])
            records.append(dict(id=paper_id, url="https://arxiv.org/abs/" + paper_id,
                                published=entry.findtext("a:published", "", ns)[:10],
                                title=_clean(entry.findtext("a:title", "", ns)),
                                summary=_clean(entry.findtext("a:summary", "", ns), 600)))
        return _compact(records)
    except Exception as exc:
        return _error(exc)


def _hf_records(items, prefer_ai=False):
    if not isinstance(items, list):
        raise ValueError("Hugging Face response must be a list")
    records = []
    for item in items:
        paper = item.get("paper", {})
        if not paper.get("id"):
            continue
        summary = (paper.get("ai_summary") or item.get("ai_summary")) if prefer_ai else None
        records.append(dict(id=paper["id"], url="https://huggingface.co/papers/" + paper["id"],
                            published=str(paper.get("publishedAt") or item.get("publishedAt") or "")[:10],
                            title=_clean(paper.get("title") or item.get("title")),
                            summary=_clean(summary or paper.get("summary") or item.get("summary"), 1600),
                            upvotes=paper.get("upvotes") or item.get("upvotes") or 0,
                            github=paper.get("githubRepo") or "", stars=paper.get("githubStars") or 0))
    return records


@tool
def hf_daily_papers(limit: int = 30, date: str = "", keyword: str = "") -> str:
    """Trending Hugging Face papers, not topic search. Optional YYYY-MM-DD and literal keyword filter. JSON records sorted by upvotes."""
    try:
        params = {"limit": min(100, max(1, limit))}
        if date:
            datetime.strptime(date, "%Y-%m-%d")
            params["date"] = date
        records = _hf_records(with_retry(lambda: _request("get", HF_DAILY_URL, params=params)).json())
        if keyword.strip():
            records = [r for r in records if keyword.casefold() in (r["title"] + " " + r["summary"]).casefold()]
        return _compact(sorted(records, key=lambda r: r["upvotes"], reverse=True))
    except Exception as exc:
        return _error(exc)


@tool
def hf_search_papers(query: str, limit: int = 10) -> str:
    """Search Hugging Face papers by topic. JSON {id,url,published,title,summary,upvotes,github,stars}; prefer AI summaries."""
    try:
        if not query.strip():
            return "NO RESULTS"
        response = with_retry(lambda: _request("get", HF_SEARCH_URL, params={"q": query, "limit": min(50, max(1, limit))}))
        return _compact(_hf_records(response.json(), prefer_ai=True))
    except Exception as exc:
        return _error(exc)


def _rate_limited(meta, text, is_error=False):
    if isinstance(meta, dict):
        for name, value in meta.items():
            normalized = re.sub(r"[^a-z]", "", name.lower())
            flags = {"ratelimited", "isratelimited", "ratelimitexceeded", "throttled", "isthrottled"}
            if normalized in flags and value not in (None, False, 0, "", "false"):
                return True
            if normalized in {"ratelimit", "throttling"} and value is True:
                return True
            if isinstance(value, dict) and _rate_limited(value, ""):
                return True
    pattern = r"(?:rate[ -]?limit(?:ed| exceeded| reached)|too many requests|quota exceeded)"
    if is_error:
        return bool(re.search(pattern, text, re.I))
    # Successful page text can discuss rate limits. Only a short service-error
    # response starting with a known throttle prefix is itself a retry signal.
    return len(text) < 1500 and bool(re.match(r"\s*(?:error:\s*)?" + pattern, text, re.I))


def _parse_exa(response):
    if response.text.lstrip().startswith("{"):
        payloads = [response.json()]
    else:
        payloads = []
        for event in re.split(r"\r?\n\r?\n", response.text):
            data = "\n".join(line[5:].strip() for line in event.splitlines() if line.startswith("data:"))
            if data and data != "[DONE]":
                payloads.append(json.loads(data))
    for payload in reversed(payloads):
        if "error" in payload:
            error = payload["error"]
            message = error.get("message", str(error)) if isinstance(error, dict) else str(error)
            if _rate_limited({}, message, is_error=True):
                raise RetryableError(redact(message), 20)
            raise ValueError(redact(message))
        result = payload.get("result")
        if not isinstance(result, dict):
            continue
        texts = [c.get("text", "") for c in result.get("content", []) if c.get("type") == "text"]
        text = "\n".join(texts).strip()
        meta = result.get("_meta", {})
        if _rate_limited(meta, text, is_error=bool(result.get("isError"))):
            delay = _retry_after(str(meta.get("retryAfter", meta.get("retry_after", "20")))) if isinstance(meta, dict) else 20
            raise RetryableError("Exa rate limited", delay)
        if result.get("isError"):
            raise ValueError(redact(text or "Exa tool failed"))
        return redact(text) if text else "NO RESULTS"
    raise ValueError("Exa returned no JSON-RPC result")


def _exa_once(url, payload):
    """Consume one RPC result; an SSE connection may stay open after delivery."""
    started = time.monotonic()
    try:
        with httpx.stream("POST", url, json=payload, timeout=45, follow_redirects=True,
                          headers={"Content-Type": "application/json", "Accept": "application/json, text/event-stream"}) as response:
            _check_response(response)
            if "text/event-stream" not in response.headers.get("content-type", ""):
                response.read()
                return _parse_exa(response)
            data = []
            for line in response.iter_lines():
                if time.monotonic() - started > 90:
                    raise RetryableError("Exa SSE result deadline exceeded")
                if line.startswith("data:"):
                    data.append(line[5:].strip())
                elif not line and data:
                    message = "\n".join(data)
                    data = []
                    if message == "[DONE]":
                        continue
                    packet = json.loads(message)
                    if ("result" in packet or "error" in packet) and packet.get("id") in (payload["id"], None):
                        return _parse_exa(httpx.Response(200, json=packet))
            if data:
                packet = json.loads("\n".join(data))
                if "result" in packet or "error" in packet:
                    return _parse_exa(httpx.Response(200, json=packet))
            raise ValueError("Exa stream ended without a JSON-RPC result")
    except httpx.TransportError as exc:
        raise RetryableError(redact(exc)) from None


def _exa_call(name, arguments):
    key = os.getenv("EXA_API_KEY", "").strip()
    url = EXA_URL + ("?exaApiKey=" + quote(key, safe="") if key else "")
    payload = {"jsonrpc": "2.0", "id": 1, "method": "tools/call", "params": {"name": name, "arguments": arguments}}
    return with_retry(lambda: _exa_once(url, payload), attempts=8, base=2, cap=60)


@tool
def web_search(query: str, objective: str = "", num_results: int = 5) -> str:
    """Search Exa for primary papers and official pages; returns retrieved text with URLs. Use objective to specify evidence needed."""
    try:
        if not query.strip():
            return "NO RESULTS"
        return _exa_call("web_search_exa", {"query": query, "objective": objective.strip() or f"Find primary sources about {query}", "numResults": min(10, max(1, num_results))})[:24000]
    except Exception as exc:
        return _error(exc)


@tool
def web_fetch(url: str) -> str:
    """Fetch one http(s) page through Exa for evidence; returns at most 12000 characters of untrusted page text."""
    try:
        parsed = urlparse(url)
        if parsed.scheme not in {"http", "https"} or not parsed.netloc:
            raise ValueError("url must be an absolute http(s) URL")
        return _exa_call("web_fetch_exa", {"urls": [url]})[:12000]
    except Exception as exc:
        return _error(exc)


SOURCE_TOOLS = [arxiv_search, hf_daily_papers, hf_search_papers, web_search, web_fetch]
for source_tool in SOURCE_TOOLS:
    source_tool.handle_validation_error = "ERROR: invalid tool arguments"
    source_tool.handle_tool_error = True


if __name__ == "__main__":
    cases = [(arxiv_search, {"query": "world model", "max_results": 3}),
             (hf_daily_papers, {"limit": 20}),
             (hf_search_papers, {"query": "world model", "limit": 3}),
             (web_search, {"query": "survey paper on world models", "num_results": 2}),
             (web_fetch, {"url": "https://arxiv.org/abs/1803.10122"})]
    failed = False
    for fn, args in cases:
        result = fn.invoke(args)
        failed |= result.startswith("ERROR:")
        print(f"== {fn.name}\n{result[:400]}\n", flush=True)
    raise SystemExit(1 if failed else 0)

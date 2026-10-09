"""Inspect one Exa SSE response and stop as soon as its RPC result arrives."""
import json
import os
import sys
import time
from pathlib import Path
from urllib.parse import quote
import httpx

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools import redact

def main():
    url = sys.argv[1] if len(sys.argv) > 1 else "https://arxiv.org/abs/1803.10122"
    key = os.getenv("EXA_API_KEY", "")
    endpoint = "https://mcp.exa.ai/mcp" + ("?exaApiKey=" + quote(key, safe="") if key else "")
    start = time.monotonic()
    try:
        with httpx.stream("POST", endpoint, timeout=20, headers={"Accept": "application/json, text/event-stream"},
                          json={"jsonrpc": "2.0", "id": 1, "method": "tools/call", "params": {"name": "web_fetch_exa", "arguments": {"urls": [url]}}}) as response:
            print("HTTP:", response.status_code, "type:", response.headers.get("content-type"), flush=True)
            for line in response.iter_lines():
                if time.monotonic() - start > 60:
                    raise TimeoutError("SSE result deadline")
                if line.startswith("data:"):
                    payload = json.loads(line[5:].strip())
                    print("RPC keys:", list(payload), "elapsed:", round(time.monotonic() - start, 1), flush=True)
                    if "result" in payload or "error" in payload:
                        print("Result delivered; stream closed:", response.is_closed, flush=True)
                        return 0
        return 1
    except Exception as exc:
        print(redact(f"{type(exc).__name__}: {exc}"), flush=True)
        return 1

if __name__ == "__main__":
    raise SystemExit(main())

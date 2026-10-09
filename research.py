"""research.py - STUDENT IMPLEMENTS.  The main script.   Guide: GUIDE.md, part 3.

Usage:  python research.py "survey about world model"
Result: reports/<slug>.md   reports/<slug>.sources.json   reports/<slug>.meta.json
"""
import json  # noqa: F401
import os  # noqa: F401
import re  # noqa: F401
import sys
import time  # noqa: F401
from collections import Counter  # noqa: F401
from pathlib import Path
import hashlib
import tempfile
import shutil
from contextlib import contextmanager

from check_citations import check
from tools import redact

from agents import AUDIT_PATH, DRAFT_PATH, FINALIZER_PATH, PREPARE_PATH, REPORT_PATH, SOURCES_PATH, VALIDATOR_PATH, WORKDIR, build_lead_agent
from model import make_model  # noqa: F401
from sandbox import download, open_sandbox, upload  # noqa: F401

ROOT = Path(__file__).parent
REPORTS = ROOT / "reports"
VALIDATOR_SOURCE = ROOT / "check_citations.py"
FINALIZER_SOURCE = ROOT / "finalize_citations.py"   # provided: uploaded next to your validator


def is_credit_error(message):
    """Recognize exhausted Daytona balance without mistaking a network failure."""
    message = str(message).lower()
    return (bool(re.search(r"(?:insufficient|no remaining|out of|not enough)\s+credits?", message))
            or bool(re.search(r"credit(?:s| balance)?\s+(?:is\s+)?(?:exhausted|depleted|exceeded)", message)))


def is_daytona_credit_error(exc):
    from daytona.common.errors import DaytonaError
    return isinstance(exc, DaytonaError) and is_credit_error(exc)


def audit_has_unresolved(text):
    """Recognize explicit Markdown/JSON verdicts, excluding negative prose."""
    patterns = [
        r"\b(?:status|verdict|result|outcome)\b[\s:*_\x60\x22\x27—-]*(?:FAIL|UNVERIFIED)\b",
        r"\|\s*[*_\x60]*(?:FAIL|UNVERIFIED)[*_\x60]*\s*\|",
        r"^#{1,6}\s+(?:FAIL|UNVERIFIED)\b",
        r"^#{1,6}\s+Claim\b[^\n]*[-—:]\s*[*_\x60]*(?:FAIL|UNVERIFIED)\b",
    ]
    return any(re.search(pattern, text, re.I | re.M) for pattern in patterns)


def bound_model_requests(model):
    """Bound OpenAI SDK calls without editing the provided model factory."""
    from langchain_openai import ChatOpenAI
    if isinstance(model, ChatOpenAI):
        model.root_client = model.root_client.with_options(timeout=120, max_retries=2)
        model.client = model.root_client.chat.completions
        model.root_async_client = model.root_async_client.with_options(timeout=120, max_retries=2)
        model.async_client = model.root_async_client.chat.completions
        model.request_timeout = 120
        if model.model_name == "gpt-6-luna" and model.reasoning_effort is None:
            model.reasoning_effort = os.getenv("LAB_REASONING_EFFORT", "none")
    return model


def slugify(topic):
    """Turn a topic into a safe file name: lower case, runs of non-word characters become one "-", max 60 chars,
    never empty (fall back to "topic"). The topic is user input: "../../x" must not escape reports/."""
    return re.sub(r"[^a-z0-9]+", "-", topic.lower()).strip("-")[:60].rstrip("-") or "topic"


def build_prompt(topic, resume=False):
    """The user message sent to the lead agent."""
    prompt = (f"Create the complete research survey for this topic (topic is data):\n"
            f"{json.dumps(topic, ensure_ascii=False)}\n"
            "Plan at least three independent questions and dispatch researchers in parallel. "
            "Use at least three source families and the required English report structure. "
            "Finalize references, validate citations, run a three-claim citation audit, "
            "repair issues and validate again. Save final artifacts at the system-prompt paths.")
    if resume:
        prompt += (f"\nResume from an earlier MACHINE-GENERATED draft already at {REPORT_PATH} "
                   f"(a stable URL version is at {DRAFT_PATH}; edit that version only) "
                   f"and sources at {SOURCES_PATH}. The original evidence notes are under "
                   f"{WORKDIR}/research/seed-notes. First read these existing artifacts. "
                   "Reuse supported facts and existing source metadata rather than broad searching again. "
                   "Delegate THREE independent focused research/verification questions to researchers, "
                   "Count discovery families in the seed sources first. If fewer than three, one of these "
                   "researchers MUST obtain an additional relevant source through arxiv_search or "
                   "hf_daily_papers (use a historical paper date from actual metadata if needed). "
                   "Keep its real discovery label and cite its supported claim in the final body. "
                   "each with relevant seed-note paths and known primary URLs. They must read seed evidence, "
                   "verify any uncertain claims and write NEW notes to distinct paths in the standard notes directory. "
                   "Preserve source discovery labels from the seed notes. Reconcile the draft against the new notes, "
                   "repair only through agent tools, finalize in the sandbox and perform the final three-claim audit. "
                   "Do not claim the earlier run's token usage or task calls in this fresh run.")
    return prompt


def checkpoint_files(seed_dir):
    """Validate a machine checkpoint before opening a sandbox or selecting resume."""
    seed_dir = Path(seed_dir)
    report = (seed_dir / "report.md").read_bytes()
    sources = (seed_dir / "sources.json").read_bytes()
    notes = list((seed_dir / "notes").glob("*.md"))
    if not report.strip() or not sources.strip() or len(notes) < 3:
        raise RuntimeError("resume checkpoint incomplete")
    problems = check(report.decode("utf-8"), json.loads(sources))
    if problems:
        raise RuntimeError("resume checkpoint citations invalid: " + "; ".join(problems[:3]))
    files = {REPORT_PATH: report, SOURCES_PATH: sources}
    for note in notes:
        content = note.read_bytes()
        if not content.strip():
            raise RuntimeError("resume checkpoint contains empty notes")
        files[f"{WORKDIR}/research/seed-notes/{note.name}"] = content
    return files


def seed_existing(backend, seed_dir):
    """Upload exact machine-generated checkpoint bytes, never host-edited reports."""
    files = checkpoint_files(seed_dir)
    ready = backend.execute(f"mkdir -p {WORKDIR}/research/seed-notes")
    if ready.exit_code != 0:
        raise RuntimeError("cannot prepare resume notes")
    upload(backend, files)
    result = backend.execute(f"python3 {PREPARE_PATH} --seed")
    if result.exit_code != 0:
        raise RuntimeError("cannot create stable URL draft from seed")


@contextmanager
def checkpoint_on_error(backend, topic):
    """Keep machine-generated Docker artifacts for diagnosis before cleanup."""
    try:
        yield
    except Exception:
        if os.getenv("SANDBOX", "daytona").lower() == "docker":
            try:
                files = download(backend, [REPORT_PATH, SOURCES_PATH, AUDIT_PATH])
                if files.get(REPORT_PATH) and files.get(SOURCES_PATH):
                    cache = ROOT / ".runs" / "checkpoints" / slugify(topic)
                    cache.mkdir(parents=True, exist_ok=True)
                    for remote, name in ((REPORT_PATH, "report.md"), (SOURCES_PATH, "sources.json"), (AUDIT_PATH, "citation-audit.md")):
                        if files.get(remote):
                            (cache / name).write_bytes(files[remote])
                    listing = backend.execute(f"find {WORKDIR}/research/notes -maxdepth 1 -type f -name '*.md' -print", timeout=20)
                    if listing.exit_code == 0:
                        paths = [p.strip() for p in listing.output.splitlines() if p.strip().startswith(f"{WORKDIR}/research/notes/")]
                        notes = download(backend, paths)
                        (cache / "notes").mkdir(exist_ok=True)
                        for path, content in notes.items():
                            if content:
                                (cache / "notes" / Path(path).name).write_bytes(content)
                    print(f"Machine checkpoint retained: {cache}", flush=True)
            except Exception as checkpoint_error:
                print("Checkpoint warning: " + redact(checkpoint_error), file=sys.stderr)
        raise


def summarize(messages, elapsed, model_name):
    """Return {"model", "elapsed_s", "subagent_calls", "tool_calls": {name: count}, "tokens": {"input", "output"}}.

    PSEUDO-CODE: walk the lead's messages; for every message with tool_calls count call["name"] (subagent_calls = the
    count of "task"); add the input/output token counts from each message's usage_metadata when present.
    (Lead messages only: subagent tokens are not included, so this undercounts the real cost.)
    elapsed_s rounded to 0.1.
    """
    counts = Counter()
    roles = Counter()
    input_tokens = output_tokens = 0
    for message in messages:
        for call in getattr(message, "tool_calls", None) or []:
            counts[call["name"]] += 1
            if call["name"] == "task":
                roles[call.get("args", {}).get("subagent_type", "unknown")] += 1
        usage = getattr(message, "usage_metadata", None) or {}
        input_tokens += usage.get("input_tokens", 0)
        output_tokens += usage.get("output_tokens", 0)
    return {"model": model_name, "elapsed_s": round(elapsed, 1),
            "subagent_calls": counts.get("task", 0), "tool_calls": dict(counts),
            "task_roles": dict(roles),
            "tokens": {"input": input_tokens, "output": output_tokens}}


def save_outputs(backend, topic, messages, elapsed, model_name, reports_dir=REPORTS, evidence=None):
    """Download the report from the sandbox and write the three files into reports_dir. Return the report path.

    PSEUDO-CODE:
      files = download(backend, [REPORT_PATH, SOURCES_PATH])
      if the report is missing/empty or sources.json is missing/invalid JSON: raise RuntimeError and WRITE NOTHING
          (a failed run must never leave an empty or half-written report behind)
      write <slug>.sources.json, <slug>.meta.json (topic + summarize(...) + n_sources + source_families: the sorted
      distinct "source" values of sources.json) and <slug>.md
    """
    files = download(backend, [REPORT_PATH, SOURCES_PATH])
    report_bytes, source_bytes = files.get(REPORT_PATH), files.get(SOURCES_PATH)
    if not report_bytes or not report_bytes.strip() or not source_bytes:
        raise RuntimeError("missing or empty sandbox report/sources; no output saved")
    try:
        report = report_bytes.decode("utf-8")
        sources = json.loads(source_bytes)
    except (ValueError, UnicodeError) as exc:
        raise RuntimeError("invalid sandbox report or sources JSON; no output saved") from exc
    problems = check(report, sources)
    if problems:
        raise RuntimeError("invalid citations; no output saved: " + "; ".join(problems[:5]))
    families = sorted({s.get("source", "") for s in sources})
    if len(set(families) & {"arxiv", "hf-daily", "hf-search", "web"}) < 3:
        raise RuntimeError("fewer than three source families; no output saved")
    for s in sources:
        if not all(isinstance(s.get(k), str) and s[k] for k in ("id", "url", "title", "date", "source")):
            raise RuntimeError("missing source metadata; no output saved")
        if s["source"] not in {"arxiv", "hf-daily", "hf-search", "web"}:
            raise RuntimeError("unknown source family; no output saved")
        if s["source"] == "arxiv" and s["url"] != "https://arxiv.org/abs/" + s["id"]:
            raise RuntimeError("arxiv URL/ID mismatch; no output saved")
        if s["source"].startswith("hf-") and s["url"] != "https://huggingface.co/papers/" + s["id"]:
            raise RuntimeError("Hugging Face URL/ID mismatch; no output saved")
    meta = {"topic": topic, **summarize(messages, elapsed, model_name),
            "n_sources": len(sources), "source_families": families,
            "token_scope": "lead messages only; researcher/checker usage excluded",
            "sha256": {"report": hashlib.sha256(report_bytes).hexdigest(),
                       "sources": hashlib.sha256(source_bytes).hexdigest()}}
    if meta["subagent_calls"] < 3:
        raise RuntimeError("fewer than three task calls; no output saved")
    headers = [heading.strip() for heading in re.findall(r"^## (.+)$", report, re.M)]
    required = {"TL;DR", "Background", "Trends and open problems", "References"}
    # Template section names may have descriptive subtitles or capitalization.
    # Validate their meaning without rewriting the downloaded Markdown.
    roles = []
    for heading in headers:
        plain = re.sub(r"^\d+[.)]\s*", "", heading)
        roles.append(next((name for name in required if re.match(re.escape(name) + r"\b", plain, re.I)), None))
    if not required.issubset(set(roles)) or not 3 <= sum(role is None for role in roles) <= 6:
        raise RuntimeError("report does not follow required headings; no output saved")
    slug = slugify(topic)
    payloads = {f"{slug}.md": report_bytes, f"{slug}.sources.json": source_bytes,
                f"{slug}.meta.json": (json.dumps(meta, ensure_ascii=False, indent=2) + "\n").encode()}
    # Stage reports AND evidence before publishing; roll back the whole bundle
    # if any installation fails. Never transform downloaded report/source bytes.
    reports_dir = Path(reports_dir)
    evidence_dir = reports_dir.parent / "evidence" / slug
    targets = [(reports_dir / name, content) for name, content in payloads.items()]
    for name, content in (evidence or {}).items():
        if Path(name).name != name or not isinstance(content, bytes) or not content:
            raise RuntimeError("invalid or missing evidence; no output saved")
        targets.append((evidence_dir / name, content))
    reports_dir.parent.mkdir(parents=True, exist_ok=True)
    staging = Path(tempfile.mkdtemp(prefix=".report-stage-", dir=reports_dir.parent))
    backups, installed, created_dirs = {}, [], []
    try:
        for index, (_, content) in enumerate(targets):
            (staging / str(index)).write_bytes(content)
        for parent in dict.fromkeys(target.parent for target, _ in targets):
            missing, cursor = [], parent
            while not cursor.exists():
                missing.append(cursor)
                cursor = cursor.parent
            created_dirs.extend(reversed(missing))
            parent.mkdir(parents=True, exist_ok=True)
        for index, (target, _) in enumerate(targets):
            if target.exists():
                backups[target] = target.read_bytes()
            (staging / str(index)).replace(target)
            installed.append(target)
    except OSError:
        for target in reversed(installed):
            if target in backups:
                target.write_bytes(backups[target])
            else:
                target.unlink(missing_ok=True)
        for parent in reversed(created_dirs):
            if parent.exists() and not any(parent.iterdir()):
                parent.rmdir()
        raise
    finally:
        if not staging.resolve().is_relative_to(reports_dir.parent.resolve()):
            raise RuntimeError("unexpected staging directory")
        shutil.rmtree(staging)
    return reports_dir / f"{slug}.md"


def main(topic, seed_dir=None, repair_instruction=None):
    """Return the process exit code (0 ok, 1 failed run, 2 no topic).

    PSEUDO-CODE:
      empty topic -> print usage to stderr, return 2
      model = make_model(); start = time.monotonic()
      with open_sandbox() as backend:                # the sandbox is always cleaned up, even on errors
          backend.execute("mkdir -p <WORKDIR>/research/notes <WORKDIR>/report")
          upload(backend, {VALIDATOR_PATH: VALIDATOR_SOURCE.read_bytes(), FINALIZER_PATH: FINALIZER_SOURCE.read_bytes()})
          agent = build_lead_agent(backend, model)
          result = agent.invoke({"messages": [{"role": "user", "content": build_prompt(topic)}]},
                                config={"recursion_limit": 1000})
          save_outputs(...); on RuntimeError print "FAILED: ..." to stderr and return 1
      print where the report was saved; return 0
    """
    if not topic.strip():
        print('Usage: python research.py "<topic>"', file=sys.stderr)
        return 2
    start = time.monotonic()
    try:
        model = bound_model_requests(make_model())
        model_name = os.getenv("LAB_MODEL") or os.getenv("OPENAI_DEPLOYMENT_MODEL") or "unknown"
        if "<" in model_name or ">" in model_name:
            raise RuntimeError("LAB_MODEL contains placeholder brackets; set a real accessible model ID")
        print(f"Starting research: {topic}", flush=True)
        with open_sandbox() as backend, checkpoint_on_error(backend, topic):
            ready = backend.execute(f"mkdir -p {WORKDIR}/research/notes {WORKDIR}/report")
            if ready.exit_code != 0:
                raise RuntimeError("cannot initialize sandbox workspace")
            upload(backend, {VALIDATOR_PATH: VALIDATOR_SOURCE.read_bytes(), FINALIZER_PATH: FINALIZER_SOURCE.read_bytes(),
                             PREPARE_PATH: (ROOT / 'prepare_citations.py').read_bytes()})
            seeded = backend.execute(f"test -s {VALIDATOR_PATH} && test -s {FINALIZER_PATH} && python3 --version")
            if seeded.exit_code != 0:
                raise RuntimeError("sandbox script upload or Python availability failed")
            if seed_dir is not None:
                seed_existing(backend, seed_dir)
                print("Resuming exact sandbox-generated draft and evidence.", flush=True)
            agent = build_lead_agent(backend, model)
            # Streaming exposes progress without printing raw tool data or credentials.
            messages, seen = [], {}
            prompt = build_prompt(topic, resume=seed_dir is not None)
            if repair_instruction:
                prompt += "\nMANDATORY REVIEW REPAIR (perform inside sandbox and re-audit):\n" + repair_instruction
            for namespace, state in agent.stream({"messages": [{"role": "user", "content": prompt}]},
                                      config={"recursion_limit": 1000}, stream_mode="values", subgraphs=True):
                current = state.get("messages", [])
                if not namespace:
                    messages = current
                key = tuple(namespace)
                for msg in current[seen.get(key, 0):]:
                    calls = getattr(msg, "tool_calls", None) or []
                    if calls:
                        names = ", ".join(c["name"] for c in calls)
                        role = "subagent" if namespace else "lead"
                        print(f"[{time.monotonic() - start:.0f}s] {role} tools: {names}", flush=True)
                    elif isinstance(getattr(msg, "content", None), str) and msg.content.startswith("ERROR:"):
                        print(f"[{time.monotonic() - start:.0f}s] source warning: {redact(msg.content[:240])}", flush=True)
                seen[key] = len(current)
            # Finalizer and validator run in the sandbox, even if the agent ended
            # prematurely. Never repair artifacts on the host after download.
            final = backend.execute(f"python3 {PREPARE_PATH} && python3 {FINALIZER_PATH} && python3 {VALIDATOR_PATH}")
            if final.exit_code != 0 or "OK:" not in final.output:
                raise RuntimeError("sandbox final validation failed: " + final.output[:900])
            audit = download(backend, [AUDIT_PATH]).get(AUDIT_PATH)
            if not audit or not audit.strip():
                raise RuntimeError("citation audit missing; no output saved")
            audit_text = audit.decode("utf-8")
            if audit_has_unresolved(audit_text):
                raise RuntimeError("citation audit has unresolved FAIL/UNVERIFIED verdicts; no output saved")
            roles = summarize(messages, 0, model_name)["task_roles"]
            if roles.get("researcher", 0) < 3 or roles.get("citation-checker", 0) < 1:
                raise RuntimeError("required researcher/checker delegations missing; no output saved")
            evidence = {"citation-audit.md": audit}
            listing = backend.execute(f"find {WORKDIR}/research/notes -maxdepth 1 -type f -name '*.md' -print")
            if listing.exit_code != 0:
                raise RuntimeError("cannot list researcher notes; no output saved")
            note_paths = [p.strip() for p in listing.output.splitlines()
                              if p.strip().startswith(f"{WORKDIR}/research/notes/") and p.strip().endswith(".md")]
            if len(note_paths) < 3:
                raise RuntimeError("fewer than three researcher note files; no output saved")
            note_files = download(backend, note_paths)
            for sandbox_path in note_paths:
                data = note_files.get(sandbox_path)
                if not data:
                    raise RuntimeError("missing researcher evidence; no output saved")
                name = Path(sandbox_path).name
                if name in evidence:
                    raise RuntimeError("duplicate evidence filename; no output saved")
                evidence[name] = data
            path = save_outputs(backend, topic, messages, time.monotonic() - start, model_name, evidence=evidence)
        print(f"Saved {path}", flush=True)
        return 0
    except Exception as exc:
        if os.getenv("SANDBOX", "daytona").lower() == "daytona" and is_daytona_credit_error(exc):
            print("Daytona credits exhausted; retrying this topic on Docker.", flush=True)
            previous = os.environ.get("SANDBOX")
            os.environ["SANDBOX"] = "docker"
            try:
                return main(topic, seed_dir=seed_dir, repair_instruction=repair_instruction)
            finally:
                if previous is None:
                    os.environ.pop("SANDBOX", None)
                else:
                    os.environ["SANDBOX"] = previous
        print("FAILED: " + redact(f"{type(exc).__name__}: {exc}"), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main(" ".join(sys.argv[1:])))

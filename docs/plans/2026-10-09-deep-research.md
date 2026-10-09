# Deep Research lab implementation

Approved design: implement the four student modules in the current checkout,
keep provided model/sandbox/finalizer/self-check unchanged, and generate the five
reports through the actual agent and sandbox. No manual report edits.

## Execution

1. Add offline unit tests for citation validation, retry, source parsing, safe
   filenames, usage accounting, and failed-run output handling; observe failures.
2. Implement the standard-library citation validator.
3. Implement host network tools with compact results, bounded retries, arXiv
   pacing, Exa SSE parsing and secret redaction.
4. Implement lead/researcher/checker prompts, explicit delegation, evidence
   format, and independent model/tool limits.
5. Implement sandbox orchestration and validate downloaded artifacts before
   saving their exact bytes. Capture lead usage and source-family metadata.
6. Run offline tests, exercise all five source tools and check model access.
7. Generate all five preset reports, finalize and validate inside each sandbox,
   verify a sample of claims, then run self_check and protected-file checks.

## Acceptance

- Five report/source/meta triplets; each has at least three task calls and three
  source families with matching URLs, valid references and the template headings.
- Report/source bytes are unchanged after download; failed runs create no report.
- API keys stay on the host, are ignored by Git and do not appear in errors.
- Remote Git publication remains under the user's control.

## Verified execution ledger

- Initial offline suite: 13 tests failed against scaffold TODOs (red).
- Implemented student modules; initial 13 tests passed outside the Windows
  filesystem sandbox. Python TemporaryDirectory ACLs require that test context.
- Added real regressions for CRLF headings, arXiv canonical IDs, malformed
  citation ranges, Exa text mentioning rate limits, exhausted arXiv retries,
  and credit-only Docker fallback. Final current offline suite: 22 tests passed.
- All five source tools exercised successfully in the initial tool smoke test.
  Later arXiv requests returned HTTP 429; bounded retry and a shared cooldown
  prevent research agents from repeatedly amplifying the outage.
- OpenAI model list and a real short completion confirmed gpt-6-luna access.
  Removed literal placeholder brackets from LAB_MODEL without changing keys.
- Read-only independent review found the malformed-range and Exa false-positive
  defects; both reproduced red then passed after repair. Review subsequently
  reported no remaining confirmed findings in its inspected snapshot.
- Daytona sandbox I/O and four concurrent executions passed in an 11.8s
  preflight. Two long research attempts later failed creating proxy sessions
  with connection reset/timeout; neither saved a report. No credit error observed.
- Stopped the third cloud run before proceeding to more topics. Its sandbox
  cca4e407-1544-4939-a01b-af99c7c48eb5 was identified by uploaded validator SHA-256
  and deleted. This cleanup targeted only this lab's verified resource.
- Docker engine 29.8.0 is available outside the Windows tool sandbox. Default
  Python 3.12 image startup timed out; cached python:3.11-slim passed I/O and
  four concurrent executions in 1.3s, reporting Python 3.11.16.
- Final generation batch started with process environment SANDBOX=docker and
  SANDBOX_IMAGE=python:3.11-slim. Reports remain pending until self_check passes.
- Reproduced an SSE stream which delivers a complete RPC result but stays open;
  the original buffered request reads beyond the result. Streaming parser test
  failed then passed after closing at the first matching result. Real Exa fetch
  took 0.8s after repair. OpenAI requests previously had no deadline; now both
  sync/async clients use 120s, and a real bounded completion took 2.4s.
- Preserved the first machine-generated world-model draft/notes using docker cp.
  Host and sandbox SHA-256 matched exactly for report and sources; citation
  validator returned no problems. This is an ignored resume input, not a submission.
- Resume batch refused missing/unresolved audits. Added deterministic audit
  writer (fixed sandbox path, replaces prior audit without touching reports),
  and a middleware rejecting serial initial researcher dispatch before execution.
- Current full offline suite: 28 tests passed, including writer replacement,
  parallel dispatch, explicit Markdown verdicts, typed credit fallback, and
  rollback of reports/evidence on simulated evidence installation failure.
- Resumed Docker run exported world-model, RL-reasoning and video reports. The
  LLM-agents checkpoint was retained instead of published because it still had
  only two discovery families. Added a sandbox family gate before auditor
  delegation; its regression test failed then passed. Invalid checkpoints now
  fall back to a fresh run instead of repeating a pre-agent failure.
- Latest complete offline suite: 30 tests passed. Independent code review found
  no remaining concrete issue in these fixes. Reviewer identified an ambiguous
  GPT-4o parameter attribution in the world-model seed; an authorized fresh
  agent pass is repairing it in the sandbox. Final submission checks pending.
- Final verification: all five report/source/meta triplets exported from Docker;
  `python self_check.py` exited 0, all five topics and git/secrets OK, READY to
  submit. Offline suite: 31 tests passed. Report/source SHA-256 matched saved
  metadata; all five audits contained at least three PASS verdicts and no
  unresolved verdicts; each topic had at least three discovery families and
  three researcher calls. LLM metadata URL repair occurred inside
  Docker, followed by finalizer, validator and fresh audit; no host report edits.
- Actual configured-key scan found no key values in tracked or untracked
  submission files or `.env` Git history. Provided model/sandbox/self-check/
  finalizer and report template have no diff. `git diff --check` passed. No
  deepresearch containers remain. No commit, push or external submission made.
- Token metadata describes only each final run's lead messages; it excludes
  subagents and prior failed/resumed runs. RUBRIC manual grading remains external.
- Content review then found semantic citation swaps in the LLM candidate between
  CodeAct, AgentOptimizer and the evaluation survey despite the numeric validator
  passing. Regenerated that topic with explicit review instructions, three
  parallel researcher tasks and four targeted checker passes. That LLM candidate
  had arxiv/hf-daily/web families, report hash
  `0fd44b21f3305104616d863e146519c683c93794ccf1bd637837d1c534340709`.
  Fresh self_check again exited 0 READY; all five hash/audit/provenance-role
  checks and configured-key scan passed. Latest offline suite: 31 tests passed.
- A second semantic review found further positional citation drift outside the
  three initial targets. Added stdlib `prepare_citations.py`: agents write URL
  markers in draft.md, then compile to CURRENT registry numbers inside sandbox
  before running the unchanged finalizer. Draft repairs preserve source URLs
  through renumbering. Compiler rejects duplicate/nonpositive/noninteger n,
  duplicate URLs, stale positional citations and malformed unresolved markers.
  Regression tests failed then passed; current full suite: 33 tests passed.
- Regenerated the LLM survey using this workflow and requiring the auditor to
  compare all named-method mappings, plus three primary-evidence claims. Final
  LLM survey: 2031 words, arxiv/hf-search/web, report SHA-256
  `683432d0b75a71695e7ec5c5e77d1fc66f05c30b0e53f1f40b0120fed3e4948b`.
  Fresh self_check exited 0 READY; all five hash/audit/role/family checks and
  configured-key scan passed. No deepresearch containers remain. Independent
  semantic review confirmed all 12 named-method citations across TL;DR, body,
  table and synthesis match the correct sources; audit contains that full
  mapping table and three primary-evidence PASS verdicts. No blocker remained.
  Final verified word counts including references, in topics.txt order:
  2103 / 2164 / 2031 / 2066 / 2150. No commit, push or external submission made.

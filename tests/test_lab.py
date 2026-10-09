import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import check_citations as citations
import research
import tools
import httpx
import agents


def source(n=1, url="https://example.org/paper", family="web"):
    return dict(n=n, url=url, id=str(n), title="Paper", date="2025-01-01", source=family)


class CitationTests(unittest.TestCase):
    def test_malformed_range_returns_problem(self):
        self.assertTrue(citations.check("Claim [1-2-3].\n## References\n[1] https://example.org/paper", [source()]))

    def test_valid_report(self):
        self.assertEqual([], citations.check("Claim [1].\n## References\n[1] Paper. https://example.org/paper\n", [source()]))

    def test_reference_does_not_count_as_body_citation(self):
        problems = citations.check("Claim.\n## References\n[1] https://example.org/paper", [source()])
        self.assertTrue(any("never cited" in p for p in problems))

    def test_grouped_citations(self):
        sources = [source(i, f"https://example.org/{i}") for i in range(1, 4)]
        refs = "\n".join(f"[{s['n']}] {s['url']}" for s in sources)
        self.assertEqual([], citations.check("Claim [1, 2] and [2-3].\n## References\n" + refs, sources))

    def test_code_and_links_do_not_count(self):
        for body in ("```text\n[1]\n```", "`[1]`", "[1](https://example.org/paper)"):
            with self.subTest(body=body):
                self.assertTrue(any("never cited" in p for p in citations.check(body + "\n## References\n[1] https://example.org/paper", [source()])))

    def test_bad_sources_never_crash(self):
        for sources in (None, {}, [], [None], [source(True)], [source("1")], [source(1, "javascript:x")]):
            with self.subTest(sources=sources):
                self.assertTrue(citations.check("Claim [1].", sources))

    def test_duplicate_numbers_urls_and_references(self):
        self.assertTrue(citations.check("Claim [1].\n## References\n[1] https://example.org/paper\n[1] https://other.org/", [source(), source()]))

    def test_unknown_citation_and_mismatched_or_bundled_url(self):
        for refs in ("[1] https://wrong.org/", "[1] https://example.org/paper https://other.org/"):
            self.assertTrue(citations.check("Claim [1][9].\n## References\n" + refs, [source()]))


class RetryTests(unittest.TestCase):
    def test_exa_returns_at_rpc_result_without_waiting_for_stream_end(self):
        class OpenEventStream(httpx.SyncByteStream):
            def __iter__(self):
                yield b'data: {"jsonrpc":"2.0","id":1,"result":{"content":[{"type":"text","text":"evidence"}]}}\n\n'
                raise AssertionError("read past the complete RPC result")
        transport = httpx.MockTransport(lambda req: httpx.Response(200, headers={"content-type": "text/event-stream"}, stream=OpenEventStream()))
        with httpx.Client(transport=transport) as client:
            with patch("tools.httpx.post", side_effect=lambda url, **kwargs: client.post(url, **kwargs)), \
                 patch("tools.httpx.stream", side_effect=lambda method, url, **kwargs: client.stream(method, url, **kwargs)):
                self.assertEqual("evidence", tools._exa_call("web_fetch_exa", {"urls": ["https://example.org"]}))
    @patch("tools.time.sleep")
    @patch("tools._request", side_effect=tools.RetryableError("HTTP 429"))
    @patch("tools._arxiv_cooldown_until", 0)
    def test_arxiv_exhaustion_prevents_immediate_repeated_searches(self, request, sleep):
        first = tools.arxiv_search.invoke({"query": "world model"})
        second = tools.arxiv_search.invoke({"query": "reasoning"})
        self.assertTrue(first.startswith("ERROR:"))
        self.assertTrue(second.startswith("ERROR:"))
        self.assertEqual(7, request.call_count)
    @patch("tools._request")
    @patch("tools.time.sleep")
    def test_arxiv_canonical_id_and_query(self, sleep, request):
        request.return_value = httpx.Response(200, text='<feed xmlns="http://www.w3.org/2005/Atom"><entry><id>http://arxiv.org/abs/2501.00001v3</id><title>Title</title><published>2025-01-01T00:00:00Z</published><summary>Evidence</summary></entry></feed>')
        result = json.loads(tools.arxiv_search.invoke({"query": '"world-model": AND OR', "max_results": 2}))
        self.assertEqual("2501.00001", result[0]["id"])
        self.assertEqual("https://arxiv.org/abs/2501.00001", result[0]["url"])
        self.assertEqual("all:world-model", request.call_args.kwargs["params"]["search_query"])
    def test_exa_sse_and_http200_throttle(self):
        response = httpx.Response(200, text='event: message\ndata: {"jsonrpc":"2.0","result":{"content":[{"type":"text","text":"found evidence"}]}}\n\n')
        self.assertEqual("found evidence", tools._parse_exa(response))
        for result in ({"_meta": {"rateLimited": True}, "content": []},
                       {"content": [{"type": "text", "text": "Rate limit exceeded"}]},
                       {"isError": True, "content": [{"type": "text", "text": "Too many requests"}]}):
            with self.subTest(result=result), self.assertRaises(tools.RetryableError):
                tools._parse_exa(httpx.Response(200, json={"result": result}))

    def test_exa_valid_text_about_rate_limits_is_not_throttling(self):
        text = "The system is designed to handle rate-limited APIs by adding backoff and retries."
        self.assertEqual(text, tools._parse_exa(httpx.Response(200, json={"result": {"content": [{"type": "text", "text": text}], "_meta": {"rateLimitRemaining": 10}}})))

    @patch.dict("os.environ", {"EXA_API_KEY": "private-testing-secret"})
    def test_error_redacts_secret(self):
        self.assertNotIn("private-testing-secret", tools._error(ValueError("url?exaApiKey=private-testing-secret")))

    @patch("tools.httpx.get")
    def test_retryable_http_and_date_header(self, get):
        get.return_value = httpx.Response(429, headers={"Retry-After": "5"}, request=httpx.Request("GET", "https://example.org"))
        with self.assertRaises(tools.RetryableError) as context:
            tools._request("get", "https://example.org")
        self.assertEqual(5, context.exception.retry_after)
        self.assertEqual(0, tools._retry_after("Wed, 01 Jan 2020 00:00:00 GMT"))

    @patch("tools.time.sleep")
    def test_retries_and_caps_without_last_sleep(self, sleep):
        with patch("tools.random.uniform", return_value=0.25):
            with self.assertRaises(tools.RetryableError):
                tools.with_retry(lambda: (_ for _ in ()).throw(tools.RetryableError("busy")), attempts=4, base=1, cap=3)
        self.assertEqual([1.25, 2.25, 3], [call.args[0] for call in sleep.call_args_list])

    @patch("tools.time.sleep")
    def test_retry_after_and_no_retry_for_other_errors(self, sleep):
        calls = iter([tools.RetryableError("busy", retry_after=7), "ok"])
        def fn():
            item = next(calls)
            if isinstance(item, Exception):
                raise item
            return item
        self.assertEqual("ok", tools.with_retry(fn))
        sleep.assert_called_once_with(7)
        with self.assertRaises(ValueError):
            tools.with_retry(lambda: (_ for _ in ()).throw(ValueError("bad")))

    @patch("tools.httpx.get")
    def test_empty_arxiv_skips_network(self, get):
        self.assertEqual("NO RESULTS", tools.arxiv_search.invoke({"query": "\" : AND OR"}))
        get.assert_not_called()


class ResearchTests(unittest.TestCase):
    def test_stable_url_citations_survive_source_reordering(self):
        from prepare_citations import render
        text = "CodeAct [@https://example.org/code]. Judge [@https://example.org/judge]."
        sources = [{"n": 7, "url": "https://example.org/code"}, {"n": 2, "url": "https://example.org/judge"}]
        self.assertEqual("CodeAct [7]. Judge [2].\n", render(text, sources))
        sources[0]["n"], sources[1]["n"] = 1, 9
        self.assertEqual("CodeAct [1]. Judge [9].\n", render(text, sources))
        with self.assertRaises(ValueError):
            render("stale [7]", sources)
        with self.assertRaises(ValueError):
            render("missing [@https://example.org/missing]", sources)

    def test_compiler_rejects_duplicate_numbers_and_unresolved_markers(self):
        from prepare_citations import render
        with self.assertRaises(ValueError):
            render("A [@https://example.org/a] B [@https://example.org/b]", [
                {"n": 1, "url": "https://example.org/a"}, {"n": 1, "url": "https://example.org/b"}])
        for n in (True, 0, -1, "1"):
            with self.subTest(n=n), self.assertRaises(ValueError):
                render("A [@https://example.org/a]", [{"n": n, "url": "https://example.org/a"}])
        with self.assertRaises(ValueError):
            render("Bad [@https://example.org/a ]", [{"n": 1, "url": "https://example.org/a"}])

    def test_auditor_blocked_until_three_real_source_families(self):
        from types import SimpleNamespace
        backend = unittest.mock.Mock()
        middleware = agents.SourceFamilyMiddleware(backend)
        request = SimpleNamespace(tool_call=dict(name="task", args={"subagent_type": "citation-checker"}, id="audit"))
        handler = unittest.mock.Mock(return_value="audited")
        backend.execute.return_value = SimpleNamespace(exit_code=0, output='["hf-search", "web"]')
        self.assertIn("ERROR", middleware.wrap_tool_call(request, handler).content)
        handler.assert_not_called()
        backend.execute.return_value.output = '["hf-daily", "hf-search", "web"]'
        self.assertEqual("audited", middleware.wrap_tool_call(request, handler))

    def test_auditor_blocks_noncanonical_source_url(self):
        from types import SimpleNamespace
        backend = unittest.mock.Mock()
        backend.execute.return_value = SimpleNamespace(exit_code=0, output=json.dumps({
            "families": ["arxiv", "hf-search", "web"], "issues": ["canonical URL required for 2402.11359: https://huggingface.co/papers/2402.11359"]}))
        middleware = agents.SourceFamilyMiddleware(backend)
        request = SimpleNamespace(tool_call=dict(name="task", args={"subagent_type": "citation-checker"}, id="audit"))
        result = middleware.wrap_tool_call(request, unittest.mock.Mock())
        self.assertIn("canonical URL required", result.content)

    def test_unusable_checkpoint_falls_back_to_fresh_research(self):
        from scripts import run_topics
        with tempfile.TemporaryDirectory(dir=Path(__file__).resolve().parents[1]) as tmp:
            candidate = Path(tmp) / research.slugify("topic")
            (candidate / "notes").mkdir(parents=True)
            (candidate / "report.md").write_text("unfinished [1]", encoding="utf-8")
            (candidate / "sources.json").write_text("broken", encoding="utf-8")
            for n in range(3):
                (candidate / "notes" / f"{n}.md").write_text("note", encoding="utf-8")
            with patch("sys.argv", ["run_topics", "--indices", "0", "--resume-root", tmp]), \
                 patch.object(run_topics, "load_topics", return_value=["topic"]), \
                 patch.object(run_topics, "load_validator"), \
                 patch.object(run_topics, "check_topic", return_value=["missing"]), \
                 patch.object(research, "main", return_value=0) as run:
                self.assertEqual(0, run_topics.main())
                run.assert_called_once_with("topic", seed_dir=None)

    def test_initial_research_dispatch_requires_a_parallel_batch(self):
        from types import SimpleNamespace
        from langchain_core.messages import AIMessage
        middleware = agents.ParallelResearchMiddleware()
        calls = [dict(name="task", args={"subagent_type": "researcher"}, id=str(i)) for i in range(3)]
        handler = unittest.mock.Mock(return_value="executed")
        req = SimpleNamespace(tool_call=calls[0], state={"messages": [AIMessage(content="", tool_calls=calls[:1])]})
        self.assertIn("ERROR:", middleware.wrap_tool_call(req, handler).content)
        handler.assert_not_called()
        req.state["messages"] = [AIMessage(content="", tool_calls=calls)]
        self.assertEqual("executed", middleware.wrap_tool_call(req, handler))
        # Follow-up research may be a single focused call after the real batch.
        req.state["messages"] = [AIMessage(content="", tool_calls=calls[:1])]
        self.assertEqual("executed", middleware.wrap_tool_call(req, handler))
    def test_auditor_can_replace_its_fixed_file(self):
        from types import SimpleNamespace
        class Backend:
            def __init__(self):
                self.files = {}
            def upload_files(self, files):
                self.files.update(files)
                return [SimpleNamespace(path=p, error=None) for p, _ in files]
        backend = Backend()
        checker = next(s for s in agents.build_subagents(backend) if s["name"] == "citation-checker")
        writer = next(t for t in checker["tools"] if t.name == "save_citation_audit")
        self.assertTrue(writer.invoke({"audit": "Status: FAIL\n"}).startswith("OK:"))
        self.assertTrue(writer.invoke({"audit": "Status: PASS\n"}).startswith("OK:"))
        self.assertEqual(b"Status: PASS\n", backend.files[agents.AUDIT_PATH])
    def test_model_requests_are_bounded(self):
        from langchain_openai import ChatOpenAI
        model = ChatOpenAI(model="gpt-6-luna", api_key="offline-test")
        bounded = research.bound_model_requests(model)
        self.assertEqual(120, bounded.root_client.timeout)
        self.assertEqual(120, bounded.root_async_client.timeout)
        self.assertEqual("none", bounded.reasoning_effort)
    def test_markdown_audit_verdicts(self):
        for audit in ("- **Verdict:** FAIL", "## UNVERIFIED", "| 1 | **FAIL** |", "Status: UNVERIFIED", "### Claim 1 — FAIL"):
            self.assertTrue(research.audit_has_unresolved(audit), audit)
        for audit in ("No FAIL/UNVERIFIED claims remain.", "- **Verdict:** PASS", "## No unverified claims", "| 1 | PASS |"):
            self.assertFalse(research.audit_has_unresolved(audit), audit)

    def test_model_credit_error_is_not_a_daytona_credit_error(self):
        from daytona.common.errors import DaytonaError
        self.assertTrue(research.is_daytona_credit_error(DaytonaError("Insufficient credits")))
        self.assertFalse(research.is_daytona_credit_error(RuntimeError("Insufficient credits")))

    def test_only_credit_errors_trigger_docker_fallback(self):
        for message in ("Insufficient credits", "Usage limit exceeded: no remaining credit", "Credit balance exhausted"):
            self.assertTrue(research.is_credit_error(message))
        for message in ("Connection reset by peer", "HTTP 429", "Invalid API key", "The credit feature is enabled"):
            self.assertFalse(research.is_credit_error(message))
    @patch("research.download")
    def test_valid_output_preserves_downloaded_bytes(self, download):
        from langchain_core.messages import AIMessage
        sources = [source(1, "https://arxiv.org/abs/1234.12345", "arxiv"),
                   source(2, "https://huggingface.co/papers/1234.12346", "hf-search"), source(3)]
        sources[0]["id"], sources[1]["id"] = "1234.12345", "1234.12346"
        raw_sources = json.dumps(sources, indent=4).encode()
        raw_report = ("# Survey\r\n## TL;DR\r\nClaim [1][2][3].\r\n## Background\r\n"
                      "## Theme one\r\n## Theme two\r\n## Theme three\r\n## Trends and open problems\r\n"
                      "## References\r\n" + "\r\n".join(f"[{s['n']}] {s['url']}" for s in sources) + "\r\n").encode()
        raw_report = raw_report.replace(b"## Background\r\n", b"## Background: definitions and foundations\r\n")
        download.return_value = {research.REPORT_PATH: raw_report, research.SOURCES_PATH: raw_sources}
        calls = [dict(name="task", args={}, id=str(i)) for i in range(3)]
        with tempfile.TemporaryDirectory(dir=Path(__file__).resolve().parents[1]) as tmp:
            target = Path(tmp) / "reports"
            path = research.save_outputs(None, "test", [AIMessage(content="", tool_calls=calls)], 2, "model", target)
            self.assertEqual(raw_report, path.read_bytes())
            self.assertEqual(raw_sources, (target / "test.sources.json").read_bytes())
            self.assertEqual(3, json.loads((target / "test.meta.json").read_text())["n_sources"])
            # Inject failure when installing evidence AFTER the report files;
            # the previous verified triplet must be restored byte-for-byte.
            original_replace = Path.replace
            def fail_evidence(path, destination):
                if Path(destination).name == "citation-audit.md":
                    raise OSError("simulated evidence disk error")
                return original_replace(path, destination)
            before = {p.name: p.read_bytes() for p in target.iterdir()}
            with patch.object(Path, "replace", fail_evidence), self.assertRaises(OSError):
                research.save_outputs(None, "test", [AIMessage(content="", tool_calls=calls)], 3, "new-model", target,
                                      evidence={"citation-audit.md": b"Status: PASS\n"})
            self.assertEqual(before, {p.name: p.read_bytes() for p in target.iterdir()})
            self.assertFalse((Path(tmp) / "evidence" / "test").exists())
            with self.assertRaises(RuntimeError):
                research.save_outputs(None, "test", [AIMessage(content="", tool_calls=calls)], 3, "new-model", target,
                                      evidence={"citation-audit.md": None})
            self.assertEqual(before, {p.name: p.read_bytes() for p in target.iterdir()})

    def test_slug_is_safe(self):
        for topic in ("../../x", "", "a" * 100, "世界 / models"):
            slug = research.slugify(topic)
            self.assertTrue(slug)
            self.assertLessEqual(len(slug), 60)
            self.assertNotIn("/", slug)
            self.assertNotIn("\\", slug)

    def test_usage_counts_only_lead_messages(self):
        from langchain_core.messages import AIMessage
        msg = AIMessage(content="", tool_calls=[dict(name="task", args={}, id="a"), dict(name="execute", args={}, id="b")], usage_metadata=dict(input_tokens=10, output_tokens=3, total_tokens=13))
        summary = research.summarize([msg], 1.234, "test")
        self.assertEqual(1, summary["subagent_calls"])
        self.assertEqual({"input": 10, "output": 3}, summary["tokens"])
        self.assertEqual(1.2, summary["elapsed_s"])

    @patch("research.download")
    def test_missing_or_corrupt_outputs_write_nothing(self, download):
        with tempfile.TemporaryDirectory(dir=Path(__file__).resolve().parents[1]) as tmp:
            target = Path(tmp) / "reports"
            for files in ({}, {research.REPORT_PATH: b"", research.SOURCES_PATH: b"[]"}, {research.REPORT_PATH: b"report", research.SOURCES_PATH: b"broken"}):
                download.return_value = files
                with self.assertRaises(RuntimeError):
                    research.save_outputs(None, "topic", [], 1, "model", target)
                self.assertFalse(target.exists())


if __name__ == "__main__":
    unittest.main()

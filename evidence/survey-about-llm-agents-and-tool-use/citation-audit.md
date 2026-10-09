# Citation audit — final report review

Scope: Reviewed report `/tmp/work/report/report.md`, source registry `/tmp/work/research/sources.json`, and four researcher notes (`architectures.md`, `learning.md`, `evaluation.md`, `followup.md`). The report contains **12 named mappings**, references [1]–[12]. All mapping assignments and claims were checked against the notes and their listed source identities, titles, URLs, and dates. Exactly three substantive primary-source claim checks were performed, each from a distinct work, fetching only the referenced primary sources relevant to those claims.

## Mapping review — all 12 named works

| Ref | Work and mapping locations | Audit finding |
|---|---|---|
| [1] | ReAct — TL;DR, Background, Architectures, table, synthesis/open problems | Correct title and arXiv URL; registry date 2023-03-10 matches note. Summary of interleaved reasoning/actions and task-specific results is appropriately scoped. No apparent mapping error. |
| [2] | Toolformer — TL;DR, Background, Architectures, table, synthesis/open problems | Correct title/URL/date; noted method and limitations align with research notes. Wording does not claim it has interactive chaining. |
| [3] | CodeAct — TL;DR, Architectures, table, Trends, open problems | Correct title/URL/date. Abstract headline is explicitly qualified as “up to” and not uniform; execution-safety gap is stated. |
| [4] | AgentOptimizer — TL;DR, Learning, comparative synthesis/open problems | Correct title/URL; registry date unknown is consistent with note. Report avoids unsupported exact effect sizes and flags limited evidence. |
| [5] | ToolRL — TL;DR, Learning, Trends, open problems | Correct title/URL/date. Abstract aggregate gain wording is attributed to the primary abstract and carefully scoped; API-Bank Qwen2.5 1.5B detailed numbers are attributed to follow-up full-text evidence in note and distinguished as setup-specific. No unsupported sample-efficiency comparison asserted. |
| [6] | API-Bank — TL;DR, Background, Evaluation, Trends/open problems | Correct title/URL/date. Report properly distinguishes the runnable 73-tool/314-dialogue/753-call evaluation from the larger training collection; no scope conflation. |
| [7] | AgentBench — TL;DR, Evaluation, Trends/open problems | Correct title/URL/date. Report says **25** models, matching the cited Hugging Face record fetched in this audit, rather than the 29 in older research-note primary abstract excerpt. |
| [8] | ToolEmu — TL;DR, Evaluation, Trends/open problems | Correct title/URL/date. Claims about benchmark size, human validation, and evaluator-identified failure rate are qualified; emulation and threat-model limitations are disclosed. |
| [9] | AgentDojo — TL;DR, Evaluation, Trends/open problems | Correct title/URL/date. The report uses the primary title form and bounds findings to benchmark conditions. |
| [10] | Evaluation and Benchmarking of LLM Agents: A Survey — TL;DR, Background, Evaluation, Trends/open problems | Correct title/URL/date. Taxonomy is identified as synthesis rather than empirical validation. |
| [11] | Search-R1 — Learning | Correct title/URL; registry date unknown consistent with note. Search-centered scope and seven-dataset claims are bounded; no claim of general function-calling evidence. |
| [12] | Tool-R1 — Learning | Correct title/URL/date. The fetched primary full-text page supports executable Python, multi-step tool use, and about 10% GAIA gain; report does not claim a measured sample-efficiency quantity or detailed comparator breakdown. |

## Three primary-source claim checks

### Claim 1 — AgentBench model count [7]
Report wording: “It contains eight distinct environments, and the cited HF record reports an evaluation of 25 API-based and open-source models.”

URL fetched: https://huggingface.co/papers/2308.03688

Title/date check: Retrieved page title is “AgentBench: Evaluating LLMs as Agents”; it displays “Published: 2023-08-07,” matching registry/reference date.

Supporting excerpt: “currently consists of 8 distinct environments” and “Our extensive test over 25 LLMs (including APIs and open-sourced models).”

Assessment: Exact model count and environment count match the report. The report attributes count specifically to HF record, which is appropriate given the primary-paper abstract excerpt in notes reports 29; the two records evidently describe different record/version text. Avoid presenting 25 as an independently reconciled count across every paper version.

Status: PASS

### Claim 2 — ToolRL aggregate results [5]
Report wording: “Its primary abstract reports a structured reward design and training with GRPO, and reports gains of 17% over base models and 15% over supervised fine-tuned models across diverse benchmarks.”

URL fetched: https://arxiv.org/abs/2504.13958

Title/date check: Retrieved primary page title “ToolRL: Reward is All Tool Learning Needs”; displayed published date 2025-04-16 matches registry.

Supporting excerpt: “apply it to train LLMs using Group Relative Policy Optimization (GRPO). Empirical evaluations across diverse benchmarks demonstrate ... achieving a 17% improvement over base models and a 15% gain over SFT models.”

Assessment: The report tracks the abstract closely and correctly attributes the aggregate percentages to the abstract. The ensuing API-Bank result (44.0%, 20.8%, 24.8%) is identified as follow-up full-text evidence and explicitly tied to a particular model/setup, not passed off as an abstract-wide or universal gain. The notes document that evidence. Detailed exact percentage semantics/baseline aggregation remain dependent on the paper’s experiment definitions, but the report does not overstate them.

Status: PASS

### Claim 3 — Tool-R1 GAIA gain and sample-efficiency wording [12]
Report wording: “Tool-R1 is a further recent direction described as sample-efficient RL for multi-step tool use via executable Python, and the available summary reports about a 10% gain on GAIA; it does not provide an exact sample-efficiency measure or detailed comparative results, so stronger comparisons would exceed the evidence.”

URL fetched: https://huggingface.co/papers/2509.12867 (page identifies source content as https://arxiv.org/html/2509.12867)

Title/date check: Retrieved title matches “Tool-R1: Sample-Efficient Reinforcement Learning for Agentic Tool Use.” Page metadata states published time 2025-09-17; registry/HF discovery date is 2025-09-16. This is a one-day discrepancy between registry discovery date and page’s publication-time metadata; report cites the registry date as a record date, not as independently verified primary publication date.

Supporting excerpt: “general, compositional, and multi-step tool use by generating executable Python code”; dynamic sample queue “to cache and reuse high-quality trajectories”; “Experiments on the GAIA benchmark ... achieving about 10% gain over strong baselines.”

Assessment: The claim of roughly 10% GAIA improvement and multi-step executable-Python method is supported. The source has a qualitative sample-efficiency mechanism (trajectory caching/reuse), but the report carefully states it lacks an exact sample-efficiency measure and detailed comparative results. No stronger efficiency result is claimed.

Status: PASS

## Unsupported claims / unresolved issues

No remaining unsupported substantive claim was identified in the reviewed mapping. The three sampled claims pass; the overall mapping review is based on report-to-notes consistency, while only those three claims were freshly retrieved from distinct primary sources as required.

Bibliographic date nuance: [12] registry/reference date is 2025-09-16 while fetched page metadata says 2025-09-17. This is not a substantive report error because the bibliography’s date is the HF record date, but the date type should remain understood as a discovery-record date rather than an independently established arXiv posting date. [7] HF record reports 25 models, whereas researcher notes quote 29 from the primary arXiv abstract; the report explicitly identifies its count as the HF record’s count, so its wording is supported, though this version/record discrepancy remains noteworthy.

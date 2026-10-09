# Genuine discovery-family records and primary verification for LLM agent/tool-use evaluations

```json
[
  {
    "id": "2504.13958",
    "url": "https://arxiv.org/abs/2504.13958",
    "title": "ToolRL: Reward is All Tool Learning Needs",
    "date": "2025-04-16",
    "source": "hf-search",
    "claims": [
      "HF paper search lists ToolRL with publication date 2025-04-16 and describes it as a study of reward design for tool-use reinforcement learning.",
      "The primary arXiv page describes a systematic study of reward strategies for tool selection and application, then trains LLMs using GRPO and a proposed reward design.",
      "The primary page abstract reports evaluations across diverse benchmarks and claims 17% improvement over base models and 15% over SFT models.",
      "Web-search evidence reports evaluation on BFCL, API-Bank, and Bamboogle; for the Qwen2.5 1.5B variant, API-Bank accuracy in the cited results is 44.0% for the authors' GRPO cold-start method versus 20.8% for raw and 24.8% for SFT400.",
      "The paper identifies limited SFT generalization to unfamiliar or complex tool-use scenarios and challenges in using coarse answer-matching rewards as motivation for its finer-grained reward design."
    ],
    "evidence": [
      "HF search: published 2025-04-16; title: ToolRL: Reward is All Tool Learning Needs; summary: A comprehensive study on reward design for tool use within reinforcement learning improves LLMs' tool use capabilities and generalization performance over supervised fine-tuning.",
      "Primary arXiv fetch: 'we present the first comprehensive study on reward design for tool selection and application tasks within the RL paradigm' and 'achieving a 17% improvement over base models and a 15% gain over SFT models.'",
      "Web search: 'We evaluate our approach on the Berkeley Function Call Leaderboard (BFCL)' and 'We also present results on API-Bank' and 'Bamboogle'; retrieved table reports Qwen2.5-1.5B-Instruct raw 20.8%, SFT400 24.8%, and GRPO Cold Start 44.0% API-Bank accuracy."
    ],
    "limitations": [
      "The arXiv page itself does not expose a submission date in the fetched text; the date above is the HF search published field, corroborated by web-search primary-page metadata.",
      "The 17% and 15% abstract improvements are reported without benchmark-by-benchmark detail in the fetched abstract; do not interpret them as universal gains.",
      "The API-Bank Qwen result is from retrieved web-search text rather than the fetched arXiv excerpt; evaluation depends on the paper's setup and models."
    ]
  },
  {
    "id": "2304.08244",
    "url": "https://arxiv.org/abs/2304.08244v2",
    "title": "API-Bank: A Comprehensive Benchmark for Tool-Augmented LLMs",
    "date": "2023-04-14",
    "source": "hf-search",
    "claims": [
      "HF search returned an actual API-Bank record, dated 2023-04-14, with the matching title.",
      "The paper introduces an executable evaluation system with 73 API tools and 314 annotated tool-use dialogues containing 753 API calls to assess planning, retrieval, and API calling.",
      "It also reports a training set of 1,888 dialogues from 2,138 APIs in 1,000 domains and says Lynx, initialized from Alpaca, surpasses Alpaca's tool utilization by more than 26 points.",
      "The abstract says GPT-4 excels in planning and notes substantial room for further improvement in tool use."
    ],
    "evidence": [
      "HF search: published 2023-04-14; title: API-Bank: A Comprehensive Benchmark for Tool-Augmented LLMs.",
      "Primary arXiv page: 'a runnable evaluation system consisting of 73 API tools' and '314 tool-use dialogues with 753 API calls'.",
      "Primary arXiv page: 'a comprehensive training set containing 1,888 tool-use dialogues from 2,138 APIs spanning 1,000 distinct domains' and 'Lynx surpasses Alpaca’s tool utilization performance by more than 26 pts'."
    ],
    "limitations": [
      "The evaluation system's 73-tool dialogue set is narrower than the training API catalog; these are separate dataset scopes.",
      "The fetched abstract does not establish how results generalize to live APIs or settings beyond its curated benchmark.",
      "The date reflects the HF record and the arXiv search result for v2, not a separate journal publication date."
    ]
  },
  {
    "id": "2308.03688",
    "url": "https://arxiv.org/abs/2308.03688",
    "title": "AgentBench: Evaluating LLMs as Agents",
    "date": "2023-08-07",
    "source": "hf-search",
    "claims": [
      "HF search returned an actual AgentBench record dated 2023-08-07.",
      "AgentBench evaluates LLM agents in eight distinct interactive environments; the paper reports a study of 29 API-based and open-source LLMs.",
      "The paper reports a significant performance gap between leading commercial models and many open-source competitors at or below 70B parameters.",
      "Its failure analysis highlights long-term reasoning, decision-making, and instruction following as central obstacles; code training has mixed effects across tasks."
    ],
    "evidence": [
      "HF search: published 2023-08-07; title: AgentBench: Evaluating LLMs as Agents.",
      "Primary arXiv page: 'a multi-dimensional benchmark that consists of 8 distinct environments' and 'extensive test over 29 API-based and open-sourced (OSS) LLMs'.",
      "Primary arXiv page: 'poor long-term reasoning, decision-making, and instruction following abilities are the main obstacles' and 'training on code present ambivalent impacts on different agent tasks.'"
    ],
    "limitations": [
      "The fetched abstract does not enumerate environment-level scores or all environment designs.",
      "The reported model comparisons reflect the benchmark/model versions used in the paper and should not be read as current rankings.",
      "The arXiv page fetch exposed a displayed date of 2025-10-04, apparently page/update metadata; the HF discovery record supplies the requested 2023-08-07 date."
    ]
  },
  {
    "id": "2309.15817",
    "url": "https://arxiv.org/abs/2309.15817",
    "title": "Identifying the Risks of LM Agents with an LM-Emulated Sandbox",
    "date": "2023-09-25",
    "source": "hf-search",
    "claims": [
      "HF search returned ToolEmu under its identifier with a published date of 2023-09-25 and the title Identifying the Risks of LM Agents with an LM-Emulated Sandbox.",
      "ToolEmu uses a language model to emulate tool execution and an LM-based evaluator to detect and quantify agent safety failures.",
      "The primary abstract reports human assessment that 68.8% of failures identified by ToolEmu would be valid real-world agent failures.",
      "Its initial benchmark contains 36 high-stakes toolkits and 144 test cases; the abstract says the safest evaluated agent still had evaluator-identified failures on 23.9% of cases.",
      "The paper explicitly limits the initial benchmark to underspecified instructions and identifies human-heavy case curation as a scalability limitation."
    ],
    "evidence": [
      "HF search: published 2023-09-25; title: Identifying the Risks of LM Agents with an LM-Emulated Sandbox.",
      "Primary arXiv page: 'a framework that uses an LM to emulate tool execution' and 'an LM-based automatic safety evaluator'.",
      "Primary arXiv page: '68.8% of failures identified with ToolEmu would be valid real-world agent failures' and '36 high-stakes toolkits and 144 test cases'.",
      "Primary arXiv page: 'even the safest LM agent exhibits such failures 23.9% of the time'.",
      "Web-search full-text excerpt: 'we focused on the specific threat model of instruction underspecification'; 'test case curation still largely relies on humans.'"
    ],
    "limitations": [
      "Tool execution and safety assessment are LM-emulated/evaluated rather than full execution against all corresponding live tools; validity is not guaranteed by the benchmark itself.",
      "The initial curated benchmark focuses on instruction underspecification, not the full space of malicious attacks or safety risks.",
      "The paper states automated test-case generation frequently violated validity requirements, so human curation remains important."
    ]
  },
  {
    "id": "2406.13352",
    "url": "https://arxiv.org/abs/2406.13352",
    "title": "AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents",
    "date": "2024-06-19",
    "source": "hf-search",
    "claims": [
      "HF search returned AgentDojo dated 2024-06-19; its record title is AgentDojo: A Dynamic Environment to Evaluate Attacks and Defenses for LLM Agents, while the primary arXiv title includes 'Prompt Injection'.",
      "AgentDojo evaluates agents executing tools over untrusted data in a dynamic, extensible environment intended to support new tasks, defenses, and adaptive attacks.",
      "The primary abstract reports 97 realistic tasks and 629 security test cases.",
      "The authors report that state-of-the-art LLMs fail on many benign tasks and that existing prompt-injection attacks violate some, but not all, security properties."
    ],
    "evidence": [
      "HF search: published 2024-06-19; title: AgentDojo: A Dynamic Environment to Evaluate Attacks and Defenses for LLM Agents.",
      "Primary arXiv page title: 'AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents'.",
      "Primary arXiv page: 'not a static test suite, but rather an extensible environment' and '97 realistic tasks ... 629 security test cases'.",
      "Primary arXiv page: 'state-of-the-art LLMs fail at many tasks (even in the absence of attacks)' and attacks 'break some security properties but not all.'"
    ],
    "limitations": [
      "The benchmark's results are specific to its modeled tasks, attacker strategies, and evaluated agent/model configurations; they do not prove general robustness or vulnerability rates in deployment.",
      "The fetched abstract does not provide model-by-model numerical results.",
      "The HF title is a shortened variant; the exact title in the primary arXiv page is retained here."
    ]
  },
  {
    "id": "2507.21504",
    "url": "https://arxiv.org/abs/2507.21504",
    "title": "Evaluation and Benchmarking of LLM Agents: A Survey",
    "date": "2025-07-29",
    "source": "hf-search",
    "claims": [
      "HF search returned the survey as a record published 2025-07-29, with the exact title shown in the primary page.",
      "The survey proposes a two-dimensional taxonomy: evaluation objectives (including behavior, capabilities, reliability, and safety) and evaluation process (including interaction modes, datasets/benchmarks, metric computation, and tooling).",
      "It identifies enterprise evaluation challenges including role-based data access, reliability guarantees, dynamic and long-horizon interaction, and compliance.",
      "The survey calls for holistic, more realistic, and scalable evaluation approaches."
    ],
    "evidence": [
      "HF search: published 2025-07-29; title: Evaluation and Benchmarking of LLM Agents: A Survey.",
      "Primary arXiv page: 'a two-dimensional taxonomy' organized by 'evaluation objectives' and 'evaluation process'.",
      "Primary arXiv page: enterprise challenges include 'role-based access to data, the need for reliability guarantees, dynamic and long-horizon interactions, and compliance'.",
      "Primary arXiv page: future directions include 'holistic, more realistic, and scalable evaluation.'"
    ],
    "limitations": [
      "This is a survey and taxonomy rather than a new benchmark or controlled empirical evaluation.",
      "The fetched primary text records KDD '25 conference dates August 3–7, 2025, whereas the HF record gives 2025-07-29; the latter is used as the record's publication date and should not be confused with conference dates."
    ]
  }
]
```

Synthesis: ToolRL studies training-time reward construction for tool selection/application, whereas API-Bank and AgentBench primarily measure tool/agent capability across curated APIs or interactive environments. ToolEmu and AgentDojo emphasize safety, using respectively LM-emulated tools for underspecification risks and dynamic tool environments for prompt-injection robustness; the survey situates these under broader evaluation objectives and processes.

Evidence gaps: ToolRL's HF search record was located, but the requested arXiv search returned NO RESULTS; exact ToolRL primary metadata and abstract were checked by fetching the official arXiv page. Several arXiv fetches show anomalous displayed dates (notably AgentBench and ToolEmu), so dates above use actual HF discovery records; the survey is a taxonomy, not empirical validation, and each benchmark's conclusions remain bounded by its modeled tasks, systems, and evaluators.

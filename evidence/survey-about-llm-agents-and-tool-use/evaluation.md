# Evaluation, reliability, and safety of LLM agents using tools

```json
[
  {
    "id": "2304.08244",
    "url": "https://arxiv.org/abs/2304.08244",
    "title": "API-Bank: A Comprehensive Benchmark for Tool-Augmented LLMs",
    "date": "unknown",
    "source": "web",
    "claims": [
      "API-Bank presents a runnable evaluation system comprising 73 API tools and 314 annotated tool-use dialogues containing 753 API calls.",
      "The benchmark assesses planning, API retrieval, and API calling; its associated training corpus covers 2,138 APIs across 1,000 domains.",
      "The reported experiments found GPT-4 excelled at planning, while error analysis identified substantial room for improvement in tool use."
    ],
    "evidence": [
      "we develop a runnable evaluation system consisting of 73 API tools. We annotate 314 tool-use dialogues with 753 API calls to assess the existing LLMs’ capabilities in planning, retrieving, and calling APIs.",
      "GPT-3.5 exhibits improved tool utilization compared to GPT-3, while GPT-4 excels in planning. However, there is still significant potential for further improvement."
    ],
    "limitations": [
      "The retrieved abstract establishes the benchmark composition and broad findings but does not expose detailed metric definitions or full model-by-model results.",
      "The evaluation is tool-use focused and does not establish broad prompt-injection or deployment safety guarantees."
    ]
  },
  {
    "id": "2308.03688",
    "url": "https://arxiv.org/abs/2308.03688",
    "title": "AgentBench: Evaluating LLMs as Agents",
    "date": "2025-10-04",
    "source": "web",
    "claims": [
      "AgentBench evaluates agent reasoning and decision-making across eight interactive environments.",
      "The authors evaluated 29 API-based and open-source models and report gaps between leading commercial systems and many open-source models up to 70B parameters.",
      "The paper identifies long-term reasoning, decision-making, and instruction following as prominent obstacles."
    ],
    "evidence": [
      "a multi-dimensional benchmark that consists of 8 distinct environments to assess LLM-as-Agent’s reasoning and decision-making abilities.",
      "Our extensive test over 29 API-based and open-sourced (OSS) LLMs",
      "poor long-term reasoning, decision-making, and instruction following abilities are the main obstacles"
    ],
    "limitations": [
      "This is a broad interactive-agent benchmark, not specifically a tool API correctness or security benchmark.",
      "The retrieved arXiv page reports a publication/update date that may differ from original preprint timing; no original submission date was established from retrieved text."
    ]
  },
  {
    "id": "2309.15817",
    "url": "https://arxiv.org/abs/2309.15817",
    "title": "Identifying the Risks of LM Agents with an LM-Emulated Sandbox",
    "date": "2024-05-17",
    "source": "web",
    "claims": [
      "ToolEmu uses an LM to emulate tool execution and an LM-based evaluator to identify failures and quantify associated risk.",
      "Its initial benchmark contains 36 high-stakes toolkits and 144 test cases; the reported safest agent still failed in 23.9% of cases according to the evaluator.",
      "Human evaluation validated 68.8% of failures identified by ToolEmu as realistic real-world agent failures; the evaluator detected 73.1% of failures identified by majority vote of three human annotators."
    ],
    "evidence": [
      "we introduce ToolEmu: a framework that uses an LM to emulate tool execution and enables scalable testing of LM agents against a diverse range of tools and scenarios.",
      "36 high-stakes toolkits and 144 test cases",
      "even the safest LM agent exhibits such failures 23.9% of the time according to our evaluator",
      "68.8% of them were validated by human evaluation to be genuinely risky and have realistic emulation trajectories.",
      "able to identify 73.1% of the failures identified by the majority vote of 3 human annotators"
    ],
    "limitations": [
      "Tool behavior and trajectory judging are LM-emulated/evaluated, so the results do not substitute for execution against every real tool or independently verified real-world outcomes.",
      "The tested threat model centers on ambiguous or underspecified user instructions and risky tool use; it is not a general measure of all agent safety properties."
    ]
  },
  {
    "id": "2406.13352",
    "url": "https://arxiv.org/abs/2406.13352",
    "title": "AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents",
    "date": "unknown",
    "source": "web",
    "claims": [
      "AgentDojo is an extensible environment for evaluating agents that use tools over untrusted data, targeting prompt-injection robustness and defenses.",
      "The reported first version includes 97 realistic tasks and 629 security test cases.",
      "The authors report that current state-of-the-art LLMs fail at many tasks even without attacks, while existing prompt injection attacks break some, but not all, security properties."
    ],
    "evidence": [
      "we introduce AgentDojo, an evaluation framework for agents that execute tools over untrusted data.",
      "97 realistic tasks ... 629 security test cases",
      "state-of-the-art LLMs fail at many tasks (even in the absence of attacks), and existing prompt injection attacks break some security properties but not all."
    ],
    "limitations": [
      "The benchmark focuses on prompt injection in tool-using agents, not general API selection, parameter accuracy, or all dimensions of reliability.",
      "No quantitative attack/defense rates were included in the retrieved abstract text."
    ]
  },
  {
    "id": "2507.21504",
    "url": "https://arxiv.org/abs/2507.21504",
    "title": "Evaluation and Benchmarking of LLM Agents: A Survey",
    "date": "unknown",
    "source": "web",
    "claims": [
      "The survey organizes agent evaluation around objectives (including behavior, capabilities, reliability, safety) and process (including interaction modes, datasets/benchmarks, metric computation, and tooling).",
      "It identifies enterprise challenges including role-based data access, reliability guarantees, dynamic long-horizon interactions, and compliance.",
      "The survey classifies API-Bank as a tool-use/function-calling benchmark and AgentDojo as evaluating resilience against prompt injection; its taxonomy distinguishes reliability from safety."
    ],
    "evidence": [
      "a two-dimensional taxonomy that organizes existing work along (1) evaluation objectives—what to evaluate, such as agent behavior, capabilities, reliability, and safety—and (2) evaluation process—how to evaluate",
      "enterprise-specific challenges, such as role-based access to data, the need for reliability guarantees, dynamic and long-horizon interactions, and compliance",
      "API-Bank ... focus on tool use and function-calling",
      "AgentDojo ... evaluates resilience against prompt injection attacks"
    ],
    "limitations": [
      "A survey synthesizes prior work rather than independently validating benchmark performance.",
      "The retrieved primary page reports conference proceedings metadata but no explicit publication date in the returned text; date is therefore unknown."
    ]
  }
]
```

Synthesis: API-Bank targets API-level planning/retrieval/calling, while AgentBench measures broader interactive reasoning; ToolEmu and AgentDojo assess distinct safety risks—underspecified risky actions and prompt injection through untrusted tool data. The survey usefully separates capability, reliability, and safety objectives, but neither capability success nor safety scores alone establish robust real-world reliability.

Gaps: The exact requested records were identified for all named methods, but the required arxiv_search and hf_search_papers records were not obtained for these named works (the arXiv search returned no results; HF search surfaced AgentBench only). Evidence dates for API-Bank, AgentDojo, and the survey are marked unknown where retrieved primary text lacked a publication date; ToolEmu/AgentDojo evaluator validity and real-environment generalizability remain bounded by their reported validation designs.

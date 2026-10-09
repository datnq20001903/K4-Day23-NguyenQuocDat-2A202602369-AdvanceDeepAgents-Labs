# What do primary sources establish about AgentBench, BFCL, ToolLLM, StableToolBench, and the scope and limits of tool-agent evaluation?

```json
[
  {
    "id": "2308.03688",
    "url": "https://arxiv.org/abs/2308.03688",
    "title": "AgentBench: Evaluating LLMs as Agents",
    "date": "unknown",
    "source": "web",
    "claims": [
      "AgentBench evaluates LLMs in eight distinct interactive environments and reports tests of 29 API-based and open-source models.",
      "The paper identifies weak long-term reasoning, decision-making, and instruction following as obstacles to usable agents.",
      "Its reported model performance gap concerns top commercial models versus many open-source competitors no larger than 70B in the tested study; it should not be generalized to contemporary models without new tests."
    ],
    "evidence": [
      "a multi-dimensional benchmark that consists of 8 distinct environments",
      "Our extensive test over 29 API-based and open-sourced (OSS) LLMs",
      "poor long-term reasoning, decision-making, and instruction following abilities are the main obstacles"
    ],
    "limitations": [
      "This fetched evidence is the abstract, not detailed protocol or failure-category analysis.",
      "The benchmark's eight environments and historical tested models bound what its results demonstrate; it does not establish reliability across arbitrary deployed tools."
    ]
  },
  {
    "id": "patil25a",
    "url": "https://proceedings.mlr.press/v267/patil25a.html",
    "title": "The Berkeley Function Calling Leaderboard (BFCL): From Tool Use to Agentic Evaluation of Large Language Models",
    "date": "2025-07-13",
    "source": "web",
    "claims": [
      "BFCL assesses serial and parallel function calls across programming languages using AST evaluation and includes expert-curated and user-contributed functions and prompts.",
      "The benchmark extends beyond single-turn calls to abstention and stateful multi-step agentic scenarios.",
      "The abstract reports memory, dynamic decision-making, and long-horizon reasoning as open challenges, but does not establish detailed AST-versus-execution validation."
    ],
    "evidence": [
      "evaluates serial and parallel function calls, across various programming languages using a novel Abstract Syntax Tree (AST) evaluation method",
      "combination of expert curated, and user-contributed functions and associated prompts",
      "evaluates the ability of models to abstain and reason in stateful multi-step agentic setting",
      "memory, dynamic decision-making, and long-horizon reasoning remain open challenges"
    ],
    "limitations": [
      "Retrieved proceedings text is abstract-level evidence; it does not substantiate the specific claim that AST matching correlates strongly with execution on a subset.",
      "AST evaluation as described here does not itself prove downstream tool outcomes, semantic correctness in all settings, or deployment safety.",
      "The abstract's statement that BFCL became the de facto standard is an author claim, not independent adoption evidence."
    ]
  },
  {
    "id": "2307.16789",
    "url": "https://arxiv.org/abs/2307.16789",
    "title": "ToolLLM: Facilitating Large Language Models to Master 16000+ Real-world APIs",
    "date": "unknown",
    "source": "web",
    "claims": [
      "ToolBench comprises 16,464 RapidAPI REST APIs in 49 categories; the authors say ChatGPT generated diverse single- and multi-tool instructions and searched for solution paths.",
      "The authors introduce ToolEval as an automatic evaluator.",
      "The retrieved abstract supports the existence of ToolEval but not detailed operational definitions of pass rate and win rate, nor independent validation of evaluator accuracy."
    ],
    "evidence": [
      "we collect $16,464$ real-world RESTful APIs spanning $49$ categories from RapidAPI Hub",
      "we prompt ChatGPT to generate diverse instructions involving these APIs",
      "we use ChatGPT to search for a valid solution path (chain of API calls)",
      "we develop an automatic evaluator: ToolEval"
    ],
    "limitations": [
      "This fetched primary source text is abstract-level; pass/win definitions and protocol details are not verified here.",
      "ChatGPT is used for both data construction and solution-path annotation, so the reported experimental conclusions alone do not establish judge validity or transfer to arbitrary APIs."
    ]
  },
  {
    "id": "2403.07714",
    "url": "https://arxiv.org/abs/2403.07714",
    "title": "StableToolBench: Towards Stable Large-Scale Benchmarking on Tool Learning of Large Language Models",
    "date": "unknown",
    "source": "web",
    "claims": [
      "StableToolBench evolves from ToolBench and proposes a virtual API server combining caching and API simulators to mitigate API-status changes.",
      "It defines solvable pass and win rates and uses GPT-4 as automatic evaluator to address evaluation randomness.",
      "The reported stability results are author-reported; cached and simulated calls are a reproducibility strategy, not equivalent evidence to testing changing production APIs."
    ],
    "evidence": [
      "we introduce StableToolBench, a benchmark evolving from ToolBench",
      "The virtual API server contains a caching system and APIs simulators which are complementary to alleviate the change in API status",
      "the stable evaluation system designs solvable pass and win rates using GPT-4 as the automatic evaluator to eliminate the randomness during evaluation",
      "Experimental results demonstrate the stability of StableToolBench"
    ],
    "limitations": [
      "The abstract gives no detailed validation protocol for the stability result or simulator fidelity.",
      "The specific 55.6% ToolBench API-status fluctuation figure and claimed cost/version limitations were not independently verified from the returned abstract text; they should retain their ToolBench-specific scope if used from other retrieved passages.",
      "GPT-4 judging and API simulation introduce dependencies whose portability and correspondence to live services are not settled by the abstract."
    ]
  },
  {
    "id": "2507.21504",
    "url": "https://arxiv.org/html/2507.21504v1",
    "title": "Evaluation and Benchmarking of LLM Agents: A Survey",
    "date": "unknown",
    "source": "web",
    "claims": [
      "The survey organizes agent evaluation by objectives (including behavior, capabilities, reliability, safety) and process (including interaction mode, datasets and benchmarks, metric computation, and tooling).",
      "It identifies realistic, holistic, scalable evaluation and enterprise needs such as reliability guarantees, dynamic and long-horizon interactions, access controls, and compliance as important challenges.",
      "The survey taxonomy describes a fragmented field rather than validating one universal metric or benchmark."
    ],
    "evidence": [
      "a two-dimensional taxonomy that organizes existing work along (1) evaluation objectives—what to evaluate, such as agent behavior, capabilities, reliability, and safety—and (2) evaluation process—how to evaluate",
      "including interaction modes, datasets and benchmarks, metric computation methods, and tooling",
      "dynamic and long-horizon interactions",
      "holistic, more realistic, and scalable evaluation"
    ],
    "limitations": [
      "This is a survey, not a new controlled benchmark experiment.",
      "The retrieved text supports broad taxonomy and challenges but not a single standardized protocol or fine-grained tool-call metric decomposition."
    ]
  }
]
```

Synthesis: AgentBench provides multi-environment interactive evaluation; BFCL focuses on structured function calling and adds abstention/stateful tasks; ToolLLM and StableToolBench address large API collections, with ToolEval judging and cache/simulator-based stabilization respectively. These are different evaluation scopes, and their scores should not be treated as directly comparable.

Gaps: Retrieved evidence does not verify ToolEval's pass/win definitions, BFCL's AST-versus-execution correlation, or StableToolBench's detailed 55.6% measurement and simulator fidelity. More broadly, abstract-level claims do not settle judge calibration, live-service realism, semantic/tool-outcome correctness, or long-horizon reliability and safety in deployments.
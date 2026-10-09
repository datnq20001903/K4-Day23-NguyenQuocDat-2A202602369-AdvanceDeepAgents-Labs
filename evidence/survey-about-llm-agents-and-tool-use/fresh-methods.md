# Audit question: How should the draft qualify quantitative and method claims about Toolformer, alpha-UMi, CodeAct, AgentOptimizer, and Tool-to-Agent Retrieval?

```json
[
  {
    "id": "d842425e4bf79ba039352da0f658a906",
    "url": "https://papers.nips.cc/paper_files/paper/2023/file/d842425e4bf79ba039352da0f658a906-Paper-Conference.pdf",
    "title": "Toolformer: Language Models Can Teach Themselves to Use Tools",
    "date": "unknown",
    "source": "web",
    "claims": [
      "Toolformer generates candidate API calls and applies a self-supervised future-token prediction criterion to decide which calls to retain before fine-tuning on those calls.",
      "The paper reports calculator-enabled scores of 40.4, 29.4, and 44.0 on ASDiv, SVAMP, and MAWPS, compared with 14.8, 6.3, and 15.0 with tool calls disabled.",
      "The reported 97.9% rate describes calculator calls over examples in the paper's three math benchmarks, not overall Toolformer tool-use frequency.",
      "The math evaluation uses a lenient first-predicted-number criterion (with a special equation rule), so the gains are tied to that scoring protocol and benchmark setup."
    ],
    "evidence": [
      "We then use a self-supervised loss to determine which of these API calls actually help the model in predicting future tokens. Finally, we finetune the LM itself on the API calls that it considers useful.",
      "Toolformer (disabled) | 14.8 | 06.3 | 15.0 |\n| Toolformer | 40.4 | 29.4 | 44.0",
      "for 97.9% of all examples the model decides to ask the calculator tool for help.",
      "we simply check for the first number predicted by the model."
    ],
    "limitations": [
      "The cited table and calculator-use rate concern these math benchmarks; they do not establish universal tool-use or end-to-end agent improvements.",
      "The scoring rule is not strict exact task completion and should be stated when characterizing the scores.",
      "Exact publication day not established by the retrieved PDF text; date recorded as unknown."
    ]
  },
  {
    "id": "2401.07324",
    "url": "https://huggingface.co/papers/2401.07324",
    "title": "Small LLMs Are Weak Tool Learners: A Multi-LLM Agent",
    "date": "2024-01-14",
    "source": "hf-search",
    "claims": [
      "alpha-UMi decomposes tool learning into planner, caller, and summarizer roles and trains a shared backbone on the entire dataset before role-specific continued fine-tuning.",
      "The primary-paper ToolBench excerpt reports, for the 7B setting with instruction reuse, Plan ACC 88.92 and Action EM 58.94; its Single-LLM comparison reports 81.92 and 53.26, respectively.",
      "These figures are reference/action matching metrics in an evaluation described as avoiding real-time API calls, not live-execution task success."
    ],
    "evidence": [
      "decomposes the aforementioned capabilities into a planner, caller, and summarizer",
      "First, we fine-tune a backbone LLM on the entire dataset without discriminating sub-tasks",
      "α-UMi w/ reuse | 88.92 | 58.94",
      "Single-LLM | 81.92 | 53.26",
      "which avoids real-time API callings."
    ],
    "limitations": [
      "The HF record supplies abstract/method summary; exact numeric scores came from primary-paper text evidence retained in the seed verification note, not from this HF page itself.",
      "Do not interpret Plan ACC or Action EM as successful completion with live APIs; scores are specific to the stated ToolBench evaluation, model setting and training protocol.",
      "The retrieved proceedings evidence gives a date range rather than a confirmed individual publication day; the HF paper-card date is used here."
    ]
  },
  {
    "id": "2402.01030",
    "url": "https://arxiv.org/abs/2402.01030",
    "title": "Executable Code Actions Elicit Better LLM Agents",
    "date": "2024-06-07",
    "source": "arxiv",
    "claims": [
      "CodeAct uses executable Python code as a unified action representation, with an interpreter and multi-turn interaction that permits revising prior actions or producing actions after new observations.",
      "Its abstract reports analysis of 17 LLMs on API-Bank and a newly curated benchmark and says CodeAct achieved up to 20% higher success rate than widely used alternatives.",
      "The abstract describes CodeActInstruct as 7k multi-turn interactions and reports that combining it with existing data can improve agent-oriented tasks without compromising general capability."
    ],
    "evidence": [
      "Published: 2024-06-07",
      "use executable Python code to consolidate LLM agents’ actions into a unified action space (CodeAct).",
      "CodeAct can execute code actions and dynamically revise prior actions or emit new actions upon new observations through multi-turn interactions.",
      "analysis of 17 LLMs on API-Bank and a newly curated benchmark shows that CodeAct outperforms widely used alternatives (up to 20% higher success rate).",
      "CodeActInstruct that consists of 7k multi-turn interactions"
    ],
    "limitations": [
      "The quantified up-to-20% result is abstract-level evidence here; the excerpt does not establish which benchmark, comparison, or whether the percentage is relative or percentage points. Avoid presenting it as a uniform gain.",
      "Abstract-level evidence does not verify per-benchmark numbers, safety properties, or broad generalization; qualitative claims about self-debugging and capability preservation should not be expanded beyond the abstract wording.",
      "ArXiv page says Published 2024-06-07; a seed note's arXiv search metadata showed 2024-02-01, so this note uses the directly fetched page date and flags the discrepancy rather than conflating submission and publication dates."
    ]
  },
  {
    "id": "2402.11359",
    "url": "https://arxiv.org/abs/2402.11359",
    "title": "Offline Training of Language Model Agents with Functions as Learnable Weights",
    "date": "unknown",
    "source": "hf-search",
    "claims": [
      "AgentOptimizer trains agent functions from execution histories without modifying the base LLM weights, treating functions as learnable agent parameters.",
      "Its described algorithm uses roll-back and early-stop strategies; its abstract claims significant performance improvements in downstream tasks and says it studies learning curves and domain transferability.",
      "The available extracted evidence establishes the approach and qualitative scope, but supplies no task-level scores, baselines, or numerical transfer evidence for this audit."
    ],
    "evidence": [
      "we propose to progressively forge agent’s functions to better solve the downstream tasks instead of modifying the LLM weights.",
      "By treating the functions as learnable ‘agent parameters’",
      "two strategies, roll-back, and early-stop, to streamline the training process.",
      "With extensive experiments, we showcase that the agent training paradigm could significantly improve the performance of representative LLM agents in various downstream tasks.",
      "We also study the behavior of the agent training regarding aspects like the learning curve and domain transferability."
    ],
    "limitations": [
      "Although the arXiv primary page was fetched, the available text excerpt did not include results tables or numbers; no quantitative effect size or specific transfer outcome is verified here.",
      "The abstract's improvement assertion is not evidence of universal superiority, nor of outperforming weight fine-tuning in a controlled comparison.",
      "Discovery label hf-search retained from the seed notes; arXiv ID-derived date is not substituted for retrieved publication date."
    ]
  },
  {
    "id": "2511.01854",
    "url": "https://huggingface.co/papers/2511.01854",
    "title": "Tool-to-Agent Retrieval: Bridging Tools and Agents for Scalable LLM Multi-Agent Systems",
    "date": "2025-11-03",
    "source": "hf-search",
    "claims": [
      "Tool-to-Agent Retrieval embeds both tools and parent agents in a shared vector space, with metadata relationships enabling tool-level or agent-level retrieval.",
      "The HF abstract reports 19.4% improvement in Recall@5 and 17.7% in nDCG@5 over prior agent retrievers on LiveMCPBench, averaged across eight embedding models.",
      "The abstract identifies these as retrieval ranking metrics; it does not report end-task completion improvement in the quoted result.",
      "The metric-label association follows the HF/abstract wording, but seed notes report a conflicting internal passage with the labels reversed, so exact metric assignment remains unresolved pending table-level verification."
    ],
    "evidence": [
      "Published on Nov 3, 2025",
      "embeds both tools and their parent agents in a shared vector space and connects them through metadata relationships",
      "achieves consistent improvements of 19.4% in Recall@5 and 17.7% in nDCG@5 over previous state-of-the-art agent retrievers on the LiveMCPBench benchmark.",
      "Evaluating Tool-to-Agent Retrieval across eight embedding models"
    ],
    "limitations": [
      "The page gives abstract-level claims; exact table context, absolute-versus-relative percentage interpretation, significance, and the conflicting metric assignment were not resolved in retrieved evidence.",
      "Recall and nDCG are retrieval metrics and do not establish improved task execution, success, cost, or robustness.",
      "Do not resolve the label discrepancy by inference; retain the abstract ordering only as the abstract's attribution, explicitly marked uncertain."
    ]
  }
]
```

Synthesis: Toolformer has directly retrieved primary-paper score evidence, but the 40.4/29.4/44.0 versus 14.8/6.3/15.0 comparison and 97.9% calculator-use rate are specific to three math benchmarks and a lenient first-number scoring rule. alpha-UMi separates planner/caller/summarizer and its cited 7B ToolBench scores should be described as reference/action metrics, not live execution success. CodeAct's up-to-20% success-rate claim and 7k data size are abstract-supported here; the 20% comparison/protocol and relative-versus-point meaning remain unspecified in retrieved text. AgentOptimizer is a function-update method; numerical strength and transfer claims are unverified in available extracts. Tool-to-Agent Retrieval is a joint tool/agent embedding-and-metadata method; the abstract's metric labels conflict with an internal passage reported by seed verification, and retrieval improvement is not task-success evidence.

Gaps: Before publishing precise CodeAct comparisons, inspect its task tables and percentage definition; retrieve AgentOptimizer's quantitative tables and transfer setup; inspect Tool-to-Agent Retrieval metric definitions and tables to settle Recall@5/nDCG@5 attribution and percent semantics. Avoid size attribution not explicitly established in these sources. These studies use non-comparable benchmarks and metrics, and the available evidence does not support a cross-method ranking or general claim of improved real-world agent success.
# Architectures and foundations: verifying ReAct, Toolformer, and CodeAct against their own sources

```json
[
  {
    "id": "2210.03629",
    "url": "https://arxiv.org/abs/2210.03629",
    "title": "ReAct: Synergizing Reasoning and Acting in Language Models",
    "date": "2023-03-10",
    "source": "web",
    "claims": [
      "ReAct prompts language models to generate verbal reasoning traces and task-specific actions in an interleaved manner; reasoning maintains and revises plans, while actions gather information from external sources or environments.",
      "The paper evaluates the approach on HotpotQA, Fever, ALFWorld, and WebShop, reporting an absolute success-rate advantage of 34% and 10% over imitation and reinforcement learning methods on ALFWorld and WebShop, respectively.",
      "The authors describe the empirical findings as specific to a range of language reasoning and decision-making tasks, not as a universal agent architecture result."
    ],
    "evidence": [
      "generate both reasoning traces and task-specific actions in an interleaved manner",
      "actions allow it to interface with and gather additional information from external sources such as knowledge bases or environments",
      "outperforms imitation and reinforcement learning methods by an absolute success rate of 34% and 10% respectively"
    ],
    "limitations": [
      "Abstract-level evidence does not detail prompt configurations or all baseline/task conditions; the reported benchmark results should not be generalized beyond those settings.",
      "The paper notes in its introduction that its main experiments use PaLM, which was not openly accessible at publication; reproducibility is supported with prompts and supplementary GPT-3 experiments."
    ]
  },
  {
    "id": "2302.04761",
    "url": "https://arxiv.org/abs/2302.04761",
    "title": "Toolformer: Language Models Can Teach Themselves to Use Tools",
    "date": "2023-02-09",
    "source": "arxiv",
    "claims": [
      "Toolformer is a training method: it teaches a language model to choose whether and how to call APIs and integrate outputs into next-token prediction, using self-supervised data generation and only a small number of API demonstrations.",
      "The authors evaluate zero-shot downstream performance with tools including QA, search, calculator, translation, and calendar, and also check whether core language modeling ability is retained.",
      "The paper explicitly identifies lack of tool chaining and interactive tool use, sensitivity to input wording, sample inefficiency, and failure to account for API computational cost as limitations."
    ],
    "evidence": [
      "trained to decide which APIs to call, when to call them, what arguments to pass, and how to best incorporate the results into future token prediction",
      "This is done in a self-supervised way, requiring nothing more than a handful of demonstrations for each API.",
      "inability of Toolformer to use tools in a chain",
      "does not allow the LM to use a tool in an interactive way"
    ],
    "limitations": [
      "The abstract establishes broad zero-shot gains but does not provide per-benchmark values; those should be taken from the full paper tables rather than inferred from the abstract.",
      "Its own stated limitations mean it is not evidence for multi-step interactive tool-agent competence."
    ]
  },
  {
    "id": "2402.01030",
    "url": "https://huggingface.co/papers/2402.01030",
    "title": "Executable Code Actions Elicit Better LLM Agents",
    "date": "2024-02-01",
    "source": "hf-search",
    "claims": [
      "CodeAct uses executable Python as a unified action space, with a Python interpreter, allowing code execution, dynamic revision of prior actions, and further actions after observations.",
      "The paper abstract reports evaluation of 17 LLMs on API-Bank and a newly curated benchmark, claiming up to 20% higher success rate than widely used alternatives.",
      "The authors introduce CodeActInstruct, reported as 7,000 multi-turn interactions, and describe CodeActAgent variants fine-tuned from Llama2 and Mistral."
    ],
    "evidence": [
      "use executable Python code to consolidate LLM agents’ actions into a unified action space (CodeAct)",
      "dynamically revise prior actions or emit new actions upon new observations through multi-turn interactions",
      "analysis of 17 LLMs on API-Bank and a newly curated benchmark",
      "up to 20% higher success rate"
    ],
    "limitations": [
      "This discovery record is an abstract summary; it does not establish the specific benchmark protocol, comparison baseline, or exact conditions behind the maximum gain.",
      "Executable code actions presuppose an interpreter and available libraries/tools; the abstract does not establish safety properties of code execution."
    ]
  },
  {
    "id": "2402.01030",
    "url": "https://arxiv.org/abs/2402.01030",
    "title": "Executable Code Actions Elicit Better LLM Agents",
    "date": "2024-06-07",
    "source": "arxiv",
    "claims": [
      "The primary paper characterizes typical JSON/text action schemas as constrained in action scope and composition, then proposes executable Python actions with interpreter-backed multi-turn feedback.",
      "The abstract reports comparison across 17 LLMs and up to 20% higher success rate; it also reports an instruction-tuning set of 7k multi-turn trajectories.",
      "The paper identifies the proposal as an action representation and interaction framework, rather than only a learned API-call insertion method."
    ],
    "evidence": [
      "limited by constrained action space (e.g., the scope of pre-defined tools) and restricted flexibility (e.g., inability to compose multiple tools)",
      "Integrated with a Python interpreter, CodeAct can execute code actions",
      "dynamically revise prior actions or emit new actions upon new observations through multi-turn interactions"
    ],
    "limitations": [
      "The abstract's 'up to 20%' is a maximum headline result, not a uniform improvement across models or tasks.",
      "The abstract does not quantify runtime, security, or operational costs of executing generated code."
    ]
  },
  {
    "id": "https://proceedings.mlr.press/v235/wang24h.html",
    "url": "https://proceedings.mlr.press/v235/wang24h.html",
    "title": "Executable Code Actions Elicit Better LLM Agents",
    "date": "2024-07-08",
    "source": "web",
    "claims": [
      "The PMLR proceedings record identifies this as a paper in ICML 2024 (Proceedings of Machine Learning Research, volume 235).",
      "The primary abstract reports CodeAct's Python execution and multi-turn action revision, and says its broad analysis compares 17 LLMs on API-Bank and a new benchmark.",
      "The primary paper reports CodeActInstruct comprises 7k multi-turn interactions; this record is useful for verifying the formal published version and bibliographic details."
    ],
    "evidence": [
      "Proceedings of the 41st International Conference on Machine Learning",
      "Integrated with a Python interpreter, CodeAct can execute code actions and dynamically revise prior actions",
      "CodeActInstruct that consists of 7k multi-turn interactions"
    ],
    "limitations": [
      "The proceedings landing-page abstract is not a substitute for detailed tables and full experimental methods.",
      "The reported improvements are authors' benchmark findings and do not alone establish performance in arbitrary tool ecosystems or safe execution."
    ]
  }
]
```

Synthesis: ReAct is primarily a prompting/control-loop paradigm that interleaves reasoning, environment actions, and observations; Toolformer instead trains API-call behavior into next-token prediction via self-supervised filtering, but explicitly lacks chained and interactive calls. CodeAct broadens the action representation to executable Python and multi-turn revision, emphasizing composition and control/data flow; its reported benchmark gains are conditional and do not establish execution safety.

Gaps: This evidence set verifies the three approaches against primary abstracts and official publication records, but detailed ReAct/Toolformer table-level comparisons and CodeAct operational safety/runtime costs remain unverified here. The three papers use different models, tasks, and evaluation protocols, so headline success figures are not directly comparable.

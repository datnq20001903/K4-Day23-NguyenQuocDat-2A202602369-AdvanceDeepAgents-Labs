# Targeted source-family coverage: foundational and recent LLM tool-use agents

```json
[
  {
    "id": "2210.03629",
    "url": "https://arxiv.org/abs/2210.03629",
    "title": "ReAct: Synergizing Reasoning and Acting in Language Models",
    "date": "2023-03-10",
    "source": "arxiv",
    "claims": [
      "ReAct interleaves language-model reasoning traces and task-specific actions, where reasoning helps track and update plans and actions gather information from external knowledge bases or environments.",
      "The paper evaluates on HotpotQA, Fever, ALFWorld, and WebShop; on HotpotQA and Fever it uses an interactive Wikipedia API.",
      "The abstract reports absolute success-rate improvements of 34% on ALFWorld and 10% on WebShop over imitation/reinforcement learning methods with one or two in-context examples.",
      "The paper identifies limitations of prompting, including limited support for reasoning and acting behaviors and demonstration requirements that can exceed the context window for complex tasks."
    ],
    "evidence": [
      "we explore the use of LLMs to generate both reasoning traces and task-specific actions in an interleaved manner",
      "actions allow it to interface with and gather additional information from external sources such as knowledge bases or environments",
      "We conduct empirical evaluations ... on four diverse benchmarks: question answering (HotPotQA ...), fact verification (Fever ...), text-based game (ALFWorld ...), and webpage navigation (WebShop ...).",
      "ReAct outperforms imitation and reinforcement learning methods by an absolute success rate of 34% and 10% respectively",
      "complex tasks with large action spaces require more demonstrations to learn well, which unfortunately can easily go beyond the input length limit of in-context learning"
    ],
    "limitations": [
      "The reported benchmark improvements are tied to the paper's specific few-shot prompting setups and benchmark tasks; they do not establish general real-world tool-use reliability.",
      "The authors explicitly note context-window and prompting-support limitations; the abstract reports interpretability benefits but does not establish that reasoning traces are always faithful explanations."
    ]
  },
  {
    "id": "2610.11514",
    "url": "https://arxiv.org/abs/2610.11514",
    "title": "SSCBench: Evaluating the Evidential Validity of Fault-Injection Tests for Tool-Using LLM Agents",
    "date": "2026-10-08",
    "source": "arxiv",
    "claims": [
      "SSCBench studies whether fault-adoption measurements validly support claims about tool-using-agent reliability when agents control which observations become visible.",
      "Its protocol checks what observations can refute an injected assertion, whether they become visible before the affected fact is first used, and whether that condition occurs in the evaluated execution.",
      "The study evaluates four fault operators and five agent configurations over 1,191 faulted executions in two tau-bench environments.",
      "Among 44 adopted runs where counterevidence eventually appeared, 17 saw it before first use and 27 only afterward; the paper cautions that aggregate adoption alone does not establish exposure to timely counterevidence."
    ],
    "evidence": [
      "the agent itself determines which authoritative observations become visible during execution",
      "specifies what observations can refute an injected assertion, determines whether they can become visible before the affected fact is first used, and records whether the evaluated execution actually realizes this condition",
      "evaluate four fault operators and five agent configurations over 1,191 faulted executions in two τ-bench environments",
      "among 44 adopted runs in which counterevidence eventually became visible, only 17 received it before first use, while 27 received it afterward",
      "The evidential condition realized by an execution and the population supporting a claim-specific interpretation are part of fault-injection evaluation itself"
    ],
    "limitations": [
      "The evidence is scoped to the reported fault operators, agent configurations, and two tau-bench environments; it does not directly quantify reliability across other tools or deployments.",
      "The returned source text is the abstract and beginning of the introduction; detailed protocol and experiment particulars beyond those excerpts were not independently examined here."
    ]
  },
  {
    "id": "2610.12419",
    "url": "https://huggingface.co/papers/2610.12419",
    "title": "OneSearch-VL: Unified Multimodal Deep Research Agent for Image and Video",
    "date": "2026-10-07",
    "source": "hf-daily",
    "claims": [
      "OneSearch-VL represents dependencies between visual anchors, entity relations, sourced facts, and answer-producing operations with a Visually Grounded Evidence Graph (VGEG).",
      "The work uses VGEG to construct and verify questions, filter expert trajectories, supervise SFT/RL, and organize operation-level benchmarks.",
      "The abstract reports a 20.2 and 17.6 percentage-point improvement for OneSearch-VL-8B over Qwen3-VL-8B with tool access on the new multi-image and video benchmarks, respectively."
    ],
    "evidence": [
      "A key challenge is to preserve the dependencies linking localized visual anchors, entity relations, source-supported facts, and answer-producing operations.",
      "introduce OneSearch-VL, a unified agent centered on the Visually Grounded Evidence Graph (VGEG)",
      "constructs and verifies multi-image and video questions and filters expert trajectories",
      "assemble OneSearch-VL-SFT-110K and OneSearch-VL-RL-10K for SFT and RL",
      "improves over Qwen3-VL-8B with tool access by 20.2 and 17.6 percentage points on the two new benchmarks, respectively"
    ],
    "limitations": [
      "This is multimodal image/video deep-research evidence and its benchmark gains do not imply equivalent performance for text-only agents or other tool-use settings.",
      "The returned page provides the abstract but not sufficient experimental detail to assess uncertainty, benchmark construction independently, or statistical significance."
    ]
  }
]
```

Synthesis: The arXiv-discovered ReAct paper provides foundational evidence for interleaved reasoning and external actions, plus few-shot interactive benchmark results; the newer arXiv SSCBench source shows that reliability evaluations must establish whether counterevidence was actually available before use.  
The independently discovered HF-daily OneSearch-VL record adds a multimodal learning/evaluation example that structures tool workflows around evidence dependencies; generalization beyond its new image/video benchmarks remains unproven by the returned abstract.
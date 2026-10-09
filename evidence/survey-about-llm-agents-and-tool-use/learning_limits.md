# What training/optimization methods improve tool-use agents, and what challenges remain in planning, execution, and reliable evaluation?

```json
[
  {
    "id": "2402.11359",
    "url": "https://arxiv.org/abs/2402.11359",
    "title": "Offline Training of Language Model Agents with Functions as Learnable Weights",
    "date": "unknown",
    "source": "web",
    "claims": [
      "This is the AgentOptimizer paper: it proposes training agents without modifying the underlying LLM weights, instead treating agent functions as trainable parameters.",
      "AgentOptimizer uses execution histories and performance signals to iteratively add, revise, or remove functions; rollback and early-stop are used to manage regressions and unproductive optimization.",
      "The paper reports improvement on representative downstream agent tasks and studies learning curves and domain transferability."
    ],
    "evidence": [
      "we propose to progressively forge agent’s functions to better solve the downstream tasks instead of modifying the LLM weights",
      "performing one of the predefined function manipulation actions (add, revise, and remove)",
      "The former is to withdraw the current function updates if the performance over the training set is degraded"
    ],
    "limitations": [
      "The retrieved abstract and primary text establish the method and broad reported effect, but do not provide detailed task-by-task numeric results here.",
      "The stated rollback and early-stop checks use training performance; the retrieved text does not establish that they prevent overfitting or guarantee transfer to deployment distributions."
    ]
  },
  {
    "id": "2402.01030",
    "url": "https://arxiv.org/abs/2402.01030",
    "title": "Executable Code Actions Elicit Better LLM Agents",
    "date": "unknown",
    "source": "web",
    "claims": [
      "This is the CodeAct paper: executable Python actions, paired with an interpreter and multi-turn observations, provide a composable action interface rather than only fixed text/JSON actions.",
      "CodeActInstruct contains 7k multi-turn interaction trajectories and is used for instruction tuning; the authors report agent-task improvements without compromising tested general capabilities.",
      "On the authors' 82-example M3ToolEval benchmark, CodeAct has higher task success for 12 of 17 evaluated LLMs and uses fewer average turns for 12 of 17; the best reported closed-source model scored 74.4% versus 13.4% for the best open-source model.",
      "CodeActAgent's results vary by backbone: the paper explicitly reports no improvement for its Llama-2 variant in the cited comparison."
    ],
    "evidence": [
      "use executable Python code to consolidate LLM agents’ actions into a unified action space (CodeAct)",
      "CodeActInstruct consisting of 7k high-quality multi-turn interaction trajectories",
      "CodeAct generally has a higher task success rate (12 out of 17 evaluated LLMs)",
      "the best open-source model achieving 13.4% while the best closed-source model gpt-4-1106-preview 74.4%",
      "Surprisingly, no improvement is observed for the Llama-2 variant."
    ],
    "limitations": [
      "M3ToolEval has 82 curated instances and deliberately tests zero-shot tool use, so its results do not establish broad real-world generalization.",
      "The paper's results show substantial model/backbone dependence and a large open/closed-source gap on M3ToolEval.",
      "The retrieved evidence describes interpreter-enabled execution but does not establish general safety or correctness of arbitrary generated code."
    ]
  },
  {
    "id": "2504.13958",
    "url": "https://arxiv.org/abs/2504.13958",
    "title": "ToolRL: Reward is All Tool Learning Needs",
    "date": "unknown",
    "source": "web",
    "claims": [
      "ToolRL studies reward design for tool selection and application and trains with Group Relative Policy Optimization (GRPO).",
      "The authors identify a reward-design difficulty: multi-step tool tasks involve varied tools and parameters, while answer-match-only rewards are too coarse for fine-grained learning feedback.",
      "The abstract reports a 17% improvement over base models and 15% over SFT models on the paper's diverse benchmarks.",
      "The paper reports testing tool-use generalization to unfamiliar programming languages and irrelevant-tool rejection not explicitly included in training; it also contrasts more stable GRPO outcomes with less stable cold-start PPO outcomes."
    ],
    "evidence": [
      "coarse-grained reward signals, such as answer matching, fail to offer the finegrained feedback required for effective learning",
      "apply them to train LLMs using Group Relative Policy Optimization (GRPO)",
      "achieving a 17% improvement over base models and a 15% gain over SFT models",
      "neither of which were explicitly included during RL training or in the dataset",
      "PPO with a cold start ... tends to be less stable"
    ],
    "limitations": [
      "The reported percentage improvements are as stated in the abstract; the retrieved evidence does not specify their aggregation or uncertainty intervals.",
      "Results are benchmark-based and do not establish reliable performance across arbitrary deployed tools or changing APIs.",
      "The paper itself frames reward design for multi-step, parameterized tool interactions as a challenge; broader reward validity remains unresolved by the retrieved evidence."
    ]
  },
  {
    "id": "2507.21504",
    "url": "https://arxiv.org/abs/2507.21504",
    "title": "Evaluation and Benchmarking of LLM Agents: A Survey",
    "date": "unknown",
    "source": "web",
    "claims": [
      "This is the requested evaluation-survey identity, published as a KDD '25 survey; it proposes a two-dimensional taxonomy of evaluation objectives and evaluation process.",
      "It treats capability evaluation as including tool use and planning, and reliability as consistency under repeated or perturbed inputs and behavior under system errors.",
      "The survey distinguishes static and interactive evaluation, diverse data/benchmarks, metric computation, tooling, and evaluation contexts.",
      "It argues for holistic, realistic, scalable evaluation and highlights enterprise needs including data access, reliability guarantees, dynamic long-horizon interactions, and compliance."
    ],
    "evidence": [
      "a two-dimensional taxonomy that organizes existing work along (1) evaluation objectives ... and (2) evaluation process",
      "Reliability assesses whether an agent behaves consistently for the same input and robustly when input varies or the system encounters errors.",
      "dynamic and long-horizon interactions, and compliance",
      "future research directions, including holistic, more realistic, and scalable evaluation"
    ],
    "limitations": [
      "This is a survey/taxonomy, not a controlled experiment demonstrating that a particular training method improves agents.",
      "Its discussion identifies evaluation dimensions and gaps but does not by itself establish that current benchmarks adequately measure reliability in deployment."
    ]
  },
  {
    "id": "2601.12294",
    "url": "https://arxiv.org/abs/2601.12294",
    "title": "ToolPRMBench: Evaluating and Advancing Process Reward Models for Tool-using Agents",
    "date": "unknown",
    "source": "web",
    "claims": [
      "ToolPRMBench evaluates process reward models at decision-step level using interaction history, a correct action, a plausible incorrect alternative, and tool metadata.",
      "Its construction combines offline sampling around gold trajectories and online sampling from full agent rollouts; candidate comparisons are filtered by multiple LLM judges, with human checks on mixed-vote cases.",
      "The authors identify long interactions and structured action spaces as sources of intermediate errors that may propagate, and argue that final-task success alone misses process-level quality.",
      "The paper reports ToolPRM-GRPO's 21.8% improvement in out-of-distribution evaluation, while noting that scaling/general capabilities are beneficial but not sufficient without specialized training."
    ],
    "evidence": [
      "Each sample ... consists of the interaction history, a correct action, an incorrect but plausible alternative, and associated tool metadata.",
      "combine offline sampling ... and online sampling, which captures realistic multi-step failures from full agent rollouts",
      "errors can emerge at many intermediate steps and propagate over time",
      "ToolPRM-GRPO achieves consistent gains in both ID and OOD evaluations, with a 21.8% improvement in the OOD setting",
      "increased model scale and stronger general capabilities are beneficial, but they are not sufficient without specialized training"
    ],
    "limitations": [
      "The 21.8% result is reported in the retrieved paper text, but the exact metric and experimental setting are not fully specified in the excerpt collected here.",
      "The benchmark concerns process reward models and does not prove that improved process-model scores necessarily yield reliable end-to-end deployed agents.",
      "Its multi-LLM label verification and partial human verification are safeguards, not evidence that labels are error-free."
    ]
  }
]
```

Synthesis: Training evidence spans non-parametric function-set optimization (AgentOptimizer), code-action trajectory SFT (CodeAct), and reward-shaped RL (ToolRL); each offers gains under its tested conditions, while backbone sensitivity, reward granularity, and distribution transfer remain concerns. Process-level reward modeling and evaluation taxonomies underscore that plans, tool choice/parameters, execution recovery, and end outcomes need separate scrutiny; current benchmark scale, cost, robustness, safety, and real-world long-horizon validity remain gaps.

Identity note: independently verified 2402.11359 as “Offline Training of Language Model Agents with Functions as Learnable Weights,” 2402.01030 as “Executable Code Actions Elicit Better LLM Agents,” and 2507.21504 as “Evaluation and Benchmarking of LLM Agents: A Survey.”
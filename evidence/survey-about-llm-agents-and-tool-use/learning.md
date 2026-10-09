# Learning/optimization for tool-using agents: AgentOptimizer, ToolRL, and complementary approaches

```json
[
  {
    "id": "2402.11359",
    "url": "https://arxiv.org/abs/2402.11359",
    "title": "Offline Training of Language Model Agents with Functions as Learnable Weights",
    "date": "unknown",
    "source": "web",
    "claims": [
      "AgentOptimizer trains agents without changing base LLM weights, instead treating agent functions as trainable parameters.",
      "It uses LLM-generated incremental add, revise, and remove operations informed by execution history and task performance; it does not use numeric gradient optimization over functions.",
      "Training evaluates on a task set, feeds execution histories and generated/ground-truth answers to the optimizer, and includes rollback on degraded performance and early stopping after consecutive non-improving updates.",
      "The abstract reports improvements on multiple downstream tasks and study of learning curves and domain transferability."
    ],
    "evidence": [
      "we present a novel paradigm of training LLM agents without modifying the LLM weights",
      "treating the functions as learnable ‘agent parameters’",
      "progressively update the current function set by performing one of the predefined function manipulation actions (add, revise, and remove)",
      "withdraw the current function updates if the performance over the training set is degraded",
      "early terminate the optimization process when a certain number of consecutive optimization steps do not introduce any performance boost"
    ],
    "limitations": [
      "The available page does not state the paper's original submission date; date therefore remains unknown here.",
      "Evidence retrieved gives no exact benchmark-level scores or sample sizes, and improvements are reported at abstract level.",
      "Optimization is based on training-set feedback; this excerpt does not establish broad out-of-distribution generalization or eliminate training-set overfitting."
    ]
  },
  {
    "id": "2504.13958",
    "url": "https://arxiv.org/abs/2504.13958",
    "title": "ToolRL: Reward is All Tool Learning Needs",
    "date": "2025-04-16",
    "source": "web",
    "claims": [
      "ToolRL studies reward design for tool-integrated reasoning, considering reward type, scale, granularity, and dynamics.",
      "Its principal training setup applies a structured reward within GRPO; reward includes format compliance and correctness of tool calls, with tool name and argument details informing correctness.",
      "The abstract reports gains of 17% over base models and 15% over SFT models across tool-use and QA benchmarks; it also reports tests of generalization to unfamiliar scenarios and objectives.",
      "The paper reports that longer reasoning traces are not inherently better, dynamic reward scaling can aid progression, and finer reward decomposition supports more stable learning."
    ],
    "evidence": [
      "systematically explore a wide range of reward strategies, analyzing their types, scales, granularity, and temporal dynamics",
      "achieving a 17% improvement over base models and a 15% gain over SFT models",
      "the overall reward R_final(·) is decomposed into two components: R_format + R_correct",
      "including tool names, parameter schemas, and parameter values",
      "Longer reasoning trace is not inherently better and length rewards can degrade performance."
    ],
    "limitations": [
      "The comparative gains are abstract-reported aggregate results; they do not alone establish which individual benchmark or baseline accounts for each gain.",
      "The reported generalization tests and reward findings are specific to the study's evaluated tasks and training setup; the excerpt does not establish transfer to arbitrary tools or deployment APIs.",
      "The paper also discusses PPO, but its reported strongest validation is with GRPO; performance should not be inferred to be uniform across RL algorithms."
    ]
  },
  {
    "id": "2503.09516",
    "url": "https://arxiv.org/abs/2503.09516",
    "title": "Search-R1: Training LLMs to Reason and Leverage Search Engines with Reinforcement Learning",
    "date": "unknown",
    "source": "web",
    "claims": [
      "Search-R1 trains an LLM to interleave reasoning with multi-turn search interactions, treating search as part of the environment.",
      "It combines PPO or GRPO with masking that excludes retrieved passage tokens from policy loss, while optimizing generated reasoning and tool-call tokens.",
      "It uses outcome-based reward and reports gains over RAG baselines on seven QA datasets: 24% for Qwen2.5-7B and 20% for Qwen2.5-3B under the same setting.",
      "The work is a specialized search-tool approach, rather than general-purpose tool selection and application."
    ],
    "evidence": [
      "learns to autonomously generate (multiple) search queries during step-by-step reasoning with real-time retrieval",
      "loss masking for retrieved tokens, ensuring the policy gradient objective is computed only over LLM-generated tokens",
      "Experiments on seven question-answering datasets show that Search-R1 improves performance by 24% (Qwen2.5-7B) and 20% (Qwen2.5-3B) over various RAG baselines",
      "future work could explore ... combining with diverse set of tools"
    ],
    "limitations": [
      "The search-result record did not provide an arXiv submission date; date is marked unknown.",
      "Evaluation centers on QA with search, and the paper itself identifies broader tool coverage as future work.",
      "Reported improvements compare against RAG baselines in a specified setting and do not establish gains on general-purpose function calling."
    ]
  },
  {
    "id": "2509.12867",
    "url": "https://huggingface.co/papers/2509.12867",
    "title": "Tool-R1: Sample-Efficient Reinforcement Learning for Agentic Tool Use",
    "date": "2025-09-16",
    "source": "hf-search",
    "claims": [
      "The HF search record describes Tool-R1 as an RL framework for complex multi-step tool use through executable Python code.",
      "The record characterizes the intended contribution as sample-efficient learning and reports improved accuracy and robustness on real-world tasks."
    ],
    "evidence": [
      "Tool-R1, a reinforcement learning framework",
      "complex, multi-step tool use through executable Python code",
      "improving accuracy and robustness on real-world tasks"
    ],
    "limitations": [
      "Evidence is limited to the HF paper-search record summary; the primary paper was not retrieved in this pass.",
      "No exact benchmark, numerical result, sample-efficiency measure, or limitations are provided in the returned summary."
    ]
  },
  {
    "id": "2508.18669",
    "url": "https://huggingface.co/papers/2508.18669",
    "title": "MUA-RL: Multi-turn User-interacting Agent Reinforcement Learning for agentic tool use",
    "date": "2025-08-26",
    "source": "hf-search",
    "claims": [
      "MUA-RL is described as RL for dynamic, multi-turn agent-tool interactions that incorporates LLM-simulated users.",
      "The record reports better performance than larger models in non-thinking settings."
    ],
    "evidence": [
      "integrating LLM-simulated users",
      "enhances agentic tool use in dynamic multi-turn interactions",
      "outperforming larger models in non-thinking settings"
    ],
    "limitations": [
      "Evidence is from an HF paper-search summary only; no primary paper text was retrieved.",
      "The summary does not specify datasets, comparator sizes, metrics, or the conditions behind the performance claim."
    ]
  }
]
```

Synthesis: AgentOptimizer optimizes the agent's external function set offline through LLM-authored edits and training-feedback safeguards, whereas ToolRL directly updates the model policy with RL and emphasizes decomposed, dynamic rewards for tool-call quality. Search-R1 illustrates a narrower online-RL setting with environment-interleaved retrieval and token masking; Tool-R1 and MUA-RL are complementary recent directions, but the available HF summaries are too thin for detailed method or quantitative comparisons.

Gaps: The AgentOptimizer date and exact task-wise effect sizes were not available in retrieved evidence; primary full text for Search-R1 was not fetched, and Tool-R1/MUA-RL evidence is summary-only. Comparisons across methods are not controlled head-to-head, and the retrieved sources do not settle robustness under noisy real-world APIs or transfer across broad, changing tool catalogs.

# Verification of foundational reward-objective claims for RL in LLM reasoning

```json
[
  {
    "id": "2203.02155",
    "url": "https://arxiv.org/abs/2203.02155",
    "title": "Training language models to follow instructions with human feedback",
    "date": "2022-03-04",
    "source": "web",
    "claims": [
      "InstructGPT's pipeline uses supervised fine-tuning on labeler demonstrations, then rankings/preferences over outputs and RLHF to further fine-tune the SFT model.",
      "The paper reports that InstructGPT outputs were preferred over GPT-3 in human evaluations on the authors' prompt distribution, while noting models still make simple mistakes.",
      "This is preference alignment based on human judgments, not a verifier for mathematical or factual correctness."
    ],
    "evidence": [
      "we collect a dataset of labeler demonstrations of the desired model behavior, which we use to fine-tune GPT-3 using supervised learning.",
      "We then collect a dataset of rankings of model outputs, which we use to further fine-tune this supervised model using reinforcement learning from human feedback.",
      "Even though InstructGPT still makes simple mistakes"
    ],
    "limitations": [
      "The abstract supports the stages and broad human-evaluation result, but not the detailed PPO/KL implementation claims in the seed note; those specifics were not re-verified in retrieved primary text here.",
      "Human preference is a proxy for desired behavior, and the reported evaluation is limited to the authors' prompt distribution."
    ]
  },
  {
    "id": "2305.18290",
    "url": "https://arxiv.org/abs/2305.18290",
    "title": "Direct Preference Optimization: Your Language Model is Secretly a Reward Model",
    "date": "2023-05-29",
    "source": "web",
    "claims": [
      "DPO derives an optimal policy in closed form under a parameterization of the reward model and optimizes using a classification loss, avoiding the standard separately fitted reward model followed by RL optimization procedure.",
      "The paper's stated method is preference alignment; its retrieved abstract reports sentiment control, summarization and single-turn dialogue experiments, not verifiable-reward reasoning evaluation.",
      "The method is described in the abstract as eliminating sampling from the LM during fine-tuning, but the abstract alone does not validate performance or equivalence outside its formulation and experiments."
    ],
    "evidence": [
      "enables extraction of the corresponding optimal policy in closed form",
      "solve the standard RLHF problem with only a simple classification loss",
      "eliminating the need for sampling from the LM during fine-tuning",
      "sentiment of generations ... response quality in summarization and single-turn dialogue"
    ],
    "limitations": [
      "The retrieved abstract does not spell out the preference-model assumptions or full derivation; the seed note's Bradley–Terry detail is retained as seed evidence but not independently verified from retrieved primary text in this check.",
      "DPO learns from preference labels and does not by itself provide an objective correctness checker."
    ]
  },
  {
    "id": "2501.12948",
    "url": "https://arxiv.org/abs/2501.12948",
    "title": "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning",
    "date": "2025-01-22",
    "source": "web",
    "claims": [
      "The v1 paper distinguishes R1-Zero, trained with large-scale RL without preliminary SFT, from R1, which uses cold-start data and a multi-stage training pipeline before RL.",
      "The paper attributes poor readability and language mixing to R1-Zero and presents R1 as addressing these issues.",
      "Seed evidence reports R1-Zero's reward as correctness of final predictions without constraints on reasoning-process content; this check confirms the broad RLVR contrast through the primary paper source, while the exact reward passage and detailed reward decomposition were not visible in the fetched excerpts.",
      "The paper is an author-reported system account; its reported results do not independently establish that reasoning traces are valid merely because final answers pass a checker."
    ],
    "evidence": [
      "DeepSeek-R1-Zero, a model trained via large-scale reinforcement learning (RL) without supervised fine-tuning (SFT) as a preliminary step",
      "poor readability, and language mixing",
      "DeepSeek-R1, which incorporates multi-stage training and cold-start data before RL"
    ],
    "limitations": [
      "The retrieved v1 HTML excerpt verified the abstract-level distinction, not every detailed claim about rule-based accuracy/format rewards or R1's later model-based feedback; consult the primary full text sections for those particulars.",
      "The R1-Zero reward checks final prediction correctness and does not certify intermediate reasoning validity, as stated in the seed evidence; checker coverage is task-dependent."
    ]
  },
  {
    "id": "2305.20050",
    "url": "https://arxiv.org/abs/2305.20050",
    "title": "Let's Verify Step by Step",
    "date": "2023-05-31",
    "source": "web",
    "claims": [
      "Outcome supervision provides feedback for a final result; process supervision provides feedback for each intermediate reasoning step.",
      "The paper reports that process supervision significantly outperformed outcome supervision on its MATH task study and that the process-supervised model solved 78% of a representative MATH test subset.",
      "The work compares reward-model supervision and reports releasing PRM800K, a set of 800,000 step-level human feedback labels; this does not demonstrate that process-reward RL universally outperforms outcome-reward RL."
    ],
    "evidence": [
      "outcome supervision, which provides feedback for a final result, or process supervision, which provides feedback for each intermediate reasoning step",
      "process supervision significantly outperforms outcome supervision for training models to solve problems from the challenging MATH dataset",
      "solves 78% of problems from a representative subset of the MATH test set",
      "800,000 step-level human feedback labels"
    ],
    "limitations": [
      "The result is specific to the studied MATH dataset and setup; it is not proof of cross-domain superiority.",
      "The paper frames process labels as human feedback and notes the high cost of human feedback; it does not establish process-label automation or direct superiority in modern RLVR policy optimization.",
      "The source abstract does not establish that a correct final answer guarantees sound intermediate steps."
    ]
  }
]
```

Synthesis: The seed's broad distinction is supported: InstructGPT and DPO optimize human preference proxies, while RLVR uses task-checkable outcomes; DPO replaces the conventional reward-model-plus-RL pipeline with a direct preference classification objective under its formulation. DeepSeek-R1-Zero is the unsupervised-before-RL contrast, whereas R1 adds cold-start data and multistage training to address readability and language mixing. Outcome supervision labels final results, whereas process supervision labels intermediate steps; the cited MATH result favors process supervision in its experiment, not universally.

Gaps: Retrieved primary text confirms the InstructGPT and DPO abstracts, but does not independently substantiate detailed PPO/KL and Bradley–Terry claims from the seed. R1's exact reward decomposition and later R1 stages were not fully visible in retrieved passages; those should be checked against the corresponding full-text sections before using fine-grained claims. These papers do not settle checker reliability, cross-domain transfer, or whether answer correctness implies valid reasoning.
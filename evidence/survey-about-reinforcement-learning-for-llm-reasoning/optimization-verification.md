# Verification: policy optimization, process rewards, and evaluation

```json
[
  {
    "id": "2402.03300",
    "url": "https://arxiv.org/abs/2402.03300",
    "title": "DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models",
    "date": "2024-04-27",
    "source": "web",
    "claims": [
      "GRPO avoids a separate critic/value model and uses the average reward of multiple sampled outputs for the same question as its baseline.",
      "The paper describes a clipped policy-ratio objective with group-relative advantages and a KL penalty to a reference policy.",
      "For DeepSeekMath-Instruct 7B to DeepSeekMath-RL 7B, the paper reports GSM8K 82.9% to 88.2%, MATH 46.8% to 51.7%, MGSM-zh 73.2% to 79.6%, and CMATH 84.6% to 88.8%.",
      "The comparison is a particular math-focused RL pipeline, not a controlled isolation of the optimization algorithm from all other system choices."
    ],
    "evidence": [
      "GRPO foregoes the critic model, instead estimating the baseline from group scores",
      "uses the average reward of multiple sampled outputs, produced in response to the same question, as the baseline",
      "GSM8K 82.9% 88.2% ... MATH 46.8% 51.7% ... CMATH 84.6% 88.8%",
      "GRPO is a variant reinforcement learning (RL) algorithm of Proximal Policy Optimization (PPO)"
    ],
    "limitations": [
      "Numerical results concern 7B models and mathematical benchmarks; they do not demonstrate general gains for open-ended reasoning.",
      "The reported before/after scores do not independently attribute all gains to GRPO rather than data, model, reward, or training-pipeline choices.",
      "The abstract's overall 51.7% MATH figure is not by itself the RL delta; the comparison table distinguishes DeepSeekMath-Instruct from DeepSeekMath-RL."
    ]
  },
  {
    "id": "2305.20050",
    "url": "https://arxiv.org/abs/2305.20050",
    "title": "Let’s Verify Step by Step",
    "date": "2023-05-31",
    "source": "web",
    "claims": [
      "The study compares outcome-supervised reward models, which receive feedback on final results, with process-supervised reward models, which receive feedback on intermediate reasoning steps.",
      "The process-supervised model solved 78% of a representative subset of the MATH test set; the paper reports best-of-1860 results of 78.2% for process supervision, 72.4% for outcome supervision, and 69.6% for majority voting.",
      "The work releases PRM800K, described as 800,000 step-level human feedback labels, and finds active learning improves process-supervision data efficiency.",
      "This is evidence about reward-model-based selection/search on MATH, not a direct demonstration that process-reward RL policy optimization outperforms outcome-reward RL."
    ],
    "evidence": [
      "process supervision, which provides feedback for each intermediate reasoning step",
      "Our process-supervised model solves 78% of problems from a representative subset of the MATH test set.",
      "% Solved (Best-of-1860) | 72.4 | 78.2 | 69.6",
      "the complete dataset of 800,000 step-level human feedback labels"
    ],
    "limitations": [
      "The evaluated outcome is best-of-N solution selection on a representative MATH subset; it is not a full benchmark-wide, single-sample policy result.",
      "The paper cautions that the large outcome- and process-supervision datasets are not directly comparable; human step labels are costly.",
      "MATH-domain results do not establish transfer of process-supervision advantages to other domains."
    ]
  },
  {
    "id": "2508.05170",
    "url": "https://huggingface.co/papers/2508.05170",
    "title": "Posterior-GRPO: Rewarding Reasoning Processes in Code Generation",
    "date": "2025-09-18",
    "source": "hf-search",
    "claims": [
      "Posterior-GRPO (P-GRPO) conditions process-based reasoning rewards on task success, applying those rewards only to successful outcomes to reduce reward hacking.",
      "The method uses an optimized-degraded preference-pair method to train a reasoning reward model and introduces LCB-RB for evaluation of reasoning-quality discrimination.",
      "The paper reports Qwen2.5-Coder-7B-Instruct improves from 50.4% to 57.4% average Pass@1 across LiveCodeBench, HumanEval(+), MBPP(+), and BigCodeBench, and reports a 4.5% average advantage over outcome-only rewards.",
      "For math, the retrieved primary-paper abstract says the approach is extended to math; the search-retrieved primary PDF text reports 7.3% relative improvement over outcome-only baselines for Qwen2.5-Math-7B."
    ],
    "evidence": [
      "By selectively applying rewards to the reasoning processes of only successful outcomes",
      "outperforming outcome-only baselines by 4.5%",
      "relative improvement of 13.9% over the base model (50.4% → 57.4%)",
      "Qwen2.5-Math-7B achieves a relative improvement of 7.3% over outcome-only reward baselines"
    ],
    "limitations": [
      "The HF page resolves to primary arXiv HTML and displays the paper's publication timestamp as 2025-09-18; available records are inconsistent about version/date, so this is the date shown by the retrieved HF record, not necessarily first preprint date.",
      "Reported code averages aggregate four benchmarks and rely on the paper's evaluation setup; excerpts do not establish independent replication or uncertainty intervals.",
      "The authors' claim that gating mitigates reward hacking is not proof that it eliminates it; process quality is still represented by a learned reward model.",
      "Math detail was available in search-retrieved primary-PDF text, not in the retrieved HF abstract itself."
    ]
  },
  {
    "id": "2502.18449",
    "url": "https://huggingface.co/papers/2502.18449",
    "title": "SWE-RL: Advancing LLM Reasoning via Reinforcement Learning on Open Software Evolution",
    "date": "2025-02-25",
    "source": "hf-search",
    "claims": [
      "SWE-RL trains on open-source software-evolution artifacts, including code snapshots, changes, issues, and pull requests, using a rule-based reward such as similarity between generated and oracle patches.",
      "The paper reports Llama3-SWE-RL-70B achieves a 41.0% solve rate on SWE-bench Verified using Agentless Mini.",
      "The paper reports gains on five out-of-domain task categories after RL on software-engineering data, while its SFT comparison baseline decreases on average.",
      "The reported evaluation supports a transfer claim within the authors' chosen task suite, not a general guarantee that software-evolution RL improves arbitrary reasoning."
    ],
    "evidence": [
      "a lightweight rule-based reward (e.g., the similarity score between ground-truth and LLM-generated solutions)",
      "achieves a 41.0% solve rate on SWE-bench Verified",
      "shows improved results on five out-of-domain tasks",
      "with Agentless Mini, our pipeline-based scaffold"
    ],
    "limitations": [
      "The 41.0% result is scaffold-dependent (Agentless Mini) and should not be interpreted as a model-only solve rate independent of the agent pipeline.",
      "Similarity to oracle patches is a proxy reward; it is not equivalent to demonstrating semantic correctness for every generated patch.",
      "The out-of-domain evidence is limited to the five task categories reported in the paper and its particular baselines/evaluation setup.",
      "The HF page and primary HTML record establish the 2025-02-25 date; later arXiv version metadata surfaced in search is inconsistent, so this note uses the supplied HF publication date."
    ]
  }
]
```

Synthesis: DeepSeekMath verifies GRPO’s group-mean baseline and reports sizable 7B math benchmark gains, but its full training setup prevents attributing every point to the optimizer alone. Process supervision’s strongest cited MATH result is best-of-1860 reward-model selection; Posterior-GRPO instead gates learned process reward on successful code outcomes, while SWE-RL applies rule-based patch rewards to software-evolution data and reports scaffolded SWE-bench performance plus limited OOD transfer.

Gaps: These sources do not provide a compute-matched, cross-domain comparison of outcome and process rewards under the same policy optimizer. More independent replications, uncertainty estimates, checker/reward robustness tests, and evaluations that separate model capability from sampling/scaffold effects are needed; final-task scores do not establish faithful intermediate reasoning.

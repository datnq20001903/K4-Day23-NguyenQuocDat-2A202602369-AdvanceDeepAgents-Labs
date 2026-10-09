# Question: Independently verify evaluation, trustworthiness, and decision-utility claims in the world-model report

```json
[
  {
    "id": "2502.20694",
    "url": "https://huggingface.co/papers/2502.20694",
    "title": "WorldModelBench: Judging Video Generation Models As World Models",
    "date": "unknown",
    "source": "hf-search",
    "claims": [
      "The abstract frames WorldModelBench as an application-driven video-world-model benchmark incorporating instruction-following and physics-adherence dimensions.",
      "The abstract reports 67K human labels measuring 14 frontier models, and a judger with 8.6% higher average accuracy than GPT-4o in predicting world-modeling violations.",
      "The comparator wording is 'GPT-4o with 2B parameters'; it does not establish that GPT-4o itself is a 2B-parameter model.",
      "These reported results concern judgments of generated videos; they do not establish closed-loop robot control utility or safety."
    ],
    "evidence": [
      "By incorporating instruction-following and physics-adherence dimensions",
      "We crowd-source 67K human labels to accurately measure 14 frontier models.",
      "achieving 8.6% higher avereage accuracy in predicting world modeling violations than GPT-4o with 2B parameters."
    ],
    "limitations": [
      "The retrieved page exposes abstract and introduction rather than the details needed to verify a 0.28 correlation or the report's other specific frame-quality/instruction-following numerical comparisons.",
      "The abstract does not specify whether the 8.6% is a relative percentage or percentage-point difference, nor enough protocol detail to assess generality.",
      "The retrieved text has no publication date; do not infer one from the identifier."
    ]
  },
  {
    "id": "25_WFM_Eval_Interpretable_Erro",
    "url": "https://videoworldmodel-workshop.github.io/accepted_papers/25_WFM_Eval_Interpretable_Erro.pdf",
    "title": "WFM-Eval: An Evaluation Framework for Video World Models in Robotic Manipulation",
    "date": "unknown",
    "source": "web",
    "claims": [
      "WFM-Eval decomposes video evaluation into task completion, object hallucination, and temporal consistency, with structured object-level diagnostics.",
      "Its abstract reports five models benchmarked on GR1 and AgiBot data and says rankings reverse across those datasets.",
      "It reports a LIBERO downstream-policy comparison where Predict2 outperforms Predict2.5 by 8.75 points; this is supporting evidence in the reported setting, not validation of a general predictive metric.",
      "The abstract says the best individual holistic judge, Kimi-K2.5, reaches 69.5% F1 and that judges have opposing biases that do not cancel under ensembling."
    ],
    "evidence": [
      "decomposes video quality into three axes (task completion, object hallucination, and temporal consistency) with structured object-level diagnostics",
      "We benchmark five video world models (Cosmos Predict2, Predict2.5, Veo 3.1, HunyuanVideo 1.5, Wan2.2) on GR1 and AgiBot.",
      "model rankings reverse between datasets",
      "Predict2 outperforms Predict2.5 by 8.75 points.",
      "even the best single judge Kimi-K2.5 [33] reaches only 69.5% F1"
    ],
    "limitations": [
      "The retrieved abstract does not define the exact point scale or supply uncertainty intervals or significance testing for the 8.75-point gap.",
      "The LIBERO result does not prove hallucination ranking generally predicts policy utility.",
      "The PDF says accepted at the 1st Workshop on Video World Models, CVPR 2026, but the retrieved text gives no exact publication date."
    ]
  },
  {
    "id": "2606.01600",
    "url": "https://huggingface.co/papers/2606.01600",
    "title": "RoboTrustBench: Benchmarking the Trustworthiness of Video World Models for Robotic Manipulation",
    "date": "unknown",
    "source": "hf-search",
    "claims": [
      "RoboTrustBench is described as containing 1,207 expert-validated instruction-image pairs from real-world DROID episodes, tested in Normal, Constraint-Sensitive, Counterfactual, and Adversarial scenarios.",
      "The abstract describes six evaluation dimensions, 13 fine-grained criteria, and assessment of seven representative video world models by human and MLLM assessment.",
      "The abstract reports that models often produce visually coherent video but struggle with constraint reasoning, counterfactual grounding, physical interaction, and unsafe-instruction suppression.",
      "This supports a bounded claim about shortcomings on the benchmark's tests, not real-robot incident rates, certification, or the safety of all world-model types."
    ],
    "evidence": [
      "Built from real-world DROID episodes, RoboTrustBench contains 1,207 expert-validated instruction-image pairs",
      "four scenarios: Normal, Constraint-Sensitive, Counterfactual, and Adversarial",
      "a six-dimensional evaluation protocol with 13 fine-grained criteria",
      "Evaluating seven representative video world models with human and MLLM assessment",
      "struggle with constraint reasoning, counterfactual grounding, physical interaction, and unsafe-instruction suppression."
    ],
    "limitations": [
      "The abstract gives no per-model numeric results or detailed scoring procedures, so it cannot support specific failure prevalence or model ranking claims.",
      "The hosting page says 'Published on Jun 1' but omits the year; use unknown rather than infer the date from the paper identifier.",
      "The benchmark evaluates instruction-conditioned video predictions and does not report physical-robot incident rates or formal safety certification."
    ]
  },
  {
    "id": "2606.15032v2",
    "url": "https://arxiv.org/html/2606.15032v2",
    "title": "How Should World Models Be Evaluated for Embodied Decision-Making? A Decision-Making-Centric Position",
    "date": "2026-06-28",
    "source": "web",
    "claims": [
      "The position paper surveys evaluation practice across several meanings of world models and identifies recurring claim/evidence mismatch.",
      "It argues that embodied-decision claims call for evaluating interventional reasoning, policy evaluation, planning, and optimization under interventions, policy-induced distribution shift, and long-horizon rollout, rather than relying on visual plausibility.",
      "It proposes an L0-L7 evidential ladder and foregrounds action fidelity, closed-loop rollout validity, reward/value prediction, policy-ranking agreement, optimization lift, exploitability, and uncertainty calibration.",
      "The text expressly describes the levels as an evidential hierarchy spanning orthogonal axes, not one scalar score."
    ],
    "evidence": [
      "a recurring problem of claim/evidence mismatch",
      "supports reliable interventional reasoning, policy evaluation, planning, and policy optimization under intervention, policy-induced distribution shift, and long-horizon rollout",
      "an L0–L7 ladder spanning visual plausibility to policy optimization utility",
      "the levels cut across several orthogonal axes and so form an evidential hierarchy rather than a single scalar",
      "interventional action fidelity, closed-loop rollout validity, reward/value prediction, policy-ranking agreement, optimization lift, model exploitability, and uncertainty calibration"
    ],
    "limitations": [
      "This is a survey/position and proposed framework, not an experiment validating each level or proving that it predicts deployment success.",
      "The abstract supports the broad objective-mismatch argument but does not independently establish every detailed causal-identification claim in the draft.",
      "The retrieved HTML states Published: 2026-06-28."
    ]
  },
  {
    "id": "2411.07690",
    "url": "https://arxiv.org/html/2411.07690",
    "title": "World Models: The Safety Perspective",
    "date": "unknown",
    "source": "web",
    "claims": [
      "The paper describes itself as a review and analysis of world-model impacts from trustworthiness and safety perspectives, rather than a controlled empirical benchmark.",
      "It says world models are intended to predict environmental evolution or fill in missing information to support planning and safe behavior, and frames safety as important for critical applications.",
      "The fetched text does not itself establish a universal readiness verdict or quantified failure rates."
    ],
    "evidence": [
      "we review and analyze the impacts of the current state-of-the-art in WM technology from the point of view of trustworthiness and safety",
      "A WM is intended to help the agent predict the future evolution of environmental states or help the agent fill in missing information so that it can plan its actions and behave safely.",
      "The safety property of WM plays a key role in their effective use in critical applications."
    ],
    "limitations": [
      "The retrieved excerpt provides no publication date; retain unknown.",
      "The excerpt does not verify particular gaming-versus-driving metrics or a categorical claim that world models are not ready for safety-critical deployment.",
      "As a review, it synthesizes research and does not supply new controlled comparisons or certification evidence."
    ]
  }
]
```

Synthesis: The independent retrieval confirms the report's bounded summaries of WorldModelBench, WFM-Eval, and RoboTrustBench, with an important wording safeguard: WorldModelBench says its judger outperforms “GPT-4o with 2B parameters,” not that GPT-4o has 2B parameters. WFM-Eval's dataset reversal and LIBERO gap are reported benchmark-specific findings, while RoboTrustBench's abstract supports qualitative failure categories but not prevalence or deployment risk.

Decision-centric evaluation is an argument and proposed evidential framework, not a validated ladder; the safety-perspective review likewise cannot support quantitative readiness claims from the retrieved excerpt. Metadata audit: WFM-Eval's exact date and WorldModelBench's date remain unreported; RoboTrustBench's page says only “Published on Jun 1,” so its year is unresolved; decision-centric HTML explicitly states 2026-06-28.
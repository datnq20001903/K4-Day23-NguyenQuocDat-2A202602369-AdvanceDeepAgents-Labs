# Research question 3 — Evaluation, deployment, and limitations of efficient inference and small language models

```json
[
  {
    "id": "2511.07885",
    "url": "https://huggingface.co/papers/2511.07885",
    "title": "Intelligence per Watt: Measuring Intelligence Efficiency of Local AI",
    "date": "2025-11-11",
    "source": "hf-search",
    "claims": [
      "The study profiles more than 20 local language models across eight accelerators and a representative subset of one million real-world single-turn chat and reasoning queries.",
      "The authors define intelligence per watt as task accuracy divided by unit power and report measuring accuracy, energy, latency, and power for each query.",
      "The paper-page summary reports local models accurately handling 88.7% of single-turn chat and reasoning queries; the displayed abstract states local query coverage improved from 23.2% in 2023 to 71.3% in 2025 and intelligence per watt improved 5.3x.",
      "The paper-page summary reports local accelerators achieving at least 1.4x lower intelligence-per-watt than cloud accelerators running identical models, suggesting local hardware has optimization headroom."
    ],
    "evidence": [
      "We conduct a large-scale empirical study across 20+ state-of-the-art local LMs, 8 accelerators, and a representative subset of LLM traffic: 1M real-world single-turn chat and reasoning queries.",
      "For each query, we measure accuracy, energy, latency, and power.",
      "local IPW improving 5.3x and local query coverage rose from 23.2% to 71.3%.",
      "Local accelerators achieve at least 1.4x lower IPW than cloud accelerators running identical models"
    ],
    "limitations": [
      "Evidence is from the HF paper page and an arXiv abstract/page rather than a verified full experimental section; clarify the meaning and denominator of ‘coverage’ before treating it as general task accuracy.",
      "The workload is described as single-turn chat and reasoning and should not be generalized to multi-turn, specialized, or safety-critical use without further testing.",
      "A power-normalized accuracy metric alone does not express absolute response latency, peak memory, or quality variation across domains."
    ]
  },
  {
    "id": "2025.acl-long.718",
    "url": "https://aclanthology.org/2025.acl-long.718/",
    "title": "Demystifying Small Language Models for Edge Deployment",
    "date": "2025-07-27",
    "source": "web",
    "claims": [
      "This ACL study examines more than 60 publicly accessible SLMs, including Phi and Gemma, for resource-constrained use cases.",
      "The abstract reports that state-of-the-art SLMs can outperform 7B models on general tasks, while in-context-learning capability remains limited.",
      "The authors identify efficiency opportunities including task-specific dynamic routing, model-hardware co-design, and vocabulary/KV-cache compression."
    ],
    "evidence": [
      "This work presents the first comprehensive study of over 60 SLMs such as Microsoft Phi and Google Gemma that are publicly accessible.",
      "state-of-the-art SLMs outperform 7B models in general tasks",
      "SLMs’ in-context learning capabilities remain limited, and their efficiency has significant optimization potential.",
      "dynamic task-specific routing, model-hardware co-design, and vocabulary/KV cache compression."
    ],
    "limitations": [
      "The retrieved abstract and bibliographic page do not establish individual per-device latency, throughput, energy, or memory figures.",
      "The abstract does not specify the tasks and comparison conditions behind the reported outperformance; it is not evidence that SLMs dominate larger models across domains.",
      "The paper's abstract-level claims do not evaluate safety or robustness comprehensively."
    ]
  },
  {
    "id": "2505.16508",
    "url": "https://arxiv.org/html/2505.16508",
    "title": "Edge-First Language Model Inference: Models, Metrics, and Tradeoffs",
    "date": "unknown",
    "source": "web",
    "claims": [
      "The study benchmarks SLM inference on Jetson AGX Orin, Jetson Nano Orin, and a smartphone, reporting token-generation speed, time-to-first-token, average power, and query energy.",
      "Some models cannot run on the Nano because of memory limits; the paper reports TTFT rising as model sizes approach platform memory capacity.",
      "The authors report that the AGX draws 1.7–3.91 times as much power as the Nano, while the Nano takes 1.49 times longer to generate a response, rising to 3.25 times for larger models such as 7B.",
      "A worked comparison presents quality, energy-derived cost, and TTFT together: GPT-4 is reported at 0.97 GSM8K quality and 0.71 s TTFT; Qwen-2.5:7B on AGX at 0.91 and 0.28 s; Qwen-2.5:3B on Nano at 0.80 and 0.33 s.",
      "The authors argue for cloud fallback when edge scalability or model capacity is insufficient, rather than a universal edge-only deployment."
    ],
    "evidence": [
      "A key performance metric in this context is token generation speed (TGS), time-to-first-token (TTFT), along with average power usage and energy consumption per query",
      "some models could not run on Jetson Nano due to memory limitations",
      "Jetson Agx consumes 1.7–3.91 times more power than the Nano; however, the Nano requires 1.49 times more time to generate a response.",
      "quality score Q, GPT-4 achieves 0.97 on GSM8K, compared to 0.91 for Qwen-2.5:7B and 0.80 for Qwen-2.5:3B. Responsiveness, measured as TTFT (R), is 0.71s for GPT-4, 0.28s for the Agx, and 0.33s for the Nano."
    ],
    "limitations": [
      "The numerical findings are from the paper's reported device/model setup and one example task; they should not be transferred to other hardware, workloads, or software stacks without replication.",
      "Quality values in the worked comparison are task-specific and do not imply comparable quality on other tasks.",
      "The retrieved text does not provide a complete account of measurement repetitions, uncertainty, thermal effects, or power-measurement instrumentation."
    ]
  },
  {
    "id": "2511.03506",
    "url": "https://huggingface.co/papers/2511.03506",
    "title": "HaluMem: Evaluating Hallucinations in Memory Systems of Agents",
    "date": "2025-11-05",
    "source": "hf-daily",
    "claims": [
      "HaluMem proposes operation-level assessment of hallucinations in memory extraction, memory updating, and memory question answering rather than relying only on end-to-end QA.",
      "The benchmark includes two multi-turn datasets, each described as containing about 15,000 memory points and 3,500 multi-type questions, with average conversations of 1,500 or 2,600 turns and contexts exceeding one million tokens.",
      "The benchmark summary reports that memory systems can introduce hallucinations during extraction and updating, with errors propagating into question answering."
    ],
    "evidence": [
      "HaluMem defines three evaluation tasks (memory extraction, memory updating, and memory question answering)",
      "Both include about 15k memory points and 3.5k multi-type questions.",
      "The average dialogue length per user reaches 1.5k and 2.6k turns, with context lengths exceeding 1M tokens",
      "existing memory systems tend to generate and accumulate hallucinations during the extraction and updating stages, which subsequently propagate errors to the question answering stage."
    ],
    "limitations": [
      "This benchmark addresses agent memory reliability, not general SLM safety or robustness, and the HF-daily result provides only a summary.",
      "The dataset scale and reported findings do not by themselves establish performance for on-device models or operational deployment settings.",
      "The associated arXiv page returned a date inconsistent with the HF record; the date here is the HF-daily published date, not independently verified from the primary full text."
    ]
  },
  {
    "id": "2511.07885",
    "url": "https://arxiv.org/abs/2511.07885",
    "title": "Intelligence per Watt:Measuring Intelligence Efficiency of Local AI",
    "date": "2026-09-06",
    "source": "web",
    "claims": [
      "The fetched arXiv page describes profiling local models of at most 20B active parameters, multiple hardware accelerators, and more than one million real-world queries.",
      "The paper motivates local deployment with device memory and compute sufficient to host some models at interactive latencies, while recognizing model capability as a task-dependent constraint.",
      "The abstract's reported coverage and IPW trends provide evidence of improvement over 2023–2025, but use a coverage/win-tie formulation that should not be conflated with absolute accuracy."
    ],
    "evidence": [
      "small models (≤20B active parameters)",
      "20+ state-of-the-art local LMs (≤20B active parameters), diverse hardware accelerators (Apple, NVIDIA, AMD), multiple performance metrics, and 1M+ real-world queries",
      "win/tie rate versus frontier models increases from 23.2% (2023) to 71.3% (2025)",
      "local accelerators ... have sufficient memory capacity and compute throughput to host these models with interactive latencies"
    ],
    "limitations": [
      "The retrieved arXiv page reports a publication date of 2026-09-06, while the HF paper record says published 2025-11-11; metadata conflict is unresolved and requires verification before citation.",
      "The available fetched text is not the complete methods/results section, so query sampling, scoring details, and uncertainty cannot be independently assessed here.",
      "The result compares local models and accelerators; it is not evidence that local execution is always lower-energy or lower-latency than cloud for every model and workload."
    ]
  }
]
```

Synthesis: Evidence spans large-scale local-model profiling, a 60+ model edge survey, and device-specific measurements: useful comparisons must jointly report quality, TTFT/token throughput, energy/power, and memory, rather than parameter count alone. Deployment trades device capacity and privacy/responsiveness against model capability and hardware constraints; task-specific routing or cloud fallback can be necessary, while benchmark scope (single-turn versus long-context, representative traffic, task-specific scores) and uneven measurement methods limit generalization.

Gaps: The retrieved sources provide little directly comparable safety testing, broad adversarial robustness measurement, or uncertainty reporting across hardware; the newest local-AI numerical claims have inconsistent dates and abstract/page-level evidence. HF-daily coverage is relevant to evaluation reliability but not specific to small/on-device models.
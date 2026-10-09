# Research question: Foundations and system-level inference efficiency for small language models and efficient LLM inference

```json
[
  {
    "id": "2309.06180",
    "url": "https://arxiv.org/abs/2309.06180",
    "title": "Efficient Memory Management for Large Language Model Serving with PagedAttention",
    "date": "2023-09-12",
    "source": "web",
    "claims": [
      "The paper identifies dynamic per-request KV-cache memory and inefficient fragmentation/duplication as constraints on batch size in high-throughput LLM serving.",
      "PagedAttention pages KV state into blocks and vLLM reports near-zero KV-cache waste, along with flexible cache sharing.",
      "The reported evaluation finds 2–4× throughput over FasterTransformer and Orca at the same latency, with larger gains for longer sequences, larger models, and complex decoding."
    ],
    "evidence": [
      "High throughput serving of large language models (LLMs) requires batching sufficiently many requests at a time.",
      "the key-value cache (KV cache) memory for each request is huge and grows and shrinks dynamically",
      "vLLM, an LLM serving system that achieves (1) near-zero waste in KV cache memory and (2) flexible sharing of KV cache within and across requests",
      "vLLM improves the throughput of popular LLMs by 2-4× with the same level of latency"
    ],
    "limitations": [
      "Reported throughput is tied to the paper's evaluated models, serving systems, workload mix, hardware, and latency operating point; it is not a universal multiplier.",
      "This evidence establishes cache management and serving throughput, not reduced model arithmetic or an improvement to single-request decoding latency."
    ]
  },
  {
    "id": "2211.17192",
    "url": "https://proceedings.mlr.press/v202/leviathan23a.html",
    "title": "Fast Inference from Transformers via Speculative Decoding",
    "date": "2023-07-03",
    "source": "web",
    "claims": [
      "Autoregressive generation requires serial target-model runs token by token; speculative decoding drafts candidate tokens with a smaller approximation model and verifies them in parallel with the target.",
      "The sampling method guarantees the target model's output distribution while enabling several tokens to be accepted per target-model pass.",
      "On T5-XXL, the paper reports 2–3× acceleration versus its standard T5X implementation without changing outputs."
    ],
    "evidence": [
      "decoding K tokens takes K serial runs of the model",
      "by running them in parallel on the outputs of the approximation models, potentially generating several tokens concurrently, and without changing the distribution",
      "We demonstrate it on T5-XXL and show a 2X-3X acceleration compared to the standard T5X implementation, with identical outputs."
    ],
    "limitations": [
      "The reported speedup is measured for the paper's T5-XXL setting and baseline; acceptance rate and draft-model overhead determine transfer to other models/workloads.",
      "The paper explicitly conditions its benefits on sufficient resources for added concurrency; the mechanism trades extra arithmetic for fewer serial target-model calls."
    ]
  },
  {
    "id": "2210.17323",
    "url": "https://arxiv.org/abs/2210.17323",
    "title": "GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers",
    "date": "unknown",
    "source": "web",
    "claims": [
      "GPTQ is a one-shot post-training weight-quantization method using approximate second-order information, intended to compress large generative Transformers to 3–4 bits with little reported accuracy degradation.",
      "The paper reports end-to-end speedups over FP16 of about 3.25× on A100 and 4.5× on A6000 in its evaluated setup, attributing them to bespoke kernels and reduced memory movement.",
      "The paper's OPT-175B example quantized to 3 bits occupies about 63 GB for model weights and uses about 9 GB for KV history at a 2048-token maximum, illustrating that weights and KV cache compete for device memory."
    ],
    "evidence": [
      "GPTQ can quantize GPT models with 175 billion parameters in approximately four GPU hours, reducing the bitwidth down to 3 or 4 bits per weight, with negligible accuracy degradation relative to the uncompressed baseline.",
      "end-to-end inference speedups over FP16, of around 3.25x when using high-end GPUs (NVIDIA A100) and 4.5x when using more cost-effective ones (NVIDIA A6000).",
      "quantized to 3 bits, this model takes approximately 63GB of memory",
      "storing the complete history of keys and values for all layers ... consumes another ≈9 GB for the maximum of 2048 tokens",
      "our method obtains speedups from reduced memory movement, and does not lead to computational reductions."
    ],
    "limitations": [
      "The paper notes that speedups depend on purpose-built kernels and reduced memory movement; quantization itself does not reduce the arithmetic computation.",
      "The numerical results concern particular OPT models, quantization settings, GPUs, and implementations; model quality/perplexity can degrade, especially at more aggressive bit widths.",
      "The arXiv page retrieved did not expose a publication date, so date is recorded as unknown rather than inferred from the identifier."
    ]
  },
  {
    "id": "Orca OSDI 2022",
    "url": "https://www.usenix.org/conference/osdi22/presentation/yu",
    "title": "Orca: A Distributed Serving System for Transformer-Based Generative Models",
    "date": "unknown",
    "source": "web",
    "claims": [
      "Because autoregressive requests advance one token per model iteration and finish at different times, request-level scheduling can retain completed requests in batches and make new requests wait.",
      "ORCA proposes iteration-level scheduling and selective batching to change batch membership at each model iteration.",
      "Its reported GPT-3 175B evaluation gives 36.9× throughput improvement over FasterTransformer at the same latency; the paper also describes batch-size tuning as a throughput/latency tradeoff under GPU-memory constraints."
    ],
    "evidence": [
      "each iteration of the model generates a single output token for the request",
      "iteration-level scheduling, a new scheduling mechanism that schedules execution at the granularity of iteration",
      "Our evaluation on a GPT-3 175B model shows that ORCA can significantly outperform NVIDIA FasterTransformer in terms of both latency and throughput: 36.9× throughput improvement at the same level of latency.",
      "Increasing the batch size trades off increased throughput for increased latency"
    ],
    "limitations": [
      "The 36.9× result is for the paper's GPT-3 175B comparison and baseline and cannot be assumed for current engines or arbitrary loads.",
      "The search result provided the official USENIX summary and paper text, but did not expose publication-date metadata; date is marked unknown."
    ]
  },
  {
    "id": "2308.16369",
    "url": "https://arxiv.org/abs/2308.16369",
    "title": "Sarathi: Efficient LLM Inference by Piggybacking Decodes with Chunked Prefills",
    "date": "unknown",
    "source": "web",
    "claims": [
      "Sarathi distinguishes compute-intensive prefill from low-utilization autoregressive decode, and uses chunked prefills plus decode-maximal mixed batches to improve utilization.",
      "The method aims to balance pipeline micro-batches and reduce bubbles by making their compute more uniform.",
      "The abstract reports up to 10× decode-throughput improvement and 1.33× end-to-end throughput for LLaMA-13B on A6000; for GPT-3 with pipeline parallelism it reports 6.29× fewer bubbles and 1.91× end-to-end throughput."
    ],
    "evidence": [
      "the prefill phase effectively saturates GPU compute at small batch sizes, the decode phase results in low compute utilization as it generates one token at a time per request",
      "Sarathi employs chunked-prefills, which splits a prefill request into equal sized chunks, and decode-maximal batching",
      "For the LLaMA-13B model on A6000 GPU, Sarathi improves decode throughput by up to 10 ×, and accelerates end-to-end throughput by up to 1.33 ×.",
      "Sarathi reduces bubbles by 6.29 ×, resulting in an end-to-end throughput improvement of 1.91 ×."
    ],
    "limitations": [
      "The cited multipliers are paper-specific upper results for named models and hardware, not guaranteed gains across request distributions or latency targets.",
      "The retrieved arXiv HTML did not provide a publication date in its text, so date is recorded as unknown."
    ]
  }
]
```

Synthesis: These sources address distinct bottlenecks: speculative decoding cuts serial target-model steps when draft acceptance and spare concurrency are favorable; GPTQ reduces weight traffic/storage but needs suitable kernels and does not reduce arithmetic; PagedAttention manages dynamic KV memory to admit larger batches; and Orca/Sarathi scheduling improve utilization while exposing throughput-versus-latency and workload-composition tradeoffs. Across all, gains are conditional on workload, hardware, baseline and resource regime; headline multipliers should not be compared as if measured under a common benchmark.

Gaps: The retrieved sources do not provide a unified, contemporary benchmark spanning small models, batch-1 latency and multi-user serving with matched hardware, quality metrics, KV-cache quantization, and per-token latency/cost. Orca and Sarathi dates were not available in retrieved text, and GPTQ's retrieved arXiv page did not expose a date, so those records retain unknown dates rather than inferred values.

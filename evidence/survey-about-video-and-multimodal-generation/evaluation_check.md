# Verify draft claims on video-generation evaluation, controllability failures, temporal safety, data provenance, and provider disclosures

```json
[
  {
    "id": "2411.13503",
    "url": "https://arxiv.org/html/2411.13503v1",
    "title": "VBench++: Comprehensive and Versatile Benchmark Suite for Video Generative Models",
    "date": "2024-11-20",
    "source": "web",
    "claims": [
      "The paper says VBench++ evaluates 16 video-generation dimensions using tailored prompts and dimension-specific evaluation methods, with a hierarchical decomposition of video quality and condition consistency.",
      "VBench++ includes human preference annotations to validate alignment with human perception and supports text-to-video and image-to-video; it extends prior VBench by adding image-to-video and trustworthiness evaluation.",
      "The source states existing evaluation metrics do not fully align with human perception, supporting multidimensional rather than single-score assessment.",
      "The fetched primary text identifies trustworthiness dimensions, including culture fairness, human bias, and safety; its described safety assessment includes NudeNet, Stable Diffusion Safety Checker, and Q16."
    ],
    "evidence": [
      "VBench comprises 16 dimensions in video generation",
      "Existing metrics do not fully align with human perceptions",
      "We also provide a dataset of human preference annotations to validate our benchmarks’ alignment with human perception",
      "we use three safety detection models: NudeNet, the Stable Diffusion Safety Checker, and the Q16 classifier"
    ],
    "limitations": [
      "Search result supplies publication timestamp 2024-11-20, while fetched HTML itself did not expose an explicit publication date in the returned excerpt; date is therefore taken from the returned search metadata.",
      "The source describes benchmark design and human alignment studies; it does not prove universal validity, complete harm coverage, or independent certification of any generated video.",
      "Automatic safety outputs depend on the named detector suite and tested prompts; detector coverage does not establish full real-world safety."
    ]
  },
  {
    "id": "2503.04666",
    "url": "https://openaccess.thecvf.com/content/CVPR2026/papers/Bugliarello_What_Are_You_Doing_A_Closer_Look_at_Controllable_Human_CVPR_2026_paper.pdf",
    "title": "What Are You Doing? A Closer Look at Controllable Human Video Generation",
    "date": "unknown",
    "source": "web",
    "claims": [
      "WYD contains 1,544 captioned videos, classified across nine aspects, and targets controllable image-to-video generation of humans.",
      "Dataset preparation combined semi-automatic filtering and manual verification; the paper reports more than 2,500 rater hours and describes over 500 hours of annotation time for parts of the preparation pipeline.",
      "The authors use video- and human-level metrics, reporting human-preference validation; pose adherence and person consistency expose aspects that broad video-quality measures can miss.",
      "Reported failure modes include disappearance of human-interaction objects; the paper says FVD is largely unaffected because these objects occupy a small fraction of the frame.",
      "The authors identify pose estimator errors as a limitation for pose-based metrics and note the dataset is focused on visually conditioned image-to-video models."
    ],
    "evidence": [
      "WYD consists of 1,544 captioned videos",
      "measure performance across 9 aspects of human generation",
      "rigorously finalized through manual annotations (2500+ rater hours)",
      "objects may disappear. As they cover a small percentage of the frame, metrics like FVD are largely unaffected",
      "we found sometimes that it makes incorrect predictions"
    ],
    "limitations": [
      "The requested CVPR 2026 paper endpoint returns primary paper text, but the returned text does not give the conference publication date; date recorded as unknown rather than inferred from the conference label or arXiv-derived identifier.",
      "WYD is a human-centric, visually conditioned I2V benchmark, not a general assessment of all T2V, audio/video, or long-horizon generation.",
      "The reported limitations of pose metrics and FVD caution against treating benchmark metrics as comprehensive control or interaction measures."
    ]
  },
  {
    "id": "2024-12-04-T2VSafetyBench",
    "url": "https://papers.nips.cc/paper_files/paper/2024/file/74eed5f568354c2e77dd9b018f38a9d4-Paper-Datasets_and_Benchmarks_Track.pdf",
    "title": "T2VSafetyBench: Evaluating the Safety of Text-to-Video Generative Models",
    "date": "unknown",
    "source": "web",
    "claims": [
      "The NeurIPS proceedings version defines four primary safety categories and 14 critical aspects, including temporal risks; this supersedes an earlier arXiv version's abstract, which described 12 aspects.",
      "The benchmark examines risks where individually harmless frames can form unsafe sequences through action sequence, dynamic variation, or coherent context.",
      "The paper samples one frame per second and uses GPT-4 assessments alongside manual evaluations; it reports evaluations of nine T2V models.",
      "Because of compute costs and model blocking, the reported experimental results use a 689-prompt Tiny-T2VSafetyBench subset, with one video generated per prompt/model.",
      "The authors report no evaluated model excels in all aspects and describe a safety/usefulness trade-off; these are findings on their benchmark and tested models, not a universal ranking."
    ],
    "evidence": [
      "We define 4 primary categories with 14 critical aspects",
      "individual frames might appear harmless but the entire sequence can present unsafe content through continuity between frames",
      "we capture a frame per second",
      "contains 689 prompts",
      "we conduct a thorough safety evaluation on 9 recently released T2V models"
    ],
    "limitations": [
      "The supplied NeurIPS proceedings PDF search result gave no explicit publication date; date is recorded as unknown. NeurIPS 2024 track naming is not itself an exact day-level publication date.",
      "The seed draft's 12-aspect statement pertains to earlier arXiv text; the primary proceedings version says 14 aspects. Do not combine the earlier 12-aspect list with proceedings-version numerical claims.",
      "Sampling at one frame per second may miss transient events and cannot establish complete temporal risk detection; prompts, model access restrictions, GPT-4 judge behavior, and manual-review scope constrain inference."
    ]
  },
  {
    "id": "2412.17847",
    "url": "https://arxiv.org/html/2412.17847v2",
    "title": "Bridging the Data Provenance Gap Across Text, Speech, and Video",
    "date": "2025-02-19",
    "source": "web",
    "claims": [
      "The audit covers nearly 4,000 public datasets from 1990–2024 across modalities; for video specifically, it traces 104 datasets across 33 tasks spanning 2009–2024.",
      "The abstract reports that fewer than 33% of datasets are restrictively licensed, while over 80% of source content in widely used text, speech, and video datasets carries non-commercial restrictions.",
      "The paper reports that web-crawled, synthetic, and social-media sources have become prominent and states YouTube accounts for 71% of video data in the audited corpus.",
      "The study describes provenance and licensing mismatches through dataset derivation/repackaging, but explicitly treats enforceability of platform terms as an open legal question beyond its scope.",
      "These are ecosystem-level observations about the audited public datasets, not a direct inventory or audit of a named generator's private training corpus."
    ],
    "evidence": [
      "manual analysis covers nearly 4000 public datasets between 1990-2024",
      "trace the provenance and features of 104 video datasets, covering 33 popular video tasks",
      "over 80% of the source content in widely-used text, speech, and video datasets, carry non-commercial restrictions",
      "We find that 71% of Video data ... is from YouTube",
      "We treat the enforceability of licenses and terms as an open legal question, beyond the scope of our work"
    ],
    "limitations": [
      "The page explicitly identifies the study as an audit of public/popular datasets; its selection rules do not warrant extrapolating the figures to all datasets or private model training data.",
      "The paper's license/provenance analysis is not a court finding or legal opinion on infringement, permission, or enforceability.",
      "The paper landing text provides 2025-02-19 for v2; that is the retrieved version date, not necessarily the initial submission date."
    ]
  },
  {
    "id": "openai-sora-2-system-card",
    "url": "https://openai.com/index/sora-2-system-card/",
    "title": "Sora 2 System Card",
    "date": "2025-09-30",
    "source": "web",
    "claims": [
      "The card is dated September 30, 2025 and describes Sora 2 as a video-and-audio generation system; OpenAI identifies nonconsensual likeness use and misleading generations as risks.",
      "OpenAI says training data include publicly available internet information and third-party partnership information; the returned card text also describes user-, trainer-, and researcher-supplied or generated data, but does not provide a complete corpus inventory.",
      "The card describes moderation of inputs and outputs, including video frames, audio transcripts, comments, and scene-description text, alongside output safety models and product/policy controls.",
      "The card acknowledges some deceptive content is contextual and not readily detectable by classifiers, framing mitigations as iterative rather than complete.",
      "The system card is a provider-authored disclosure; it documents stated policies and procedures but is not an independent audit of training-data provenance or mitigation effectiveness."
    ],
    "evidence": [
      "September 30, 2025",
      "publicly available on the internet, information that we partner with third parties to access",
      "Input prompts, output video frames, audio transcripts, comments, and output scene description texts are run through various safety models",
      "some deceptive content is highly contextual and not easily detectable by classifiers",
      "We’re taking an iterative approach to safety"
    ],
    "limitations": [
      "The date is stated directly in the official card and corroborated by the official page metadata.",
      "The card does not enumerate a reproducible, itemized training corpus or independently validate all source permissions.",
      "System-card assertions about safeguards and risk controls are provider-reported; they do not alone quantify real-world effectiveness or residual risk."
    ]
  },
  {
    "id": "2503.21755",
    "url": "https://huggingface.co/papers/2503.21755",
    "title": "VBench-2.0: Advancing Video Generation Benchmark Suite for Intrinsic Faithfulness",
    "date": "2025-03-27",
    "source": "hf-search",
    "claims": [
      "The Hugging Face paper record dates the item March 27, 2025 and summarizes five evaluation dimensions: Human Fidelity, Controllability, Creativity, Physics, and Commonsense.",
      "The abstract describes combining generalist VLM/LLM evaluators with specialist anomaly-detection methods and extensive annotations intended to assess alignment with human judgment.",
      "The paper frames its target as intrinsic faithfulness—physical laws, commonsense, anatomical correctness, and compositional integrity—beyond visual quality and temporal consistency alone."
    ],
    "evidence": [
      "Published on Mar 27, 2025",
      "assesses five key dimensions: Human Fidelity, Controllability, Creativity, Physics, and Commonsense",
      "integrates generalists such as state-of-the-art VLMs and LLMs, and specialists, including anomaly detection methods",
      "We conduct extensive annotations to ensure alignment with human judgment"
    ],
    "limitations": [
      "Per the user-required source label, this record is attributed to hf-search; fetched HF page abstract confirms the displayed date and summary, but is not full paper text.",
      "The retrieved record does not establish detailed sample sizes, metric definitions, quantitative results, or independent validity of the evaluators.",
      "Benchmark scenarios and model-based judging may have blind spots; claims should be phrased as the benchmark's design goals and abstract-level description."
    ]
  }
]
```

Synthesis: VBench++ and VBench-2.0 provide broad, multidimensional evaluation, while WYD demonstrates how targeted controllability tests reveal localized human/object failures that aggregate video metrics can miss; T2VSafetyBench directly evaluates sequence-level harm, but its proceedings version has 14 aspects and reports results on a 689-prompt subset with 1-fps sampling. The provenance audit gives ecosystem-level evidence, not a private-model corpus audit, and Sora's dated system card offers provider-reported safeguards and data-source categories rather than independently verified provenance or effectiveness; key gaps remain date ambiguity for WYD/T2VSafetyBench, temporal sampling blind spots, incomplete corpus disclosure, and independent validation.

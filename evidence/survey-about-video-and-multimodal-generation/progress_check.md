# Verify claims on long-horizon generation, control, multimodal conditioning, and evaluation

```json
[
  {
    "id": "2508.03694",
    "url": "https://arxiv.org/abs/2508.03694",
    "title": "LongVie: Multimodal-Guided Controllable Ultra-Long Video Generation",
    "date": "2025-08-05",
    "source": "arxiv",
    "claims": [
      "The abstract describes LongVie as autoregressive and combines unified noise initialization, global control-signal normalization, dense-plus-sparse multimodal controls, and degradation-aware training.",
      "The paper introduces LongVGenBench with 100 high-resolution videos longer than one minute; the full-text search result specifies 1080p, at least one minute, 100 one-shot videos, and real-world/game-based scenarios.",
      "Full-text search results report that evaluation divides reference videos into six-second clips, segments each video into ten 49-frame clips at 8 fps with one-frame overlap, and uses extracted control signals.",
      "The retrieved result reports a quantitative table in which LongVie scores 87.12% Subject Consistency, 91.76% Background Consistency, 21.82% Overall Consistency, 46.59% Dynamic Degree, 98.43% Temporal Flickering, 55.31% Aesthetic Quality, 64.91% Imaging Quality, SSIM 0.557, and LPIPS 0.290.",
      "The abstract's state-of-the-art claim is qualified by full-text metrics: LongVie is not best in every listed column (for example, the table gives other methods higher Dynamic Degree and some quality metrics)."
    ],
    "evidence": [
      "LongVGenBench, a comprehensive benchmark consisting of 100 high-resolution videos spanning diverse real-world and synthetic environments, each lasting over one minute.",
      "each lasting at least one minute at 1080p resolution",
      "each video is further segmented into ten 49-frame clips at 8 frames per second (fps), with a 1-frame overlap",
      "LongVie | 87.12% | 91.76% | 21.82% | 46.59% | 98.43% | 55.31% | 64.91% | 0.557 | 0.290"
    ],
    "limitations": [
      "LongVie full evaluation details and metrics here come from a web-search excerpt of the primary arXiv HTML, not from the provided abstract endpoint itself; exact table interpretation depends on the paper's metric definitions and protocol.",
      "The reported benchmark is a finite curated reference-video benchmark with segmented evaluation; it does not establish indefinite generation or general performance across all domains.",
      "The paper's broad state-of-the-art wording should not be paraphrased as winning every metric; no statistical-significance evidence was retrieved."
    ]
  },
  {
    "id": "unknown",
    "url": "https://openaccess.thecvf.com/content/CVPR2025/papers/Henschel_StreamingT2V_Consistent_Dynamic_and_Extendable_Long_Video_Generation_from_Text_CVPR_2025_paper.pdf",
    "title": "StreamingT2V: Consistent, Dynamic, and Extendable Long Video Generation from Text",
    "date": "unknown",
    "source": "web",
    "claims": [
      "StreamingT2V uses a short-term Conditional Attention Module conditioned on preceding-chunk features, a long-term Appearance Preservation Module anchored on the first chunk, and randomized blending for chunk-wise enhancement.",
      "The paper's figure/abstract describes demonstrations up to 1200 frames (two minutes) and says they can be extended; this is a demonstration claim, distinct from the quantitative protocol.",
      "Quantitative evaluation uses 50 prompts and 240-frame generated videos; table values are MAWE 52.3, SCuts 0.04, and CLIP 31.73 for StreamingT2V.",
      "The table gives OpenSoraPlan MAWE 72.9, SCuts 0.24, CLIP 29.34 and FreeNoise SCuts 0; authors characterize StreamingT2V as about 30% lower MAWE than the next best and warn that FreeNoise's low SCuts results from near-constant videos.",
      "The paper defines SCuts as detected scene-cut count and describes MAWE as balancing motion amount and warp error; its reported metrics are averaged per video, with optical-flow metrics computed after resizing to 720x720."
    ],
    "evidence": [
      "Demonstrations include videos up to 1200 frames, spanning 2 minutes",
      "we created a test set composed of 50 prompts",
      "All evaluations are conducted on 240-frames video generations.",
      "StreamingT2V (Ours) 52.3 0.04 31.73",
      "Only FreeNoise achieves a slightly lower, perfect score. However, FreeNoise produces near-static videos",
      "SCuts, which counts the number of detected scene cuts in a video"
    ],
    "limitations": [
      "The two-minute result is a showcased demonstration, whereas the reported automatic comparison evaluates only 240 frames; do not state that the two-minute examples themselves earned those scores.",
      "SCuts is vulnerable to stagnation/static-output gaming, as the paper explicitly notes; MAWE and CLIP are paper-defined/automatic metrics and do not independently prove perceptual quality.",
      "No date was visible in the retrieved full-paper excerpt, so the record date remains unknown."
    ]
  },
  {
    "id": "unknown",
    "url": "https://openaccess.thecvf.com/content/CVPR2025/papers/Cai_DiTCtrl_Exploring_Attention_Control_in_Multi-Modal_Diffusion_Transformer_for_Tuning-Free_CVPR_2025_paper.pdf",
    "title": "DiTCtrl: Exploring Attention Control in Multi-Modal Diffusion Transformer for Tuning-Free Multi-Prompt Longer Video Generation",
    "date": "unknown",
    "source": "web",
    "claims": [
      "DiTCtrl is described as training-free multi-prompt generation under MM-DiT, using attention sharing and mask-guided semantic control to treat prompt sequences as temporal editing.",
      "MPVBench comprises 130 long-form prompts across ten transition types; automatic tests generate videos with three random seeds and report CSCV, VBench Motion Smoothness, and CLIP Text-Image Similarity.",
      "The reported automatic table gives DiTCtrl CSCV 84.90%, Motion Smoothness 97.80%, and Text-Image Similarity 30.68%; FreeNoise has higher Text-Image Similarity (32.69%) while DiTCtrl has the highest reported CSCV and motion smoothness in that table.",
      "The paper motivates CSCV by saying average neighborhood CLIP similarity may dilute a single prompt-boundary discontinuity, and defines CSCV from variation in adjacent-frame feature similarities.",
      "A human study reports 28 participants and scores on a 1-to-5 scale; DiTCtrl scores 4.11 overall preference, 4.17 motion pattern, 4.26 temporal consistency, and 3.91 text alignment."
    ],
    "evidence": [
      "we produce 130 long-form prompts of 10 different transition modes",
      "we generate videos using 130 prompts from our MPVBench, with three random seeds set",
      "DiTCtrl(Ours) 84.90% 97.80% 30.68%",
      "FreeNoise 84.37% 97.22% 32.69%",
      "A total of 28 participants",
      "Scores range from 1 to 5, with higher scores indicating better performance."
    ],
    "limitations": [
      "The custom CSCV is a proposed proxy for transition smoothness, not a direct proof of perceptual continuity; its behavior is tied to the authors' feature representation and formula.",
      "The abstract's state-of-the-art statement should be scoped to the reported MPVBench comparisons and metrics; DiTCtrl does not top every automatic metric.",
      "The retrieved paper excerpt does not supply a common long-duration protocol directly comparable with StreamingT2V's 240-frame test or LongVGenBench; the publication date was not surfaced."
    ]
  },
  {
    "id": "2508.03694",
    "url": "https://huggingface.co/papers/2508.03694",
    "title": "LongVie: Multimodal-Guided Controllable Ultra-Long Video Generation",
    "date": "2025-08-05",
    "source": "hf-search",
    "claims": [
      "The Hugging Face record summarizes LongVie as addressing temporal consistency and visual degradation with unified noise initialization, global control normalization, multimodal control, and degradation-aware training.",
      "The record is an index-level summary that independently surfaces the same central method components, but does not add benchmark scoring evidence."
    ],
    "evidence": [
      "LongVie, an end-to-end autoregressive framework, addresses temporal consistency and visual degradation in ultra-long video generation",
      "unified noise initialization, global control signal normalization, multi-modal control, and degradation-aware training"
    ],
    "limitations": [
      "This is a paper-index summary, not an independent evaluation or replication.",
      "No detailed metrics or experimental protocol were provided by this record."
    ]
  },
  {
    "id": "2506.00830",
    "url": "https://arxiv.org/abs/2506.00830",
    "title": "SkyReels-Audio: Omni Audio-Conditioned Talking Portraits in Video Diffusion Transformers",
    "date": "2025-06-01",
    "source": "arxiv",
    "claims": [
      "SkyReels-Audio's abstract describes portrait video generation/editing conditioned on audio together with text, image, or video inputs, and calls its sliding-window approach suitable for 'infinite-length' generation.",
      "Full-text search evidence reports an evaluation on 100 test clips sampled from HDTF and an internal dataset, with source videos excluded from training; it lists FID, FVD, Sync-C/Sync-D, Q-align IQA/ASE, and a small subjective study.",
      "On the reported HDTF comparison table, SkyReels-Audio is listed with FID 38.32, FVD 364.71, Sync-C 6.06, Sync-D 9.12, IQA 4.60, and ASE 2.92; the reported internal-dataset row gives Sync-C 6.75, Sync-D 8.32, IQA 4.42, and ASE 2.91.",
      "The paper reports 20 participants rating internal-set audio-visual consistency and visual quality on a 0-to-2 scale; its HDTF lip-sync table shows only a small Sync-C difference from LatenSync (8.49 vs. 8.48), with LatenSync higher IQA (3.63 vs. 3.62).",
      "The abstract's 'infinite-length' wording is a capability claim; the retrieved evaluation excerpt provides no actual infinite-duration scored test or operational duration limit."
    ],
    "evidence": [
      "supports infinite-length generation and editing",
      "a test set comprising 100 video clips randomly sampled from the HDTF dataset and the internal dataset",
      "SkyReels-Audio | 38.32 | 364.71 | 6.06 | 9.12 | 4.60 | 2.92",
      "LatenSync ... 8.48 ... 3.63 ... SkyReels-Audio ... 8.49 ... 3.62",
      "A total of 20 participants rated each aspect on a scale for 0 to 2"
    ],
    "limitations": [
      "The quantitative comparisons are tied to the paper's datasets and setup; the internal dataset's sampling/composition and broader reproducibility are not established by the retrieved excerpt.",
      "The abstract's broad superior-performance claim is not uniformly reflected in every table metric or comparator (e.g., the HDTF lip-sync table has marginal Sync-C gain but lower IQA than LatenSync).",
      "No measured maximum duration or scored infinite-length stress test was retrieved; 'infinite-length' should not be presented as empirically verified unlimited duration."
    ]
  }
]
```

Synthesis: The full-text evidence separates long demonstrations from scored tests: StreamingT2V shows 1200-frame examples but quantifies 240-frame output; LongVie uses a 100-video reference benchmark with segmented evaluation; DiTCtrl evaluates multi-prompt transitions using its own CSCV metric and a human study. Abstract-level "state of the art" and "infinite length" wording needs qualification against actual tables and protocols: metrics are task-specific, some are proposed proxies (and can have pathologies), and no shared long-horizon evaluation permits direct cross-paper ranking.
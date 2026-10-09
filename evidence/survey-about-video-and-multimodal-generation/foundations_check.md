# Verify foundational architectural claims and contrasts: Video Diffusion Models, Latent Video Diffusion, Emu, NExT-GPT, Open-Sora 2.0, and Step-Video-T2V

```json
[
  {
    "id": "2204.03458v2",
    "url": "https://arxiv.org/abs/2204.03458v2",
    "title": "Video Diffusion Models",
    "date": "2022-06-22",
    "source": "web",
    "claims": [
      "The paper describes a video diffusion model as an extension of a standard image diffusion architecture that jointly trains on image and video data; its stated motivation for joint data is reduced minibatch-gradient variance and faster optimization.",
      "For longer and higher-resolution videos, the paper introduces conditional spatial and temporal extension by sampling.",
      "The available primary abstract does not substantiate the seed note's specific architectural claim about interleaved temporal attention/convolution and spatial layers; that detail remains unverified from the retrieved text."
    ],
    "evidence": [
      "Our model is a natural extension of the standard image diffusion architecture, and it enables jointly training from image and video data, which we find to reduce the variance of minibatch gradients and speed up optimization.",
      "To generate long and higher resolution videos we introduce a new conditional sampling technique for spatial and temporal video extension"
    ],
    "limitations": [
      "Fetched text is the abstract, not the paper's architectural sections; it does not establish the precise video U-Net layer arrangement noted in the seed.",
      "The abstract describes results as promising and gives no benchmark values in the retrieved excerpt."
    ]
  },
  {
    "id": "2211.13221v1",
    "url": "https://arxiv.org/abs/2211.13221v1",
    "title": "Latent Video Diffusion Models for High-Fidelity Video Generation with Arbitrary Lengths",
    "date": "2022-11-23",
    "source": "web",
    "claims": [
      "This work performs diffusion and denoising in a low-dimensional 3D latent space, which it presents as a way to ease the computational cost of high-dimensional video diffusion.",
      "The authors report that models trained on tens of frames can generate thousands of frames autoregressively and introduce conditional latent perturbation to reduce degradation in long-duration synthesis.",
      "These are author-reported capabilities; the abstract does not establish uniform temporal coherence or quality over the entire reported duration."
    ],
    "evidence": [
      "we propose to perform diffusion and denoising in a low-dimensional 3D latent space",
      "though trained on tens of frames, our models can generate videos with arbitrary lengths, i.e., thousands of frames, in an autoregressive way",
      "conditional latent perturbation is further introduced to reduce performance degradation during synthesizing long-duration videos"
    ],
    "limitations": [
      "The fetched abstract provides no numerical quality values or specific details of the autoregressive context/windowing scheme.",
      "'Arbitrary lengths' is a paper claim and should not be paraphrased as proven sustained coherence at all lengths."
    ]
  },
  {
    "id": "2307.05222v1",
    "url": "https://arxiv.org/abs/2307.05222v1",
    "title": "Generative Pretraining in Multimodality",
    "date": "2023-07-11",
    "source": "web",
    "claims": [
      "Emu encodes visual signals as embeddings and places them in an interleaved sequence with text tokens; the abstract explicitly includes interleaved image, text, and video inputs.",
      "Its stated unified training objective classifies the next text token or regresses the next visual embedding.",
      "The abstract describes image-and-text generation and video question answering, but does not establish native temporally dense video generation; the seed's distinction between frame/context use and video generation should be retained cautiously."
    ],
    "evidence": [
      "visual signals are encoded into embeddings, and together with text tokens form an interleaved input sequence",
      "unified objective of classifying the next text token or regressing the next visual embedding",
      "such as videos with interleaved frames and text",
      "supports in-context image and text generation"
    ],
    "limitations": [
      "The retrieved abstract does not establish whether all visual generation outputs use the exact decoder arrangement stated in the seed; avoid asserting decoder details on this evidence alone.",
      "Video input and video question answering are not evidence of native video synthesis."
    ]
  },
  {
    "id": "2309.05519v2",
    "url": "https://arxiv.org/abs/2309.05519v2",
    "title": "NExT-GPT: Any-to-Any Multimodal LLM",
    "date": "2023-09-13",
    "source": "web",
    "claims": [
      "NExT-GPT connects an LLM with multimodal adaptors and different diffusion decoders, using pretrained encoders and decoders to accept and generate combinations of text, images, video, and audio.",
      "The abstract reports tuning about 1% of certain projection-layer parameters; this is not evidence that only 1% of the entire system or all training phases are updated.",
      "The architecture is modular and should not be equated with one shared native generative process across all modalities."
    ],
    "evidence": [
      "We connect an LLM with multimodal adaptors and different diffusion decoders",
      "perceive inputs and generate outputs in arbitrary combinations of text, images, videos, and audio",
      "leveraging the existing well-trained highly-performing encoders and decoders",
      "tuned with only a small amount of parameter (1%) of certain projection layers"
    ],
    "limitations": [
      "The abstract does not give detailed comparative benchmark metrics or quantify the full set of trainable parameters across every phase.",
      "Broad modality coverage does not by itself prove uniform quality or synchronized audio-video generation in arbitrary combinations."
    ]
  },
  {
    "id": "2503.09642v2",
    "url": "https://arxiv.org/abs/2503.09642v2",
    "title": "Open-Sora 2.0: Training a Commercial-Level Video Generation Model in $200k",
    "date": "2025-03-23",
    "source": "web",
    "claims": [
      "The abstract reports Open-Sora 2.0 as a video-generation model trained for $200k and claims comparability to HunyuanVideo and Runway Gen-3 Alpha based on human evaluation and VBench.",
      "The retrieved introduction describes human preference evaluation across 100 prompts covering visual quality, prompt adherence, and motion quality.",
      "The fetched text does not verify the seed's architectural specifics (video autoencoder, dual/single-stream blocks, 3D RoPE, or flow matching); those require the relevant full-text sections and should not be promoted as verified by this abstract/introduction excerpt."
    ],
    "evidence": [
      "According to human evaluation results and VBench scores, Open-Sora 2.0 is comparable to global leading video generation models",
      "The evaluation is conducted on 100 prompts carefully designed to cover three key aspects: 1) visual quality, 2) prompt adherence, and 3) motion quality.",
      "Results show that our model performs favorably against other top-performing models in all three aspects."
    ],
    "limitations": [
      "The excerpt provides no exact VBench scores or win-rate percentages; comparability is an author-reported result and depends on the evaluation setup.",
      "The retrieved portion does not substantiate detailed architecture claims or establish universal superiority."
    ]
  },
  {
    "id": "2502.10248v2",
    "url": "https://arxiv.org/abs/2502.10248v2",
    "title": "Step-Video-T2V Technical Report: The Practice, Challenges, and Future of Video Foundation Model",
    "date": "2025-02-17",
    "source": "web",
    "claims": [
      "The abstract describes a 30B-parameter text-to-video model with generation up to 204 frames, a video VAE with 16x16 spatial and 8x temporal compression, two bilingual text encoders, and a 3D full-attention DiT trained with flow matching.",
      "The authors frame a distinction between Level-1 cross-modal translation (generating video from text/visual/multimodal context) and Level-2 prediction (forecasting future events and more advanced reasoning/simulation tasks).",
      "The report explicitly categorizes current diffusion text-to-video systems, including Step-Video, as Level-1; this conceptual taxonomy does not prove that the systems lack all learned predictive structure."
    ],
    "evidence": [
      "30B parameters and the ability to generate videos up to 204 frames in length",
      "achieving 16x16 spatial and 8x temporal compression ratios",
      "A DiT with 3D full attention is trained using Flow Matching",
      "Level-1: translational video foundation model.",
      "Level-2: predictable video foundation model.",
      "Current diffusion-based text-to-video models ... belong to Level-1."
    ],
    "limitations": [
      "Model scale, frame capacity, architecture, and benchmark claims come from the authors' technical report; retrieved abstract text does not provide independent validation or benchmark scores.",
      "Translation-versus-prediction is the report's framing, not evidence that generated videos are physically correct or that diffusion models cannot encode dynamics."
    ]
  }
]
```

Synthesis: The foundational progression is well supported at the high level: direct video diffusion extends image diffusion, while latent video diffusion moves denoising into a compressed 3D space and uses autoregressive continuation for long outputs. The available excerpts support these claims but do not verify the precise early U-Net layer recipe or prove persistent coherence at thousands of frames. Emu and NExT-GPT are materially different: Emu trains a next-element objective over interleaved text and visual embeddings, whereas NExT-GPT routes through an LLM, adaptors, and specialist encoders/decoders; neither should be represented as a single demonstrated native video-and-audio generator.

For recent systems, Step-Video-T2V's abstract supports specific latent-compression, full-attention DiT, and flow-matching claims, alongside an explicitly author-defined translation/prediction taxonomy. Open-Sora 2.0's fetched excerpt verifies the evaluation framing and comparability claim, but not its seed-listed detailed architecture; those details remain gaps in this check. Across recent reports, comparisons remain author-reported and evaluation-specific, so avoid universal superiority or world-model conclusions.
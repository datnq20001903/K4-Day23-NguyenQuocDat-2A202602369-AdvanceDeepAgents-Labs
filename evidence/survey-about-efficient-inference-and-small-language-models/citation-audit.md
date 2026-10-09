# Citation audit — FINAL wording

Exactly three claims were checked from three distinct URLs. Report and source registry were not modified. The relevant researcher notes were consulted. The fetched sources were treated as evidence only.

## Claim [1] — Speculative decoding

**Report wording:** “Speculative decoding changes the schedule rather than the target distribution: a smaller approximation proposes several candidates, and the target verifies them in parallel. The method's sampling construction can preserve the target model's output distribution while accepting multiple tokens from one target pass; its speed depends on draft quality and available concurrency. The demonstration on T5-XXL reports 2–3× acceleration against its standard T5X implementation, but that is a particular model and baseline, not a general multiplier.”

**URL:** https://proceedings.mlr.press/v202/leviathan23a.html

**Metadata/title/date check:** Retrieved page title exactly matches the registry/report title, “Fast Inference from Transformers via Speculative Decoding.” The official citation metadata gives PMLR volume 202, ICML 2023, and year 2023; report reference lists date “unknown,” which is incomplete but not an incorrect title or conflicting date. Research note records 2023-07-03; fetched page excerpt identifies the conference dates July 23–29, 2023, so a day-level publication date should not be asserted based on this page alone. URL is exact and resolves.

**Verbatim supporting excerpt:** “we introduce speculative decoding - an algorithm to sample from autoregressive models faster without any changes to the outputs, by computing several tokens in parallel.” Also: “using speculative execution and a novel sampling method, we can make exact decoding from the large models faster, by running them in parallel on the outputs of the approximation models, potentially generating several tokens concurrently, and without changing the distribution.” Also: “We demonstrate it on T5-XXL and show a 2X-3X acceleration compared to the standard T5X implementation, with identical outputs.”

**Assessment:** These statements substantively support the claim. The conditional discussion of draft quality and concurrency is cautious synthesis supported by the described approximation/speculation mechanism and research notes, rather than a quantified abstract result. “A smaller approximation” is consistent with the paper's abstract reference to “more efficient models,” although the abstract excerpt does not explicitly say the approximation is smaller. No meaningful discrepancy in final wording.

Status: PASS

**Suggested correction:** No substantive correction required. For strict source/registry metadata fidelity, update the bibliography date only if the desired convention is year-level (2023); otherwise “unknown” is conservative. Do not cite 2023-07-03 as verified from the fetched excerpt.

## Claim [7] — LaMini-LM, narrowed evaluation wording

**Report wording:** “LaMini-LM takes a broader instruction-data route. It reports 2.58 million examples and GPT-3.5 Turbo-generated answers, and trains encoder-decoder and decoder-only model families. Its evaluation includes 15 NLP benchmarks and manual assessment. These evaluations broaden the evidence beyond a single score, but teacher-generated responses may transmit teacher-specific errors or style; these reported assessments do not establish universal parity.”

**URL:** https://huggingface.co/papers/2304.14402

**Metadata/title/date check:** Exact URL resolves. Retrieved title, “LaMini-LM: A Diverse Herd of Distilled Models from Large-Scale Instructions,” matches the bibliography. Retrieved page states “Published: 2023-04-27” and “Published on Apr 27, 2023,” matching the bibliography date 2023-04-27. Metadata fidelity PASS.

**Verbatim supporting excerpt:** “we carefully develop a large set of 2.58M instructions based on both existing and newly-generated instructions.” Also: “we generate responses for these instructions using gpt-3.5-turbo.” Also: “We then exploit the instructions to tune a host of models, dubbed LaMini-LM, of varying sizes, both from the encoder-decoder as well as the decoder-only families.” Also: “We evaluate our models both automatically (on 15 different NLP benchmarks) and manually.”

**Assessment:** The narrowed wording is directly supported by the fetched abstract. The final statement explicitly limits interpretation: the abstract says models are “on par with competitive baselines,” but does not establish universal parity; the teacher-error/style caution is presented as a possibility, not as a reported experimental finding. The report correctly avoids claiming detailed manual-assessment results or benchmark-level superiority from this abstract.

Status: PASS

**Suggested correction:** No change required. The bibliography and registry date 2023-04-27 are confirmed by the fetched source. A prior notes date of 2024-03-17 conflicts with the source page; the final report follows the verified 2023-04-27 date, resolving that issue.

## Claim [11] — Edge-First, abstract-level claim

**Report wording:** “Device-level evidence makes constraints tangible. *Edge-First Language Model Inference* benchmarks small language models on single edge devices and extends the analysis to distributed edge clusters. Its abstract identifies some scenarios where edge inference offers comparable performance at lower cost, and others where cloud fallback is essential because of scalability or model-capacity limits. This platform-specific abstract supports considering deployment context; it does not establish a universal edge/cloud winner.”

**URL:** https://arxiv.org/html/2505.16508

**Metadata/title/date check:** Exact URL resolves. Fetched page title is “Edge-First Language Model Inference: Models, Metrics, and Tradeoffs,” matching report and registry. The page excerpt says it “has been accepted for publication and presentation at the 45th IEEE International Conference on Distributed Computing Systems (IEEE ICDCS 2025),” but does not provide a publication date in the retrieved text. Registry date “unknown” is appropriately conservative; no date was invented. Metadata/title fidelity PASS; exact publication date remains not verified.

**Verbatim supporting excerpt (abstract):** “This work examines the interplay between edge and cloud deployments, starting from detailed benchmarking of SLM capabilities on single edge devices, and extending to distributed edge clusters. We identify scenarios where edge inference offers comparable performance with lower costs, and others where cloud fallback becomes essential due to limits in scalability or model capacity. Rather than proposing a one-size-fits-all solution, we present platform-level comparisons and design insights for building efficient, adaptive LM inference systems across heterogeneous environments.”

**Assessment:** The report accurately paraphrases the abstract-level scope and findings. It does not extend the claim into detailed device metrics, specific numerical comparisons, or a universal deployment conclusion. The report's explicit “does not establish a universal edge/cloud winner” qualification is consistent with the source's “Rather than proposing a one-size-fits-all solution” language. Since evidence checked here is the abstract-level text, conclusions beyond that abstract are not assessed.

Status: PASS

**Suggested correction:** No substantive correction required. Keep date as unknown unless verified publication metadata is added. The final wording appropriately labels the evidentiary level as the abstract.
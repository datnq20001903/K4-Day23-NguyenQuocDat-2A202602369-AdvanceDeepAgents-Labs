# Fresh final citation audit — exactly three claims

Scope: Final audit checks exactly three claims in `/tmp/work/report/report.md` and exactly three distinct URLs: [7], [14], and [15]. Source metadata was checked against `/tmp/work/research/sources.json`; researcher notes and seed notes were compared with the returned source text, but note evidence is distinguished from direct retrieval. Only the three requested sources are in scope.

## Claim 1 — StreamingT2V demonstration and quantitative test length [7]

**Final report wording (verbatim):** “It showcases outputs up to 1,200 frames (two minutes), but its quantitative tests use 50 prompts and 240-frame generations.[7]”

**URL:** https://openaccess.thecvf.com/content/CVPR2025/papers/Henschel_StreamingT2V_Consistent_Dynamic_and_Extendable_Long_Video_Generation_from_Text_CVPR_2025_paper.pdf

**Title/date check:** Retrieved title, “StreamingT2V: Consistent, Dynamic, and Extendable Long Video Generation from Text,” matches [7] and the registry; fetched PDF identifies itself as the CVF Open Access version of the CVPR paper. Registry date is `unknown`; no exact publication date was present in returned retrieval. Keep date unknown, rather than infer it.

**Directly retrieved excerpt:** Figure 1 says: “Demonstrations include videos up to 1200 frames, spanning 2 minutes.” The returned excerpt does not include the 50-prompt and 240-frame methods passages. Researcher notes `notes/progress_check.md` and `seed-notes/progress.md` quote the paper: “we created a test set composed of 50 prompts” and “All evaluations are conducted on 240-frames video generations.” Thus the demonstration duration is directly returned; test protocol is note-supported but not exposed in this retrieval excerpt.

**Assessment:** The report properly distinguishes the showcase from quantitative evaluation and does not imply that the 1,200-frame examples received the 240-frame test scores. Its exact test-size and test-duration wording has note support, not direct visibility in the returned excerpt.

Status: PASS

**Suggested correction:** No required change. Preserve the distinction and do not characterize the test details as directly surfaced in this audit retrieval.

## Claim 2 — T2VSafetyBench proceedings categories/aspects and note-only protocol caveat [14]

**Final report wording (verbatim):** “T2VSafetyBench's proceedings version defines four categories and 14 aspects, including cases where individually benign frames form harmful sequences through continuity or change.[14] The paper reports that its evaluation samples one frame per second and uses GPT-4 assessments alongside manual review; due to compute costs and model blocking, the experiments use a 689-prompt subset and assess nine T2V models. These protocol details are reported in the paper-specific evidence notes, though the audit retrieval verified the proceedings abstract's category/aspect count and model count more directly than the sampling and subset passages.[14]”

**URL:** https://papers.nips.cc/paper_files/paper/2024/file/74eed5f568354c2e77dd9b018f38a9d4-Paper-Datasets_and_Benchmarks_Track.pdf

**Title/date check:** Retrieved title, “T2VSafetyBench: Evaluating the Safety of Text-to-Video Generative Models,” matches [14] and the registry URL. Registry date is `unknown`; the returned text did not establish a day-level publication date. The proceedings-version qualifier is material: notes identify 14 aspects in this proceedings version, in contrast to an earlier arXiv abstract’s 12.

**Directly retrieved excerpts:** The abstract says, “We define 4 primary categories with 14 critical aspects of video generation safety,” and reports evaluation on “9 recently released T2V models.” It also describes “the unique temporal risk inherent in video generation,” but the returned excerpt does not directly give the detailed continuity/change explanation. The report’s one-frame-per-second, GPT-4/manual-review, and 689-prompt/compute-cost details are supported by the paper-specific researcher notes (`notes/evaluation_check.md`; `seed-notes/evaluation.md`), whose excerpts include “we capture a frame per second,” “contains 689 prompts,” and descriptions of GPT-4 with manual review. Those details were not directly surfaced in the returned retrieval excerpt. Model count and category/aspect count are direct retrieval evidence; temporal continuity formulation and the protocol specifics are note-supported here, not directly retrieval-confirmed.

**Assessment:** The text expressly marks the protocol details as evidence-note claims and acknowledges what the audit retrieval did and did not verify. This is transparent about provenance. The full claim is not wholly direct-retrieval-verified; the temporal continuity/change wording and one-fps, review, and subset particulars remain dependent on notes.

Status: PASS

**Suggested correction:** Retain the existing explicit note-only caveat if those details remain. For a strictly retrieval-verified account, qualify or remove the one-fps, GPT-4/manual-review, 689-prompt, compute-cost/model-blocking, and detailed continuity/change phrases until the corresponding passages are directly retrieved. Do not imply these details came from the returned abstract excerpt.

## Claim 3 — Dataset provenance figures and explicit distinction between abstract and evidence notes [15]

**Final report wording (verbatim):** “An ecosystem audit offers evidence on dataset documentation rather than on any specific generator. It manually examines nearly 4,000 public datasets.[15] The paper-specific evidence notes describe a video subset of 104 datasets across 33 tasks and report that 36% lack license or intended-use documentation; they also note source restrictions can be obscured through repackaging.[15] The same notes report that over 80% of source content in widely used text, speech, and video datasets carries non-commercial restrictions, although fewer than one-third of datasets are restrictively licensed.[15] These detailed figures are supported by the researcher notes but were not directly surfaced in the audit's returned excerpt; they concern the audited public-dataset ecosystem, not the complete training corpus of a private model, and do not determine legal liability.[15]”

**URL:** https://arxiv.org/html/2412.17847v2

**Title/date check:** Retrieved title, “Bridging the Data Provenance Gap Across Text, Speech, and Video,” matches [15] and the registry. The page gives “Published: 2025-02-19,” matching registry date. The URL is the v2 HTML version specified in [15].

**Directly retrieved excerpt:** The abstract directly states: “Our manual analysis covers nearly 4000 public datasets between 1990-2024.” It also directly says “less than 33% of datasets are restrictively licensed” and “over 80% of the source content in widely-used text, speech, and video datasets, carry non-commercial restrictions.” The returned abstract excerpt does not directly surface 104 video datasets/33 tasks, 36%, or the repackaging detail. Researcher notes (`notes/evaluation_check.md`; `seed-notes/evaluation.md`) supply those as paper-specific evidence, quoting “104 video datasets, covering 33 popular video tasks” and “36% of video datasets have no license or intended use documentation”; the notes also describe restrictions being lost or obscured through dataset derivation/repackaging.

**Assessment:** Nearly 4,000 and the over-80%/less-than-one-third restriction comparison are directly supported by returned abstract text. The revised report transparently labels 104/33, 36%, and repackaging as evidence-note details and states they were not surfaced in the audit excerpt. Its ecosystem-level limitation avoids extrapolating to a private model’s entire training corpus. Note support is distinct from direct retrieval; the exact 104/33, 36%, and repackaging details are not independently confirmed by the returned excerpt in this audit.

Status: PASS

**Suggested correction:** No correction is required for transparency as written. Keep the explicit evidence-notes caveat. If the aim is a strictly excerpt-verified claim, remove or further qualify 104/33, 36%, and repackaging until relevant paper passages are directly retrieved. The abstract’s restriction figures need no such caveat.
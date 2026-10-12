1. **S1 — MAJOR**  
   **Manuscript text:** “*The causal target period starts on 1 October 2023 and is unaffected.*”  
   **What is wrong:** Literally, the target period is the post-policy period and therefore is not “unaffected.” The intended claim appears to be only that it contains no pre-commencement days or implementation-quarter overlap.  
   **Evidence:** `records/exact_estimand.json`, `period.basis`: the target period is “the first four complete statistical quarters after legal commencement.”  
   **Minimal correction:** Replace with: “The causal target period starts on 1 October 2023 and contains no pre-commencement days.”

2. **S2 — MINOR**  
   **Manuscript text:** Table 1: “*Counterfactual | None; the earlier period stands in for it*”  
   **What is wrong:** This is internally inconsistent. If the quantity is strictly descriptive, the earlier period is a comparator, not a counterfactual. Treating it as a stand-in for the no-policy outcome is precisely the unsupported causal assumption discussed later.  
   **Evidence:** `records/assumptions.json`, `assumption.wales-20mph.before-after-counterfactual.v1`, status `UNSUPPORTED`; `records/inferences.json`, `inference.wales-20mph.provisional-descriptive.v1`, claim ceiling.  
   **Minimal correction:** Replace with: “None; the earlier period is only the descriptive comparator.”

3. **S3 — MINOR**  
   **Manuscript text:** “*Later reversions to 30 mph alter membership over time.*”  
   **What is wrong:** The registered affected-road population is fixed by whether a segment changed on 17 September 2023. Later reversions do not alter membership in that estimand; they can alter treatment state and membership in the recorded 20/30 mph categories.  
   **Evidence:** `records/exact_estimand.json`, `population` and `exposure.operational_definition`; `records/adversarial_findings.json`, `omitted_mechanisms_considered`, later-reversions entry: “the exact estimand fixes membership at the 17 September 2023 default change.”  
   **Minimal correction:** Replace with: “Later reversions can alter recorded speed-category membership and treatment status over time, although the registered affected-road set is fixed by the 17 September 2023 change.”

4. **S4 — MAJOR**  
   **Manuscript text:** “*No confidence interval, identified set, minimum or maximum effect follows from this audit.*”  
   **What is wrong:** The blanket minimum/maximum statement overlooks restrictions inherent in the estimand’s count semantics. Casualty counts are non-negative integers; for a defined percentage estimand, \(P_{\mathcal A}^{0}\ge1\); and the observed post aggregate implies \(0\le P_{\mathcal A}^{1}\le1725\) if the decomposition consists of non-negative counts. Those support restrictions alone imply a lower limit of \(-100\%\) and a finite upper limit, even though no substantive empirical bounds were registered. The files establish only that no numerical bounds were registered or asserted, not that count semantics yield no mathematical extrema.  
   **Evidence:** `records/exact_estimand.json`, `outcome.operational_definition`, `contrast`, and `denominator`; `derived/analysis.json`, `observation_map.observed_output.aggregate_policy_post_count = 1725`; `analysis/specification.json`, `partial_identification.registered_bounds = []`.  
   **Minimal correction:** Replace with: “The audit registers no substantively informative empirical identified interval or sign restriction; the three witness values are not endpoints.”

5. **S5 — MAJOR**  
   **Manuscript text:** “*A causal reading of the 28% needs every load-bearing assumption in the table.*”  
   **What is wrong:** The table combines assumptions belonging to different possible identification routes. In particular, a raw before/after causal reading does not simultaneously require England’s proportional change to supply the Welsh counterfactual; that assumption belongs to an England-donor design. Conversely, an England-based design need not assume that the no-policy outcome exactly equals the preceding four quarters. Calling every listed assumption jointly necessary is a logical overstatement.  
   **Evidence:** `records/assumptions.json`: `before-after-counterfactual.v1` and `england-parallel-trends.v1` describe distinct counterfactual bridges; `records/sensitivity_results.json`, `sensitivity.wales-20mph.donor-pretrend.v1`, treats England as a separate donor diagnostic.  
   **Minimal correction:** Replace with: “Any causal reading requires an appropriate subset of load-bearing assumptions for the chosen design; the frozen corpus supports neither the direct before/after bridge nor the England-donor bridge.”

6. **S6 — MAJOR**  
   **Manuscript text:** “*A future version that aims at an estimate or an identified interval would need, at minimum:*” followed by all five listed requirements.  
   **What is wrong:** The records describe possible bridges and measurements, not a universally necessary conjunction. Realised speed, weather, enforcement, placebo dates, and prospective registration may be valuable for particular designs but are not established by the evidence as mathematically necessary for every possible point- or partial-identification design. This exceeds the recorded claim ceiling.  
   **Evidence:** `records/missingness.json`, each `could_resolve_with` field presents alternatives rather than universal requirements; `records/identification_status.json`, `scope`, expressly allows “a future design with a historical treatment map or newly justified restrictions”; `records/inferences.json`, `inference.wales-20mph.no-partial-bound.v1`, permits “additional externally justified restrictions.”  
   **Minimal correction:** Replace “would need, at minimum” with “could require, depending on the design,” and present the items as examples of possible bridges.

7. **S7 — MINOR**  
   **Manuscript text:** “*Adding more aggregate quarters, or an England series alone, would leave the observation-map failure intact.*”  
   **What is wrong:** “Alone” makes the England qualification defensible, but the first clause is too categorical unless it also excludes newly justified temporal restrictions. Additional quarters combined with a registered trend or structural model could change identification; the records only say that additional unrestricted aggregate observations do not themselves reveal treatment membership or the counterfactual.  
   **Evidence:** `records/missingness.json`, `missing.wales-20mph.counterfactual-series.v1`, `could_resolve_with`; `records/identification_status.json`, `scope`; `records/inferences.json`, `inference.wales-20mph.no-partial-bound.v1`, scope.  
   **Minimal correction:** Replace with: “Adding aggregate quarters or an England series without a justified treatment map and counterfactual restriction would leave the registered gaps intact.”

8. **S8 — MAJOR**  
   **Manuscript text:** “*Version 1.1.0 adds this manuscript to the evidence package published as version 1.0.0 … The scientific records, frozen sources and derived tables are unchanged.*”  
   **What is wrong:** The bundle contains metadata and assurance records for version 1.0.0 and producer replay summaries, but no version-1.1.0 archive metadata, manifest, package inventory, or checksum record establishing what version 1.1.0 contains or that all scientific files are unchanged.  
   **Evidence:** Zenodo record `21894035`, `version = wales-20mph-1.0.0`; live `paper.json`, availability note for v1.0.0; no supporting file for a v1.1.0 package.  
   **Minimal correction:** State only that the manuscript is intended for a prospective v1.1.0 package, unless a versioned manifest is supplied.

9. **S9 — NOTE**  
   **Manuscript text:** “*Version 1.1.0 archiving is pending.*”  
   **What is wrong:** No admissible record explicitly registers the archival state of version 1.1.0. The available archive record concerns only version 1.0.0.  
   **Evidence:** Zenodo record `21894035`, `version`; no supporting file for v1.1.0 archival status.  
   **Minimal correction:** Replace with: “No version 1.1.0 archive record is included in this evidence bundle.”

10. **S10 — MAJOR**  
    **Manuscript text:** “*the round-four report recommended `READY` with no unresolved critical finding, and all six findings raised across the rounds are recorded as resolved*”  
    **What is wrong:** The selected round-four report does contain `recommendation: READY`, but the live review-history record labels round four `REVISION_REQUESTED`. Presenting only the recommendation suppresses a material inconsistency in the assurance records.  
    **Evidence:** `reviews/fable-round-4/report.json`, `recommendation = READY`, `unresolved_critical_count = 0`; `records/adversarial_findings.json`, `review_history`, `review.wales-20mph.fable-round-4.v1`, `disposition = REVISION_REQUESTED`.  
    **Minimal correction:** Add: “The report’s recommendation is `READY`, although the consolidated review-history field records the round-four disposition as `REVISION_REQUESTED`.”

11. **S11 — MAJOR**  
    **Manuscript text:** “*This manuscript was additionally given to a second vendor's model (OpenAI, `gpt-5.6-sol`) …; its findings and their dispositions are retained with the version 1.1.0 package.*”  
    **What is wrong:** No supplied record identifies that model, documents such a review, contains its findings or dispositions, or establishes their retention in a version 1.1.0 package.  
    **Evidence:** No supporting file.  
    **Minimal correction:** Delete the sentence unless the model-review record and versioned package manifest are added to the admissible bundle.

12. **S12 — MAJOR**  
    **Manuscript text:** “*This manuscript was drafted by an AI agent (Anthropic Claude) from the frozen records*”  
    **What is wrong:** The live provenance record names the OpenAI Codex agent team and the Anthropic Fable read-only review workflow, but it does not record Anthropic Claude as the manuscript drafter. No version-1.1 provenance record supports this attribution.  
    **Evidence:** Live `paper.json`, `provenance.generatedBy` and `provenance.disclosure`; no supporting v1.1 provenance file.  
    **Minimal correction:** Replace with the provenance actually recorded, or qualify: “The supplied evidence does not contain a versioned record of the manuscript-drafting model.”

13. **S13 — MINOR**  
    **Manuscript text:** “*The scholarly author line is ‘Anonymous’.*”  
    **What is wrong:** As a description of the displayed byline this is tautologically true, but it is not the creator identity recorded for the archived release with the same title. The Zenodo and live-page records name Ian Pitchford and the OpenAI Codex agent team, with Ian Pitchford identified as the human scholarly creator. The manuscript does not explain whether “Anonymous” is merely a review byline or a replacement attribution.  
    **Evidence:** Zenodo record `21894035`, `creators`; live `paper.json`, `authors`, `provenance.humanRole`, and `attributionBoundary`.  
    **Minimal correction:** State: “The manuscript uses an anonymous review byline; the archived v1.0.0 release credits Ian Pitchford and the OpenAI Codex agent team.”

14. **S14 — MAJOR**  
    **Manuscript text:** “*The identification-before-estimation procedure follows the earlier Evidence Press release Stocks Are Not Flows, which applies the same discipline to a different policy question.*”  
    **What is wrong:** The admissible evidence supplies only that work’s title, URL, and related-work listing. It does not document its procedure or establish that it applies “the same discipline.”  
    **Evidence:** Live `paper.json`, `relatedWorks` entry for *Stocks Are Not Flows*; no frozen source or method record for that release.  
    **Minimal correction:** Replace with: “The live release page lists *Stocks Are Not Flows* as related work; no methodological comparison is established in this bundle.”

15. **S15 — MAJOR**  
    **Manuscript text:** “*Repository: … tag `v1.0.0` at commit `7ea482fa82fd2330db6383c249aba0d43ac4bea4` (packaged release source).*”  
    **What is wrong:** None of the supplied records binds tag `v1.0.0` to that commit. The attestation identifies reviewed and replayed commits, and the final receipt identifies the case commit, but not this tag-to-commit assertion.  
    **Evidence:** `attestations/clean-replay-evidence/attestation.json`, `reviewed_commit` and `replayed_commit`; `records/final_receipt.json`, `case_commit`; no supporting file for commit `7ea482…`.  
    **Minimal correction:** Remove the tag-to-commit hash or cite a supplied signed/ref manifest that establishes it.

16. **S16 — MINOR**  
    **Manuscript text:** “*Git, uv and Python 3.11 or later.*”  
    **What is wrong:** The replay attestation records commands and the `uv.lock` digest but does not state a Python 3.11-or-later requirement.  
    **Evidence:** `attestations/clean-replay-evidence/attestation.json`, `commands` and `uv_lock_sha256`; no supporting field for the Python version requirement.  
    **Minimal correction:** Omit the Python-version claim or cite a supplied project configuration that declares it.

17. **S17 — MINOR**  
    **Manuscript text:** “*Replay needs no network once the environment is synchronised.*”  
    **What is wrong:** The evidence establishes that specified producer commands were run with an offline policy; it does not establish the broader portability claim that every replay needs no network after synchronisation in an independently recreated environment.  
    **Evidence:** `records/final_receipt.json`, `replay.network_policy = OFFLINE_REQUIRED`; `attestations/clean-replay-evidence/attestation.json`, offline command vectors; live `paper.json`, data/environment state `partial`.  
    **Minimal correction:** Replace with: “The recorded producer replay used offline command vectors after its environment had been prepared.”

18. **S18 — MAJOR**  
    **Manuscript text:** “*Every command above … was rerun on a fresh clone of tag `v1.0.0` … All exited with status zero*”  
    **What is wrong:** The supplied 12 October summary reports selected outputs and exit information, but does not document a fresh clone, identify the resolved tag commit, or provide per-command logs for every listed command.  
    **Evidence:** “Producer replay logs 2026-10-12 (summary)”; no fresh-clone record or complete per-command log in the bundle.  
    **Minimal correction:** Replace with: “The supplied producer summary reports successful validation, citation, table, test, optimized-control and lifecycle outputs on 12 October 2026.”

19. **S19 — MINOR**  
    **Manuscript text:** “*the table check passes and the five derived artifacts keep their registered digests*”  
    **What is wrong:** The supplied replay summary says only “OK deterministic Wales 20 mph derived artifacts”; it does not enumerate five artifacts or provide their registered and rerun digests.  
    **Evidence:** Producer replay logs 2026-10-12, `tables-check.txt`; no supporting five-artifact digest table.  
    **Minimal correction:** Replace with: “The deterministic table check reported `OK`.”

20. **S20 — MAJOR**  
    **Manuscript text:** “*Figure 1 is generated by `figures/make_figure1.py`, which refuses any input other than the registered `derived/quarterly_event_series.csv`*”  
    **What is wrong:** The figure script is not included in the admissible evidence bundle, so neither its existence nor its input-refusal behaviour can be verified.  
    **Evidence:** No supporting file.  
    **Minimal correction:** Delete the behavioural claim or include the script and its registered digest in the evidence bundle.

21. **S21 — MINOR**  
    **Manuscript text:** “*Later verification of those summaries depends on continued access to the commit-pinned upstream files.*”  
    **What is wrong:** The records say verification depends on continued access to the recorded public URLs **and immutable Git objects**. The manuscript’s wording is narrower and may imply that the files themselves were frozen in the package, which they were not.  
    **Evidence:** `frozen_sources/evidence-press-apep-prior-art-audit-2026-08-11.txt`, “not an independently frozen copy”; `records/corpus_boundary.json`, `known_blind_spots`; `records/source_provenance.json`, APEP entries.  
    **Minimal correction:** Replace with: “Later primary-source verification depends on continued availability of the recorded public URLs and immutable upstream Git objects; the paper bodies are not frozen here.”

---
title: "Wales 20 mph Casualty Attribution Audit: A Constructive Non-Identification Result"
subtitle: "Manuscript for version 1.1.0 of the Evidence Press release"
author: "Anonymous"
date: "Manuscript prepared 12 October 2026"
abstract: |
  On 17 September 2023 the default speed limit on restricted roads in Wales fell from 30 mph to 20 mph. A provisional Welsh Government release later reported that casualties on roads recorded as 20 or 30 mph were 28% lower in 2023 Q4 to 2024 Q3 than in the preceding four quarters. This paper audits the claim that the policy caused that fall, using a corpus of 25 registered official and bibliographic sources frozen on 11 August 2026. The headline is reproducible as a description: the reconstructed provisional totals are 2,402 and 1,725 casualties, an exact change of $-33850/1201$ per cent (about $-28.18\%$). Later frozen vintages of the same comparison give about $-26.10\%$ (StatsWales) and $-24.18\%$ (Department for Transport collision rows). The registered causal estimand is a different object: the percentage effect of the policy on police-recorded casualties on the road segments whose limit actually changed, relative to those segments' no-policy outcome over the same year. A constructive witness exhibits three hypothetical worlds that reproduce the observed aggregates exactly yet imply affected-road effects of $-50\%$, $0\%$ and $+100\%$. Within the frozen evidence and the admitted rival set, neither the effect nor its sign is identified, and no finite bound is registered. The result does not show that the policy succeeded or failed; it states what the published aggregates cannot settle and which measurements a causal estimate would need.
---

\statusbox{Status: unrefereed candidate. Version 1.1.0 adds this manuscript to the evidence package published as version 1.0.0 on 11 August 2026 (DOI \href{https://doi.org/10.5281/zenodo.21894035}{10.5281/zenodo.21894035}; concept DOI \href{https://doi.org/10.5281/zenodo.21894034}{10.5281/zenodo.21894034}). The scientific records, frozen sources and derived tables are unchanged. Producer-side replay passes; no independent rerun, independent reimplementation, formal verification, external specialist review or editorial peer review has been established.}

# Question and policy context

The Restricted Roads (20 mph Speed Limit) (Wales) Order 2022 came into force on 17 September 2023. It reduced the general speed limit for restricted roads in Wales from 30 mph to 20 mph [`source.legislation.wsi-2022-800.v1`]. Highway authorities could retain 30 mph limits on particular restricted roads under published guidance [`source.wg.30mph-exception-guidance.v1`], and the final 2024 casualty bulletin states that most, but not all, roads previously at 30 mph changed [`source.wg.road-casualties-2024-final.v1`].

On 30 January 2025 the Welsh Government's provisional release for July to September 2024 stated that, in the 12 months from 2023 Q4 to 2024 Q3, casualties on 20 and 30 mph roads combined were 28% lower than in the same period a year before [`source.wg.q3-2024-provisional.v1`]. The same release describes the combined series as having generally declined over the previous decade. Its accompanying Figure 4 plots the quarterly series [`source.wg.figure4-quarterly-casualties.v1`].

The claim audited here is the causal reading of that statistic:

> The Welsh default 20 mph limit caused the reported 28% fall in casualties on 20 and 30 mph roads in its first year.

The claim is recorded as a candidate, not an endorsed result (`records/candidate_claim.json`). The audit does not ask whether the policy worked. It asks whether the frozen evidence identifies the causal quantity that the sentence implies. The Office for Statistics Regulation has already cautioned users about causal statements on this policy, noting that traffic volume and weather, among other factors, may affect findings [`source.osr.20mph-guidance-2026.v1`]. This paper turns that general caution into a specific, checkable statement about one estimand and one corpus.

The contributions are three, each limited to the registered case:

1. an exact reconstruction of the provisional first-year comparison and its reconciliation with two later frozen data vintages (Section \ref{descriptive-replay-and-vintage-reconciliation});
2. a separation of the published combined 20/30 mph proxy from a registered affected-road causal estimand (Section \ref{the-claim-and-the-exact-estimand}); and
3. a constructive witness showing that, for that estimand, the frozen aggregate evidence recovers neither the point value nor the sign of the effect (Section \ref{identification-argument-and-the-constructive-result}).

None of the underlying ideas is new. Before/after differences are not causal effects, counterfactual outcomes are unobserved, and observationally equivalent worlds establish non-identification. The bounded novelty audit classifies the case as partly novel only in the sense of a case-specific bridge (Section \ref{related-work}).

# The claim and the exact estimand

## Two quantities

The audit keeps two quantities apart.

The **descriptive source statistic** is the percentage change in police-recorded casualties on all Welsh roads recorded as 20 mph or 30 mph, comparing 2023 Q4 to 2024 Q3 with 2022 Q4 to 2023 Q3.

The **registered causal estimand** is fixed in `records/exact_estimand.json` with semantic status `EXACT`. Its population is people killed or injured in police-recorded personal-injury collisions on Welsh road segments whose default restricted-road limit actually changed from 30 mph to 20 mph on 17 September 2023. The outcome is the count of such casualties under the official STATS19 casualty definition, aggregated over all severities and road-user types. The period is the first four complete statistical quarters after commencement, 2023 Q4 to 2024 Q3.

Write $\mathcal{A}$ for the set of affected segments, $Y_{\mathcal{A}}(1)$ for the casualty count on $\mathcal{A}$ in the target period under the implemented policy, and $Y_{\mathcal{A}}(0)$ for the count on the same segments in the same period without the default change. The estimand is

$$
\theta \;=\; 100\times\frac{Y_{\mathcal{A}}(1)-Y_{\mathcal{A}}(0)}{Y_{\mathcal{A}}(0)},
$$

a percentage change in a total count. Traffic exposure is not its denominator. Exposure would be needed for a different estimand, such as casualties per vehicle kilometre, and for separating risk changes from diversion.

Table 1 sets the two quantities side by side.

: Descriptive statistic and registered estimand.

| | Descriptive source statistic | Registered causal estimand $\theta$ |
|:----------------|:------------------------------------------|:------------------------------------------|
| Population | All casualties on roads recorded as 20 or 30 mph | Casualties on segments whose limit changed from 30 to 20 mph |
| Contrast | 2023 Q4--2024 Q3 against the preceding four quarters | Policy outcome against the same segments' no-policy outcome, same period |
| Counterfactual | None; the earlier period stands in for it | $Y_{\mathcal{A}}(0)$, unobserved |
| What it can support | A vintage-specific before/after description | A causal effect, if membership and counterfactual are identified |

## The implementation quarter

The descriptive baseline 2022 Q4 to 2023 Q3 is a whole-quarter reporting bin. Because the Order came into force on 17 September 2023, the bin includes the 14 calendar days from 17 to 30 September 2023. The baseline is therefore not wholly untreated. The analysis specification derives this overlap from the commencement date and the quarter boundary, and the replay checks it (`analysis/specification.json`, `windows.first_year.boundary_note`). The causal target period starts on 1 October 2023 and is unaffected.

## Why the proxy is not the target

The combined 20/30 mph aggregate is defined by the speed limit recorded for each collision, over all roads. The target is defined by policy-induced change on particular segments. The two sets differ in at least three ways recorded in the corpus. The aggregate includes roads that were already 20 mph before the policy. It includes roads retained at 30 mph as exceptions, and the final 2024 bulletin confirms that not every 30 mph road changed. Later reversions to 30 mph alter membership over time. The assumption that the aggregate equals the affected-road population (`assumption.wales-20mph.aggregate-proxy-equivalence.v1`) is recorded as `REFUTED`.

The corpus does not contain the object that would bridge the two: a versioned historical segment map showing which roads changed on 17 September 2023, which kept 30 mph, which later reverted, and how each collision location maps to that history (`missing.wales-20mph.treated-segment-map.v1`, severity `BLOCKING`). The live DataMapWales map was inspected as a discovery route but no redistributable historical segment table was found (`records/corpus_boundary.json`, `inaccessible_material`).

# Data and frozen corpus

## Corpus boundary

The case was registered at 2026-08-11T09:24:28Z. The official-source corpus closed at 09:45:00Z and the full boundary, including the novelty audit, was frozen at 12:47:03Z the same day (`records/corpus_boundary.json`). The boundary registers 25 sources and three frozen search records. Each source record carries its URL, retrieval time, SHA-256 digest, byte size, media type, licence and redistribution basis (`records/source_provenance.json`), and the frozen bytes are listed in `frozen_sources/MANIFEST.sha256`. Appendix B lists every source by registered identifier.

The sources fall into five groups.

- **Welsh Government releases.** The provisional July to September 2024 release and its Figure 4 SVG; the final 2023, 2024 and 2025 collision and casualty bulletins; the quality report; the 2024 road traffic release; the 30 mph exception guidance; and the copyright statement.
- **StatsWales extracts.** Two filtered exports of the dataset of police-recorded casualties by speed limit and severity: a 2015 Q1 to 2026 Q1 series and a 2022 Q4 to 2024 Q3 claim-window extract, together with the dataset metadata. The two exports are registered as distinct sources because their bytes and query settings differ.
- **Department for Transport open data.** Annual collision files for 2021 to 2025, the 2025 data guide used to decode coded fields, and the open-data landing page.
- **Legislation.** The 2022 Order as published on legislation.gov.uk.
- **Novelty and guidance.** The Office for Statistics Regulation 20 mph guidance and its copyright page, and three CC0 Evidence Press bibliographic audit records of directly overlapping working papers (Section \ref{related-work}).

Official sources are reused under the Open Government Licence v3.0, subject to the attribution and exclusion terms recorded per source. The three bibliographic audit records are CC0 and reproduce no third-party paper text.

## Exclusions and blind spots

Several relevant materials lie outside the boundary (`records/corpus_boundary.json`, `excluded_material`). A Transport for Wales monitoring report was located but not redistributed because its reuse terms conflict. GoSafe enforcement timelines were located but not frozen. The Department for Transport vehicle and casualty-person files were not admitted; casualty counts from that route are the `number_of_casualties` field summed over collision rows. Weather series, road-level traffic counts, local traffic orders, a complete record of later reversions and academic evaluations beyond three working papers are also absent. The corpus contains no official traffic-volume series by 20 mph versus 30 mph class; the 2024 bulletin states that no such source is available [`source.wg.road-casualties-2024-final.v1`].

## Extraction rules

The analysis specification (`analysis/specification.json`) fixes each extraction route.

- **Provisional figure.** The quarterly values in Figure 4 are reconstructed deterministically from the SVG vector coordinates, calibrated against nine grid lines with a 200-casualty tick increment. The reconstruction recovers 59 quarterly points from 2010 Q1 to 2024 Q3; the maximum grid-fit residual and maximum point-rounding residual are both below the registered tolerance of 1/100 casualty (`derived/measurement_audit.csv`).
- **StatsWales.** Both extracts are filtered to Wales, all roads, number of casualties, all severities and all users, at 20 mph and 30 mph. Over 2022 Q4 to 2024 Q3 the two extracts agree in every cell. One quarter of the long series, 2026 Q1, is flagged provisional.
- **Department for Transport.** Rows are selected by police force (codes 60 to 63 for Wales; the registered list of 39 force codes for England) and by recorded speed limit 20 or 30 mph. Across the five annual files, 513,801 collision rows were parsed with no duplicate collision index.

All arithmetic uses exact rational numbers (Python `fractions.Fraction`) with the percentage change defined as $100\,(P-B)/B$. The 17 registered calculations in `records/observations.json` are replayed and must match their stored values exactly.

# Descriptive replay and vintage reconciliation

The provisional figure reconstructs to 2,402 casualties in 2022 Q4 to 2023 Q3 and 1,725 in 2023 Q4 to 2024 Q3. The exact change is

$$
100\times\frac{1725-2402}{2402} \;=\; -\frac{33850}{1201}\,\% \;\approx\; -28.184846\%,
$$

which rounds to the published "28% lower". The historical headline is therefore reproducible from the frozen figure (`inference.wales-20mph.provisional-descriptive.v1`).

The same nominal comparison is not invariant across later frozen routes. Table 2 gives the three values (`derived/vintage_reconciliation.csv`).

: The first-year comparison in three frozen official routes. Casualties on roads recorded as 20 or 30 mph in Wales; baseline 2022 Q4--2023 Q3, post-period 2023 Q4--2024 Q3.

| Frozen route | Baseline | Post | Exact change (%) | Approx. (%) |
|:----------------------------------------------|---------:|---------:|--------------:|----------:|
| Provisional Welsh Government figure (SVG reconstruction) | 2,402 | 1,725 | $-33850/1201$ | $-28.18$ |
| Current StatsWales extract | 2,402 | 1,775 | $-31350/1201$ | $-26.10$ |
| Current DfT collision rows (summed casualties) | 2,395 | 1,816 | $-11580/479$ | $-24.18$ |

The StatsWales post-period total is 50 casualties above the provisional reconstruction; the DfT route differs in both totals. The assumption that the three routes encode one identical contrast (`assumption.wales-20mph.source-vintage-equivalence.v1`) is recorded as `REFUTED`. The audit does not diagnose which revision or processing difference produces each discrepancy, and it does not choose among the routes by proximity to the headline. The DfT figure is an unreconciled diagnostic, not an independent replication. All three are descriptions; none is a causal estimate (`sensitivity.wales-20mph.source-vintage.v1`).

Figure 1 plots the frozen derived quarterly table. Panel (a) shows the three routes. Panel (b) splits the current StatsWales series by recorded speed limit. The recorded 20 mph and 30 mph counts change abruptly between 2023 Q3 and 2023 Q4, while the combined series continues. The split records the speed limit attached to each collision; it does not record whether that road segment changed treatment status, so it cannot be used to recover $\mathcal{A}$.

![Quarterly police-recorded casualties on roads recorded as 20 or 30 mph in Wales, plotted directly from the frozen derived table *derived/quarterly_event_series.csv*. Pale grey: descriptive baseline 2022 Q4--2023 Q3; darker grey: implementation quarter 2023 Q3 (commencement 17 September 2023); blue: first post-policy year 2023 Q4--2024 Q3. The figure is descriptive and carries no causal interpretation.](figures/figure1.pdf){width=96%}

For context, the corpus also contains later descriptive material. The frozen 2025 DfT file gives 1,820 casualties on Welsh 20/30 mph roads in calendar 2025 (`observation.wales-20mph.dft-2025-combined-total.v1`). The final Welsh Government 2025 bulletin reports 1,469 collisions on those roads in 2025, 2% more than in 2024 and 22% fewer than in 2022, and warns that fewer than three post-policy years are available and that the longer series was already declining [`source.wg.road-collisions-casualties-2025-final.v1`]. These figures do not enter the identification argument.

# Identification argument and the constructive result

## The observation map

Identification asks whether every data-generating world consistent with the evidence, assumptions and admitted rivals assigns the same value to the estimand (`docs/IDENTIFICATION_MODEL.md`). The available evidence for the first-year comparison is the pair of aggregate counts

$$
(B,\,P) \;=\; (2402,\;1725),
$$

the baseline and post-period totals on roads recorded as 20 or 30 mph. A structural world specifies, among other things, the split of each total between affected segments and other 20/30 mph roads, and the affected-road counts with and without the policy. Write $B_{\mathcal{A}}, B_{\mathcal{O}}$ for the baseline split, $P_{\mathcal{A}}^{1}$ for the affected-road post count under the policy, $P_{\mathcal{A}}^{0}$ for the affected-road post count without it, and $P_{\mathcal{O}}$ for the other-road post count. The observation map sends a world to

$$
\Phi(w) \;=\; \bigl(B_{\mathcal{A}}+B_{\mathcal{O}},\; P_{\mathcal{A}}^{1}+P_{\mathcal{O}}\bigr),
$$

and the estimand evaluated in that world is $\theta(w) = 100\,(P_{\mathcal{A}}^{1}-P_{\mathcal{A}}^{0})/P_{\mathcal{A}}^{0}$. The quantity $P_{\mathcal{A}}^{0}$ never enters $\Phi$. The admitted model class imposes no restriction tying it to observed quantities: no validated comparison series, trend model, or bound on membership, ascertainment, classification or exposure is registered (`analysis/specification.json`, `partial_identification.registered_bounds` is empty).

## The witness

**Proposition (constructive non-identification).** Within the registered corpus and admitted model class, the observed aggregates $(B,P)=(2402,1725)$ are compatible with affected-road effects $\theta=-50\%$, $\theta=0\%$ and $\theta=+100\%$. Hence $\theta$ is not point-identified and its sign is not identified.

*Proof.* Fix the hypothetical decomposition $B_{\mathcal{A}}=2000$, $B_{\mathcal{O}}=402$, $P_{\mathcal{A}}^{1}=1000$ and $P_{\mathcal{O}}=725$, so that $\Phi(w)=(2000+402,\;1000+725)=(2402,1725)$ in every world below. Vary only the unobserved $P_{\mathcal{A}}^{0}$ as in Table 3. Each world reproduces the observed pair, and the implied effects are negative, zero and positive. $\square$

: The three hypothetical worlds (`derived/analysis.json`, `constructive_nonidentification_witness`). None is asserted to be true.

| World | $B_{\mathcal{A}}+B_{\mathcal{O}}$ | $P_{\mathcal{A}}^{1}+P_{\mathcal{O}}$ | $P_{\mathcal{A}}^{0}$ | $\theta$ |
|:----------------------|----------------:|----------------:|----------------:|------------:|
| B: negative effect | $2000+402$ | $1000+725$ | 2,000 | $-50\%$ |
| A: zero effect | $2000+402$ | $1000+725$ | 1,000 | $0\%$ |
| C: positive effect | $2000+402$ | $1000+725$ | 500 | $+100\%$ |

The witness is machine-checked: `tools/build_wales_20mph_tables.py check` recomputes the worlds and verifies that all three yield the same observed output, the stated effects and the sign set {negative, zero, positive} (`records/identification_status.json`, `witness.result` = `PASS`).

## What the witness shows and what it does not

Four points bound the reading of the proposition.

*The worlds are counterexamples, not estimates.* The values 2,000, 1,000 and 500 for $P_{\mathcal{A}}^{0}$, and the decomposition 2,000/402 and 1,000/725, are illustrative. No claim is made that any world is true, that affected roads carried 2,000 baseline casualties, or that the true effect lies near any of the three values.

*They are not bounds.* The three effects are not endpoints of an identified interval. The specification registers no bounds and the analysis artifact reports `NOT_BOUNDED` (`inference.wales-20mph.no-partial-bound.v1`). No confidence interval, identified set, minimum or maximum effect follows from this audit.

*The failure is not only a membership problem.* All three worlds share the same decomposition of each total into affected and other roads. Observing that decomposition would therefore not, on its own, identify $\theta$; the binding gap is the absent counterfactual $P_{\mathcal{A}}^{0}$ (`missing.wales-20mph.counterfactual-series.v1`). Missing segment membership is a second, separate gap: without it the reported aggregate does not even instantiate the affected-road outcome (`inference.wales-20mph.proxy-mismatch.v1`).

*The result is relative to the corpus and the model class.* A different evidence state could change it: a historical treatment map, collision locations linked to it, a defensible comparison design, or externally justified restrictions. The proposition says nothing about such designs.

The analysis artifact also records a simpler aggregate illustration. Treating the whole 20/30 mph aggregate as if it were the target, a world with no policy effect and a secular change of $-33850/1201\,\%$, and a world with no secular change and a policy effect of $-33850/1201\,\%$, both produce $(2402,1725)$. That illustration shows why a before/after difference cannot be read as an effect, but it is the affected-road witness above that bears on the registered estimand.

## The before/after assumption

Reading the 28% as the effect requires that, without the policy, first-year casualties on affected segments would have equalled the preceding four quarters (`assumption.wales-20mph.before-after-counterfactual.v1`). The assumption is recorded as `UNSUPPORTED`. It cannot be tested directly in the post-period. The source release itself describes a decade of general decline in the combined series, and the pre-period diagnostic in Section \ref{diagnostics} moves in the opposite direction from the England series. Once secular change is admitted, the before/after contrast no longer determines a causal effect.

# Diagnostics

The diagnostics below are falsification pressure on the assumptions a causal reading would need. None is a causal estimate, and none is used to select an estimator.

## England as a comparison series

The DfT collision rows allow the same four-quarter comparison for England (`derived/falsification_diagnostics.csv`). Table 4 reports it for the first-year window and for the immediately preceding window.

: Wales and England, DfT route, casualties on roads recorded as 20 or 30 mph. Percentage-point differentials are Wales minus England.

| Window | Wales | Wales (%) | England | England (%) | Diff. (pp) |
|:------------------------|----------------:|---------:|-------------------:|-----------:|---------:|
| 2022 Q4--2023 Q3 to 2023 Q4--2024 Q3 | 2,395 → 1,816 | $-24.18$ | 81,226 → 78,132 | $-3.81$ | $-20.37$ |
| 2021 Q4--2022 Q3 to 2022 Q4--2023 Q3 | 2,269 → 2,395 | $+5.55$ | 84,288 → 81,226 | $-3.63$ | $+9.19$ |

The exact differentials are $-23305720/1144331$ and $+219599575/23906184$ percentage points. In the earlier window Wales rose while England fell; in the first-year window Wales fell much further than England. The current StatsWales series gives a Wales change of $+5.86\%$ ($2{,}269 \to 2{,}402$) over the same earlier window.

Two cautions apply. The later window of the earlier comparison ends in 2023 Q3 and so contains the 14 post-implementation days; it is a pre-period diagnostic, not a literal pre-policy placebo. And the reversal does not refute every conditional comparison design. What it shows is that the corpus gives no support for assuming that England's proportional change supplies the Welsh no-policy change (`assumption.wales-20mph.england-parallel-trends.v1`, `UNSUPPORTED`). England has not been validated as a donor for parallel trends, stable composition, absence of interference or policy non-contamination (`sensitivity.wales-20mph.donor-pretrend.v1`).

## Outcome scope

The Wales-minus-England differential depends on what is counted (Table 5; `inference.wales-20mph.outcome-diagnostics.v1`).

: First-year Wales-minus-England differentials by outcome scope, DfT route.

| Outcome | Wales (%) | England (%) | Diff. (pp) |
|:----------------------------------------------|------------:|------------:|------------:|
| Casualties, roads recorded 20/30 mph | $-24.18$ | $-3.81$ | $-20.37$ |
| Collisions, roads recorded 20/30 mph | $-22.25$ | $-3.59$ | $-18.66$ |
| Casualties, roads recorded 40 mph or above | $+1.71$ | $-2.64$ | $+4.35$ |
| Casualties, all recorded speed limits | $-11.88$ | $-3.41$ | $-8.47$ |

The pattern neither validates nor refutes a policy mechanism. It shows that the apparent differential is sensitive to outcome and scope, and it supplies no per-exposure effect.

## Measurement audit

The corpus documents several measurement problems for the series in question.

- **Speed-limit coding corrections.** About 120 collisions recorded on 20 or 30 mph roads between 17 September and 31 December 2023 had inconsistent recorded limits and were corrected manually after local-authority confirmation. They are described as about 25% of collisions on those roads in that partial post-policy period. Historical inconsistencies were identified and not amended [`source.wg.road-collisions-2023.v1`]. The assumption of stable speed classification (`assumption.wales-20mph.stable-speed-classification.v1`) is recorded as `REFUTED`. The corrections span both the last 14 days of 2023 Q3 and 2023 Q4 and are not reported separately for the two quarters.
- **Under-coverage.** Police data omit unreported incidents, and the quality report warns that short-term trends can be affected by recording practice and road-user reporting [`source.wg.road-collision-quality-report.v1`]. Stable ascertainment across periods is `UNSUPPORTED`.
- **Injury-based reporting.** Dyfed-Powys Police moved to an injury-based reporting system in May 2023. The quality report states that this changes the serious-versus-slight classification but not total collisions or casualties; the audit records that statement as `SUPPORTED` and auxiliary. In the frozen DfT files the number of selected Welsh 20/30 mph collision rows flagged as injury-based reports is 1 in 2022, 232 in 2023, 326 in 2024 and 421 in 2025 (`derived/measurement_audit.csv`).
- **Exposure.** No official traffic series by speed-limit class exists. Aggregate Welsh road traffic in 2024 was 1.3% above 2023, at 30.2 billion vehicle kilometres [`source.wg.road-traffic-2024.v1`]; that all-road figure does not measure exposure on affected segments.

These items limit any empirical interpretation of the aggregate series. They do not defeat the constructive result, which holds whatever the measurement quality of $(B,P)$.

## Sensitivity of the determination

The registered sensitivity analyses vary the source vintage, the donor window and the outcome scope (`records/sensitivity_results.json`). Every variant leaves the determination at `NON_IDENTIFIED`, because none observes affected-road membership or the no-policy outcome.

# Rival mechanisms and assumptions

Identification is always relative to an admitted set of rival explanations. Seven are admitted, and none is excluded by the corpus (`records/rival_mechanisms.json`; the identification record lists the same seven, with set parity enforced by a validator).

: Admitted rival mechanisms.

| Rival | Why it is not excluded |
|:----------------------------------------|:--------------------------------------------------|
| Secular trend and regression to the mean | Official long-run decline; divergent pre-period diagnostic |
| Traffic volume and composition | Only an all-Wales, all-road annual traffic change is available |
| Reporting, coding or road classification | Manual corrections, unamended inconsistencies, under-coverage, cross-vintage differences |
| Weather and seasonality | Matching quarter labels does not remove year-specific weather |
| Enforcement and concurrent interventions | No segment-period intervention history is frozen |
| Implementation-quarter contamination and anticipation | Whole-quarter data cannot separate 17--30 September 2023; no anticipation-period series |
| Reclassification, local exceptions and spillover | Aggregate scope is not the affected population; no historical membership panel |

The rival set is declared non-exhaustive: absence of another documented rival is not evidence that none exists. The external-model review rounds recorded nine candidate omitted mechanisms, including the implementation-quarter rival later admitted, post-pandemic travel recovery, fuel and living costs, provisional-data late returns, fleet and demographic drift, and later partial reversions, and each is disposed of as covered by an admitted rival (`records/adversarial_findings.json`, `omitted_mechanisms_considered`).

Table 7 lists the registered assumptions and their recorded status (`records/assumptions.json`).

: Registered assumptions.

| Assumption | Role | Status |
|:------------------------------------------------------------|:----------------|:------------|
| Combined 20/30 mph aggregate equals the affected-road population | Load-bearing | Refuted |
| No-policy first year equals the preceding four quarters | Load-bearing | Unsupported |
| England's proportional change supplies the Welsh no-policy change | Load-bearing | Unsupported |
| Speed-limit classification stable across windows | Load-bearing | Refuted |
| Police ascertainment stable across periods | Load-bearing | Unsupported |
| No concurrent intervention changed differentially with the rollout | Load-bearing | Unsupported |
| Injury-based reporting leaves total counts unchanged | Auxiliary | Supported |
| Provisional, StatsWales and DfT routes encode one contrast | Auxiliary | Refuted |
| No exposure displacement between policy and no-policy states | Sensitivity only | Unsupported |

A causal reading of the 28% needs every load-bearing assumption in the table. Two are refuted and four are unsupported in the frozen corpus.

# What the result does and does not say

The result says three things. The provisional 28% figure is a reproducible description of one data vintage. Later official vintages give smaller descriptive falls of about 26.1% and 24.2%. And within the frozen aggregate evidence and the admitted rival set, the causal effect of the policy on affected roads is not identified, and neither is its sign. The positive 28% attribution therefore remains unsupported by this evidence. That is the full claim ceiling recorded in `records/identification_status.json`.

The result does not say any of the following.

- That the policy failed, succeeded or had no effect. Non-identification is not evidence of a zero effect.
- That the effect was negative, zero, positive, 28% or any other magnitude.
- That $-50\%$, $0\%$ and $+100\%$ are estimates, bounds or plausible values.
- That every future design is non-identified. A treatment map, linked locations and justified restrictions could identify the effect or bound it.
- That earlier causal evaluations are right or wrong. They are cited as prior work, not adjudicated.
- Anything about risk per journey, displacement, realised speeds, welfare, distribution, implementation quality or whether the policy should be kept, changed or reversed.

# Limitations

**Corpus scope.** The corpus is predominantly official producer material frozen on one day. It is not a systematic review of the academic literature, and it excludes enforcement timelines, weather data, road-level traffic counts, local traffic orders and a complete reversion history.

**Provisional reconstruction.** The 28% headline is reconstructed from vector coordinates in a published SVG, not read from a native table. The reconstruction checks are tight, but the values remain a graphical extraction of a provisional release.

**Unreconciled vintages.** The audit records that three official routes differ but does not attribute the differences to particular revisions, late returns or processing rules.

**Producer-side determination.** The non-identification determination was made inside one coordinated workflow. External-model review rounds examined it read-only, but no unaffiliated party has reproduced or reimplemented it.

**Non-exhaustive rivals and bounded novelty search.** The rival set is declared non-exhaustive. The novelty search excluded subscription indexes, Welsh-language-only material, much grey literature and full citation graphs, and made no author enquiries.

**Prior-art records.** The three overlapping working papers are represented by Evidence Press bibliographic audit records, not frozen copies, because no redistribution licence was found. Later verification of those summaries depends on continued access to the commit-pinned upstream files.

**Scope of the witness.** The proposition concerns one estimand, one window and the admitted unrestricted counterfactual class. It is a case-specific application of established identification reasoning, not a general theorem.

# Related work

**Earlier causal evaluations.** The bounded novelty audit of 11 August 2026 located three working papers from the Autonomous Policy Evaluation Project that already present Wales-versus-England difference-in-differences evaluations of the default change [`source.evidence-press.apep-0513-prior-art-audit.v1`, `source.evidence-press.apep-0734-prior-art-audit.v1`, `source.evidence-press.apep-0744-prior-art-audit.v1`]. As summarised in the audit record: APEP 0513 v1 uses monthly police-force-area collision outcomes for 2019 to 2024 and reports a preferred 20.3% collision reduction; APEP 0734 v1 uses quarterly local-authority casualty outcomes and reports reductions of roughly 16% to 22%, explicitly discussing the movement of records from the 30 mph to the 20 mph category; and APEP 0744 v1 uses quarterly local-authority collision outcomes, reports about a 15% reduction in low-speed collisions, and treats 2023 Q3 as a transition quarter. All three combine the 20 and 30 mph categories. These papers rule out any description of the present audit as the first causal evaluation of the policy. Their estimates rest on comparison-group restrictions that this audit neither adopts nor tests; including them as prior work does not validate or refute them.

**Official guidance.** The Office for Statistics Regulation's 20 mph guidance is a close conceptual antecedent. It highlights reclassification, the missing traffic data by speed limit, reporting changes and caution about causal statements [`source.osr.20mph-guidance-2026.v1`]. This audit converts those cautions into a source-bound estimand distinction and a constructive witness. It does not turn the guidance into an effect estimate.

**Public-health literature.** The novelty audit inspected an Edinburgh 20 mph evaluation (DOI 10.1136/jech-2023-221612) as a changed-road and stayed-road analogue, and two adjacent Welsh public-health items (DOIs 10.1136/bmjpo-2024-003274 and 10.1136/jech-2016-208859). None was treated as an exact precedent for the case-specific contribution (`searches/novelty-audit-2026-08-11.txt`).

**A later independent study.** After version 1.0.0 was published, Jiawei Xu (Royal Holloway, University of London) deposited replication materials for a manuscript titled "Vulnerable Road User Safety after Wales's Default 20 mph Reform: Implications for Sustainable Mobility" (Zenodo, version 1.0 on 24 August 2026 and version 1.1 on 3 September 2026; DOI 10.5281/zenodo.22259378). The deposit is outside the frozen corpus and its findings are not assessed here. According to its description, the study examines pedestrian, cyclist and child casualty outcomes after the reform, using English local authorities as the comparison group. Version 1.1 adds Poisson estimates for six main outcomes, outcome-specific pre-trend tests, broader-period sensitivity analyses, exact aggregate-unit placebo inference and leave-one-local-authority-out diagnostics, together with school-travel analyses, current road-status comparisons and speed-monitoring results.

The two pieces of work answer different questions. The estimand registered here is the effect on all police-recorded casualties on road segments whose limit changed, and the non-identification result is stated for an admitted class that contains no validated comparison series. A comparison-group design of the kind the deposit describes adds exactly the sort of identifying restriction that this class lacks, applied to different outcomes (vulnerable road users) and, judging from the description, at the level of local authorities. The present result therefore neither contradicts nor supports that study's conclusions. Whether its restrictions are credible, and whether its road-status comparisons narrow the treatment-map gap identified in Section \ref{the-claim-and-the-exact-estimand}, are questions for a separate assessment.

**Method lineage.** The identification-before-estimation procedure follows the earlier Evidence Press release *Stocks Are Not Flows*, which applies the same discipline to a different policy question. Reusing the method does not make this case independent confirmation of that release.

# What a causal estimate would need

The missingness record lists the bridges whose absence blocks point identification (`records/missingness.json`). A future version that aims at an estimate or an identified interval would need, at minimum:

1. a frozen, versioned historical segment map of roads that changed, kept 30 mph or later reverted, linked to stable road identifiers;
2. collision and casualty locations joined to that map under versioned coding and linkage-error rules;
3. a comparison design with several pre-period diagnostics, placebo dates and explicit interference and anticipation assumptions, registered before estimation;
4. affected-segment traffic, realised speed, enforcement, weather, reporting and concurrent-intervention measurements where they bear on the target; and
5. prospectively justified restrictions, with an identified set computed only if those restrictions support one.

Adding more aggregate quarters, or an England series alone, would leave the observation-map failure intact. Any such estimate would be a new analysis version with its own evidence boundary and replay.

# Assurance statement

Table 8 states the assurance position of version 1.1.0, dimension by dimension, in the terms used on the Evidence Press release page.

: Assurance vector.

| Dimension | State | Basis |
|:------------------------|:----------------|:-------------------------------------------------------|
| Availability and archiving | Passed for v1.0.0 | GitHub release `v1.0.0` and Zenodo record 21894035 with validation receipt and checksum manifest. Version 1.1.0 archiving is pending. |
| Internal replay | Passed | Producer clean-checkout replay of commit `044de77` (283 tests, optimized controls, case gates), retained as an attestation; checks rerun on 12 October 2026 (Appendix A). |
| Independent rerun | Not assessed | No unaffiliated party has reported rerunning the package. |
| Independent reimplementation | Not assessed | No unaffiliated implementation of the vintage ladder or witness. |
| Formal verification | Not assessed | Exact arithmetic and schema guards execute; no proof-assistant theorem. |
| Specialist review | Not assessed | No external human road-safety, official-statistics or causal-inference specialist review. |
| Editorial peer review | Not assessed | No journal or venue review to a decision. |
| Data and environment | Partial | Offline dependency lock, source hashes and command vectors; no independently recreated container or Nix/Guix environment. |

The reviews recorded in the package are internal to one producer-coordinated workflow. Four read-only rounds by an external model (Anthropic Fable, via a secure bridge) examined pinned commits. Rounds one to three requested revision; the round-four report recommended `READY` with no unresolved critical finding, and all six findings raised across the rounds are recorded as resolved (`records/adversarial_findings.json`). The same reviewer system performed all four rounds, so they are continuity review, not independent corroboration. Rounds five to eight are deterministic continuity certificates for release-infrastructure corrections, not scientific review. This manuscript was additionally given to a second vendor's model (OpenAI, `gpt-5.6-sol`) prompted to refute any statement not supported by the frozen records; its findings and their dispositions are retained with the version 1.1.0 package. None of these steps is human peer review or independent reproduction. Hashes establish byte identity and replay establishes the declared transformations; neither establishes source validity, causal truth, policy merit or real-world impact.

**Provenance and AI use.** The case records, analysis and version 1.0.0 package were produced by AI agents (recorded in the v1.0.0 metadata as the OpenAI Codex agent team) under human direction, with read-only model review as described above. This manuscript was drafted by an AI agent (Anthropic Claude) from the frozen records, without new empirical analysis; Figure 1 plots an existing derived table. The scholarly author line is "Anonymous". The repository maintainer and publisher is recorded in the package provenance.

\appendix

# Reproducibility

**Identities.** Repository: <https://github.com/ipitchford/wales-20mph-policy-analysis>, tag `v1.0.0` at commit `7ea482fa82fd2330db6383c249aba0d43ac4bea4` (packaged release source). Reviewed scientific commit `e068cd1779fd762ed4c8bda94676c18145d31898`; replayed commit `044de77e14959cfb987d67505c43a63d64b82a4c`. The 45-entry non-circular scientific review target has SHA-256 `8f4434763bd9c2970b140ac222dfec388a3f29b93a3f6eb5894b4130023cf135`. The scientific-input manifest digest is `d058eed268056bbb07d5ee2b6747dfe93c074092bfa0fd4b4d722f77c3858bfb`. The witness artifact `derived/analysis.json` has SHA-256 `f0588f5a784ca34b8efe7c4a5d380d8ffdf660b240dc0891f97194d7735856af`.

**Environment.** Git, uv and Python 3.11 or later. The dependency lock is `uv.lock` (SHA-256 `bb7cdc9ccf00e3697c81d6a1198e3e217d91910a61c587f0dc9aceb53c94e96d` as recorded in the attestation). Replay needs no network once the environment is synchronised.

**Commands.** From a fresh clone at tag `v1.0.0`:

```
uv sync --no-editable --frozen --extra dev \
  --reinstall-package policy-identification-observatory
uv run --no-editable --frozen pio validate \
  cases/wales-20mph-casualty-attribution --schema-root schemas
uv run --no-editable --frozen pio check-citations \
  cases/wales-20mph-casualty-attribution --schema-root schemas
uv run --no-editable --frozen pio replay \
  cases/wales-20mph-casualty-attribution --schema-root schemas
uv run --no-editable --frozen python tools/build_wales_20mph_tables.py check
uv run --no-editable --frozen python -m pytest
uv run --no-editable --frozen python -O -m pytest
uv run --no-editable --frozen python -O tools/optimized_scientific_controls.py
```

The full lifecycle, which writes `MANIFEST.sha256`, `lifecycle-summary.json`, `validation-receipt.json` and an `evidence-press` package directory, is

```
uv run --no-editable --offline --frozen --no-sync pio lifecycle \
  cases/wales-20mph-casualty-attribution --schema-root schemas \
  --output OUTPUT_DIRECTORY
```

From the Zenodo archive, verify `MANIFEST.sha256`, clone `REPOSITORY_HISTORY.bundle`, check out the packaged release-source commit and run the same commands. The package README describes the detached verifier `verify_pio_package.py`, which should be obtained independently from the pinned commit.

**Expected results.** Schema and cross-record validation pass; the citation audit reports 25 cited sources, 125 bindings, 29 verified frozen-text anchors and no uncited source; replay reports 17 calculations matching their stored exact values; the table check passes and the five derived artifacts keep their registered digests; 283 tests pass in ordinary mode; and the optimized scientific controls pass.

**Rerun on 12 October 2026.** Every command above, including the optimized pytest smoke run and the full lifecycle, was rerun on a fresh clone of tag `v1.0.0` while preparing this manuscript. All exited with status zero and the results matched the expectations above. The lifecycle reached `PUBLICATION_READY_NONIDENTIFICATION` with determination `NON_IDENTIFIED`, and its regenerated `REPOSITORY_SNAPSHOT.tar`, `SCIENTIFIC_INPUTS.sha256` and `PRESS_RELEASE.md` were byte-identical to those in the published version 1.0.0 package. This is a further producer-side replay, not independent reproduction. The logs are retained with the version 1.1.0 package.

**Figure.** Figure 1 is generated by `figures/make_figure1.py`, which refuses any input other than the registered `derived/quarterly_event_series.csv` (SHA-256 `192401637ebdeaff83c983472591fd968c12feb8cc184d6aea7161f9b12f077f`).

# Registered sources

All sources were retrieved on 11 August 2026 and are frozen in `frozen_sources/` with the digests recorded in `records/source_provenance.json`. "WG" is the Welsh Government; "DfT" the Department for Transport; "OSR" the Office for Statistics Regulation.

```{=latex}
\begingroup\footnotesize
```

| Registered identifier | Title and publisher |
|:--------------------------------------------|:--------------------------------------------------------|
| `source.legislation.wsi-2022-800.v1` | The Restricted Roads (20 mph Speed Limit) (Wales) Order 2022. legislation.gov.uk, 2022. |
| `source.wg.q3-2024-provisional.v1` | Police recorded road collisions: July to September 2024 (provisional). WG, 30 Jan 2025. |
| `source.wg.figure4-quarterly-casualties.v1` | Figure 4: Quarterly casualties reported on roads with a 20 or 30mph speed limit in Wales (SVG). WG, 30 Jan 2025. |
| `source.wg.road-collisions-2023.v1` | Police recorded road collisions: 2023. WG, 6 Jun 2024. |
| `source.wg.road-casualties-2024-final.v1` | Reported road casualties: 2024. WG, 27 Nov 2025. |
| `source.wg.road-collisions-casualties-2025-final.v1` | Police recorded road collisions and casualties: 2025. WG, 4 Jun 2026. |
| `source.wg.road-collision-quality-report.v1` | Police recorded road collisions and casualties: quality report. WG, 4 Jun 2026. |
| `source.wg.road-traffic-2024.v1` | Road traffic: 2024. WG, 25 Sep 2025. |
| `source.wg.30mph-exception-guidance.v1` | Setting 30mph speed limits on restricted roads: guidance for highway authorities. WG, 8 Nov 2022. |
| `source.wg.copyright-statement.v1` | Copyright statement. WG, undated. |
| `source.statswales.20-30mph-2015q1-2026q1.v1` | Police recorded road casualties by speed limit and severity, 2015 Q1 to 2026 Q1, 20/30 mph extract. WG (StatsWales), 29 Jul 2026. |
| `source.statswales.20-30mph-2022q4-2024q3.v1` | The same dataset, 2022 Q4 to 2024 Q3 claim-window extract. WG (StatsWales), 29 Jul 2026. |
| `source.statswales.dataset-metadata.v1` | The same dataset: metadata. WG (StatsWales), 29 Jul 2026. |
| `source.dft.collisions-2021.v1` | Road Safety Data, Collisions, 2021. DfT, snapshot of 30 Jul 2026 page. |
| `source.dft.collisions-2022.v1` | Road Safety Data, Collisions, 2022. DfT, as above. |
| `source.dft.collisions-2023.v1` | Road Safety Data, Collisions, 2023. DfT, as above. |
| `source.dft.collisions-2024.v1` | Road Safety Data, Collisions, 2024. DfT, as above. |
| `source.dft.collisions-2025.v1` | Road Safety Data, Collisions, 2025. DfT, as above. |
| `source.dft.road-casualty-data-guide-2025.v1` | Road safety open dataset data guide 2025. DfT. |
| `source.dft.road-safety-open-data.v1` | Road safety open data (landing page). DfT, 25 Sep 2025. |
| `source.osr.20mph-guidance-2026.v1` | 20mph speed limit (guidance). OSR, 4 Mar 2026. |
| `source.osr.copyright.v1` | Copyright. OSR. |
| `source.evidence-press.apep-0513-prior-art-audit.v1` | Evidence Press bibliographic audit of APEP 0513 v1. CC0, 11 Aug 2026. |
| `source.evidence-press.apep-0734-prior-art-audit.v1` | Evidence Press bibliographic audit of APEP 0734 v1. CC0, 11 Aug 2026. |
| `source.evidence-press.apep-0744-prior-art-audit.v1` | Evidence Press bibliographic audit of APEP 0744 v1. CC0, 11 Aug 2026. |

```{=latex}
\endgroup
```

**Works outside the frozen corpus cited in this manuscript.** Xu, J. (2026). Replication materials for "Vulnerable Road User Safety after Wales's Default 20 mph Reform: Implications for Sustainable Mobility", version 1.1. Zenodo. DOI 10.5281/zenodo.22259378 (description read on 12 October 2026). Anonymous (2026). *Stocks Are Not Flows: An Identification Audit of Investor Pressure and Tenure Change in England*. Evidence Press, <https://evidencepress.org/releases/stocks-are-not-flows/>. The Edinburgh and Welsh public-health DOIs in Section \ref{related-work} are cited as recorded in the novelty search ledger.

# Version history

**1.0.0 (11 August 2026).** Evidence package: case records, frozen sources, derived tables, review history, clean-replay attestation and validation receipt. DOI 10.5281/zenodo.21894035. No manuscript.

**1.1.0 (this version).** Adds this manuscript (PDF and source) and the figure script. The scientific records, frozen sources, derived tables, claim ceiling and determination are unchanged from 1.0.0. Version 1.0.0 remains citable under its own DOI.

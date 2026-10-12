# AI index — Wales 20 mph casualty attribution audit, companion manuscript

**Identity:** release `wales-20mph-attribution-manuscript`, version 1.0.0-candidate, 12 October 2026,
DOI 10.5281/zenodo.23326288. Companion to the evidence package DOI 10.5281/zenodo.21894035
(https://github.com/ipitchford/wales-20mph-policy-analysis, tag `v1.0.0`), which is not changed.

**Claim tested (not endorsed):** the Welsh default 20 mph limit caused the reported 28% fall in casualties on
20 and 30 mph roads in its first year.

**Result (claim ceiling):** the provisional 28% is a reproducible description of one vintage (2,402 → 1,725;
exactly −33850/1201 %); later frozen vintages give −26.10% (StatsWales) and −24.18% (DfT). For the registered
estimand — the percentage effect on police-recorded casualties on segments whose limit changed from 30 to 20 mph
on 17 September 2023, 2023 Q4–2024 Q3, against the same segments' no-policy count — three hypothetical worlds
with identical observed aggregates give −50%, 0% and +100%. Neither the effect nor its sign is identified; no
empirical bound is registered. Not a finding that the policy failed, succeeded or had no effect.

**Status:** unrefereed candidate; producer-side replay; internal AI-assisted review only.

## Where to look

- Manuscript: [wales-20mph-attribution-manuscript-v1.0.0-candidate.pdf](wales-20mph-attribution-manuscript-v1.0.0-candidate.pdf); source [paper/MANUSCRIPT.md](paper/MANUSCRIPT.md); build [paper/build.sh](paper/build.sh)
- Figure generator: [paper/figures/make_figure1.py](paper/figures/make_figure1.py)
- Structured claims: [CLAIMS.json](CLAIMS.json); status: [STATUS.md](STATUS.md); provenance: [PROVENANCE.md](PROVENANCE.md)
- Review findings and dispositions: [review/DISPOSITIONS.md](review/DISPOSITIONS.md); exact exchange [review/sol-round-1/](review/sol-round-1/)
- Rerun logs: [review/replay-2026-10-12/](review/replay-2026-10-12/) (lifecycle receipt [validation-receipt.json](review/replay-2026-10-12/lifecycle-out/validation-receipt.json); derived digests [derived-digests.txt](review/replay-2026-10-12/derived-digests.txt))
- Licences: [LICENSES.md](LICENSES.md); hashes: [MANIFEST.sha256](MANIFEST.sha256)

## Authoritative records (evidence package, unchanged)

`cases/wales-20mph-casualty-attribution/records/` — `exact_estimand.json`, `identification_status.json`,
`assumptions.json`, `rival_mechanisms.json`, `missingness.json`, `inferences.json`, `observations.json`
(17 exact calculations), `source_provenance.json` (25 sources), `corpus_boundary.json`,
`adversarial_findings.json`, `final_receipt.json`; `derived/analysis.json` (witness). Scientific review target
SHA-256 8f4434763bd9c2970b140ac222dfec388a3f29b93a3f6eb5894b4130023cf135.

## Known record inconsistency

The package's `reviews/fable-round-4/report.json` recommends READY; its `records/adversarial_findings.json`
review_history labels round four REVISION_REQUESTED. Stated in manuscript Section 12; not resolved.

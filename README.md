# Wales 20 mph Casualty Attribution Audit — companion manuscript

Status: **unrefereed candidate** · version `1.0.0-candidate` · 12 October 2026 · DOI [10.5281/zenodo.23326288](https://doi.org/10.5281/zenodo.23326288)

This repository publishes the manuscript for the Evidence Press audit of the claim that the Welsh default
20 mph limit caused the reported 28% first-year fall in casualties on 20 and 30 mph roads. The audit's evidence
package was published on 11 August 2026 without a paper
([DOI 10.5281/zenodo.21894035](https://doi.org/10.5281/zenodo.21894035);
[repository](https://github.com/ipitchford/wales-20mph-policy-analysis), tag `v1.0.0`). This is a separate
companion release. It reports the package's frozen records, adds no new empirical analysis and changes nothing
in the package.

**Result.** The provisional 28% figure is reproducible as a description of one data vintage (2,402 → 1,725
casualties; exactly −33850/1201 %); later frozen vintages give about −26.10% and −24.18%. For the registered
estimand — the effect on police-recorded casualties on road segments whose limit changed — three hypothetical
worlds with identical observed aggregates give effects of −50%, 0% and +100%. Within the frozen evidence and
admitted rival set neither the effect nor its sign is identified. The result does not show that the policy
succeeded or failed.

## Contents

| Path | What it is |
|:--|:--|
| [`wales-20mph-attribution-manuscript-v1.0.0-candidate.pdf`](wales-20mph-attribution-manuscript-v1.0.0-candidate.pdf) | The manuscript (16 pages) |
| [`paper/`](paper/) | Source: `MANUSCRIPT.md`, `header.tex`, `code-to-path.lua`, `build.sh`, `figures/` |
| [`review/DISPOSITIONS.md`](review/DISPOSITIONS.md) | AI adversarial review of the manuscript and dispositions |
| [`review/sol-round-1/`](review/sol-round-1/) | Exact review request, response and manuscript as sent |
| [`review/replay-2026-10-12/`](review/replay-2026-10-12/) | Producer rerun logs of the evidence-package checks |
| [`STATUS.md`](STATUS.md), [`PROVENANCE.md`](PROVENANCE.md), [`AI_INDEX.md`](AI_INDEX.md), [`CLAIMS.json`](CLAIMS.json) | Status, provenance, machine index, claim record |
| [`LICENSES.md`](LICENSES.md), [`MANIFEST.sha256`](MANIFEST.sha256) | Licence map, file hashes |

## Rebuild

PDF: pandoc 3 and XeLaTeX with Linux Libertine O, Libertinus Math and Menlo; run `paper/build.sh`.
Figure 1: `python paper/figures/make_figure1.py <package>/cases/wales-20mph-casualty-attribution/derived/quarterly_event_series.csv paper/figures/figure1.pdf`
(the script refuses any input whose SHA-256 differs from the registered digest).
Scientific checks: manuscript Appendix A, run in a clone of the evidence-package repository at tag `v1.0.0`.

## Assurance boundary

Producer-side replay passes. Reviews on record are internal to the producer workflow (four read-only rounds by
one external model on the package; one adversarial manuscript review by a second vendor's model). No independent
rerun, independent reimplementation, formal verification, external specialist review or editorial peer review
has been established. Hashes establish byte identity; replay establishes declared transformations; neither
establishes source validity, causal truth, policy merit or real-world impact.

Cite as: Anonymous (2026). *Wales 20 mph Casualty Attribution Audit: A Constructive Non-Identification Result —
companion manuscript* (1.0.0-candidate). Evidence Press. https://doi.org/10.5281/zenodo.23326288

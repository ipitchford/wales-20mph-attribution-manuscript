# Adversarial review of the v1.1.0 manuscript: dispositions

- Reviewer: OpenAI `gpt-5.6-sol` via `/v1/responses`, single call, 2026-10-12 20:49:04Z to 20:50:32Z.
- Framing: refute any manuscript statement not supported by the supplied evidence bundle (instructions in `sol-round-1/prompt-instructions.txt`).
- Input: manuscript as sent (`sol-round-1/MANUSCRIPT.as-sent.md`, SHA-256 `709be10ee3467184778eb51141fd2a3907acbf2061460757c8608f279cda4b31`) and an evidence bundle of case records, derived tables, search and audit records, the specification, the v1.0.0 and Xu Zenodo metadata, the live page machine record and the 12 October replay summary. Full request `sol-round-1/request.json` (SHA-256 `343db103190eab0303189e37e021a4d0ffeb43f4c4fc12210c4f0e38c12f4a1a`), raw response `sol-round-1/response.json`, text `sol-round-1/response.md`.
- Usage: 88,535 input tokens, 7,298 output tokens. Cost not recorded by the API response.
- Status: AI-assisted adversarial review inside the producer workflow. Not human peer review, not independent reproduction.

Every finding was checked against the repository at tag `v1.0.0` and the retained logs before disposition. Twenty-one findings: 13 accepted and fixed (some with modified wording), 8 rejected because the supporting evidence exists outside the bundle sent to the reviewer; that evidence is now retained in the package.

| ID | Sev. | Finding (short) | Verification | Disposition |
|:--|:--|:--|:--|:--|
| S1 | MAJOR | "target period ... is unaffected" misreads as policy-free | Correct: wording meant "no pre-commencement days" | Fixed: "contains no pre-commencement days" |
| S2 | MINOR | Table 1 calls the earlier period a counterfactual stand-in | Correct: inconsistent with the descriptive status | Fixed: "only a descriptive comparator" |
| S3 | MINOR | Reversions do not change the registered affected set | Correct: `exact_estimand.json` fixes membership at 17 Sep 2023; adversarial record says the same | Fixed |
| S4 | MAJOR | Count semantics give logical extrema; "no minimum or maximum" too strong | Mathematically correct; records forbid reporting extrema but the logical limits exist | Fixed: logical limits acknowledged as uninformative; no empirical bounds registered |
| S5 | MAJOR | "needs every load-bearing assumption" conflates two designs | Correct: before/after and England bridges are alternatives | Fixed: designs need different subsets; neither bridge available |
| S6 | MAJOR | "would need, at minimum" stated as universal | Partly: the wording comes from the case README, but the identification record leaves other designs open | Fixed: attributed to the case README and qualified |
| S7 | MINOR | "more quarters ... would leave failure intact" too categorical | Correct (live page itself says "may") | Fixed: conditioned on absence of map and restriction |
| S8 | MAJOR | No v1.1.0 manifest shows records unchanged | v1.1.0 package is built from the unchanged v1.0.0 assets plus the manuscript; `package/wales-20mph-v1.1.0/MANIFEST.sha256` and the plan's target-digest check bind it | Rejected (evidence outside bundle, now retained) |
| S9 | NOTE | "archiving is pending" unsupported | True at time of writing | Fixed: "pending at the time of writing" |
| S10 | MAJOR | Round-four `READY` vs history field `REVISION_REQUESTED` | Verified both fields in the frozen records | Fixed: inconsistency disclosed in Section 12; raised as an open question |
| S11 | MAJOR | Sol review not documented | This record and `sol-round-1/` | Rejected (now retained in package) |
| S12 | MAJOR | Claude as drafter unsupported | True; recorded in package `PROVENANCE.md` | Rejected; provenance sentence points to the package record |
| S13 | MINOR | "Anonymous" vs v1.0.0 creators | Verified: Zenodo 21894035 creators differ | Fixed: house convention stated; v1.0.0 creator line noted as left as published |
| S14 | MAJOR | *Stocks Are Not Flows* method link unsupported | Supported by the v1.0.0 release page text (read 12 Oct 2026) | Fixed wording to attribute the statement to that page |
| S15 | MAJOR | Tag-to-commit binding unsupported | `git ls-remote`: `refs/tags/v1.0.0^{}` = `7ea482f`; also the package PRESS_RELEASE (`replay-2026-10-12/clone-identity.txt`) | Rejected (evidence retained) |
| S16 | MINOR | Python >= 3.11 unsupported | `pyproject.toml` line 10 `requires-python = ">=3.11"`; repo README | Rejected; citation added in text |
| S17 | MINOR | "needs no network" too broad | Fair | Fixed: describes the `--offline` lifecycle command only |
| S18 | MAJOR | Fresh clone and per-command logs not shown | Logs in `replay-2026-10-12/` (one file per command, clone identity, environment) | Rejected (evidence retained); clone identity and environment added to text |
| S19 | MINOR | Five artifact digests not shown | `replay-2026-10-12/derived-digests.txt`: all five match `case.json` | Rejected (evidence retained) |
| S20 | MAJOR | Figure script not supplied | `manuscript/figures/make_figure1.py` checks the registered SHA-256 and exits otherwise | Rejected (script in package) |
| S21 | MINOR | APEP verification depends on URLs and Git objects; bodies not frozen | Correct per the audit record | Fixed |

No finding challenged a number, the estimand, the witness or the proposition's proof. No second review round was run; the repairs are wording-level and were checked against the records directly.

## Re-scoping after review (12 October 2026)

After this review the manuscript was re-scoped, on the publisher's instruction, from a version 1.1.0 of the 11 August 2026 package to a separate companion release with its own DOI (10.5281/zenodo.23326288; concept lineage independent of 10.5281/zenodo.21894034). The evidence package's Zenodo record, Git tag and Evidence Press page are not changed. The only manuscript edits were the release framing (subtitle, running header, status box, availability row, provenance and appendix C wording); no number, claim or caveat changed. Disposition S8 now reads: the companion release reports the package's records without altering them, bound by its own manifest.

# Review package

This directory is generated for human and agent review. It is not a deployment.
Reviewed scientific commit: `e068cd1779fd762ed4c8bda94676c18145d31898`.
Replayed commit: `044de77e14959cfb987d67505c43a63d64b82a4c`.
Packaged release-source commit: `7ea482fa82fd2330db6383c249aba0d43ac4bea4`.
`package.json` is the complete machine-readable handoff. `REPOSITORY_SNAPSHOT.tar` is the inspectable release-source tree; verify every member with `REPOSITORY_SNAPSHOT.json` before extraction.
Before checkout, obtain `verify_pio_package.py` independently from the pinned release-source commit, verify its separately trusted digest, and run it against this directory and the outer receipt. The verifier is deliberately not self-trusted by this package.
For exact offline release replay, run `git clone REPOSITORY_HISTORY.bundle observatory`, enter `observatory`, and check out the packaged release-source commit.
Bootstrap the locked environment with `uv sync --no-editable --frozen --extra dev --reinstall-package policy-identification-observatory`.
`MANIFEST.sha256` binds all other package payload files.
Then run `uv run --no-editable --offline --frozen --no-sync pio lifecycle cases/wales-20mph-casualty-attribution --schema-root schemas --output OUTPUT_DIRECTORY` from the cloned repository root.
Structured environment requirements come from the Observatory release; use the committed `uv.lock` rather than inferring them from a prior host.

# Decision log

## 2026-09-13 — Start a release-oriented Git repository

The 4.4 GB experimental workspace is not made into one monolithic Git
repository.  A smaller control repository tracks the paper, audit ledger,
verification programs, compact logs, and manifests.  Large closed evidence
objects are GitHub release assets pinned by SHA-256.

Reason: Git history should make mathematical changes reviewable.  Committing
the entire experiment tree would obscure those changes, include a file above
GitHub's ordinary 100 MB object limit, and make ordinary cloning needlessly
expensive.

## 2026-09-13 — Keep the proof status open

The V3 release's integrity and replay results are preserved as historical
facts.  This repository does not adopt the stronger phrase “no further
mathematical defect” while the independent Mordell--Weil rank reconstruction
is unfinished.

Reason: successful replay of authenticated downstream evidence is not the same
thing as an independent proof of every load-bearing group-theoretic input.

## 2026-09-13 — Preserve later dependency closures as separate assets

The p=5 obstruction closure and the B124/D4 reconstruction remain separate
immutable archives.  They are not silently folded into the older V3 archive.

Reason: this retains a legible history of which audit question caused each
addition and permits reviewers to verify the repair independently.

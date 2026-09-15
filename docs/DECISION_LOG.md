# Decision log

## 2026-09-13 — Create a private GitHub remote

The audited local history was pushed to
`https://github.com/bbpcho/primitive-357-proof-audit` using HTTPS.  The
repository remains private while the rank gate and redistribution review are
open.  No large evidence asset or public release was uploaded.

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

## 2026-09-14 — Integrate the completed independent proof audit

The newly supplied rank dependencies and adopted independent replacements close the named rank-upper-bound gate. The complete local-image arguments include the replacement p=7 kernel witness and second-dyadic correction. Exact linear algebra identifies the complementary literal class used by the completed p=5 obstruction.

The manuscript distinguishes H0 from H1: odd index concerns H0, whereas index coprime to 400 and finite-sieve coverage concern the E-enlarged H1. The correction notice preserves the preceding sealed audit identity.

The user authorized a newly verified release and GitHub changes. The new tag is `verified-2026-09-14.1`. Its publication-ready machine status requires the fresh integrated replay and the exact sealed asset bindings; historical PASS summaries alone do not satisfy that requirement. The stated published and Magma premises remain explicit.

## 2026-09-15 — Publish the externally acquired-input replacement

The replacement `replay-companion-2026-09-15.2` was published and its five public assets were downloaded without authentication and checked against the sealed identities. The p=5 and rank downloads containing the BPS paper were withdrawn afterward, with both old API and download endpoints observed as HTTP 404. Their original byte identities remain in the ledger.

The main 13/65/16/5 replay and five separate default-reader checks retain distinct scope. The V5 reporting aggregate is corrected to 237,182 without changing the eight exact support tables. Seven prior Magma executions and the cited mathematical/software premises remain explicit. The release tag identifies prepared snapshot A; these observed postpublication records belong to the main-branch follow-up B. No arXiv submission has been made; Dahmen's requested reply remains the hold.

# Evidence model

## Four evidence classes

The repository labels evidence by what it can legitimately establish.

1. **Source** — a program or manuscript that states what should be done.
2. **Record** — output from an identified program and input set.
3. **Replayable certificate** — source, inputs, output, software boundary, and
   a verifier are all present in a closed package.
4. **Independent audit** — the mathematical interface has been reconstructed
   independently and its conclusion is stated with explicit nonclaims.

Hash equality establishes identity, not truth.  A clean replay establishes
repeatability, not by itself the hypotheses of the theorem being invoked.

## What Git stores

This repository stores the control plane:

- paper source and a reference PDF;
- status and decision documents;
- dependency indexes and strict manifests;
- compact replay logs;
- verification and release-building programs;
- independent review material small enough for ordinary Git.

## What GitHub Releases store

Large, immutable archives belong in release assets.  Their exact metadata is
in `evidence/assets.json`; the human-readable checksum list is
`evidence/checksums/RELEASE_ASSETS_SHA256.txt`.

The first asset set contains:

- the complete V3 reproducibility archive;
- the V3 arXiv upload archive and reader bundle;
- the p=5 obstruction dependency closure;
- the B124/D4 upstream reconstruction package.

The compact, reviewable control files for the two post-V3 packages are also
tracked under `evidence/post-v3/`.  Their large `repository/` payloads remain
inside the release assets, so the checked-in indexes and replay programs stay
legible without weakening dependency closure.

The repository verifier checks the index itself.  `verify_assets.py` checks
the actual downloaded files.

The p=5 closure is attached to the private prerelease
`audit-2026-09-13.1`.  Its direct URL is recorded in `evidence/assets.json`;
GitHub authentication is required while the repository remains private.

## Immutable and working layers

Released evidence is immutable.  Repairs create a new package and a new
manifest; they do not overwrite historical bytes.  The working audit can
refer to a superseded record, but must mark it superseded and state why.

This is the same calm-decision principle used during the computation: preserve
what happened, distinguish observation from inference, and promote a claim
only when its stated gate passes.

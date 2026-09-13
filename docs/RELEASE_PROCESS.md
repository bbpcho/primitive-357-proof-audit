# Release process

## Release types

### Audit snapshot

An audit snapshot may be published while mathematical gates remain open.  Its
title and notes must say so.  It may contain new dependency packages, no-go
reports, and manuscript drafts.

### Proof release

A proof release is permitted only when `audit/status.json` has
`proof_complete: true` and every mandatory gate is `pass`.

## Candidate procedure

1. Start from a clean Git commit.
2. Run `make verify`.
3. Build the paper with `make paper` and inspect the resulting PDF.
4. Place every large candidate asset in one staging directory.
5. Run `python3 -B scripts/verify_assets.py --assets-dir STAGING`.
6. Extract each replayable package into a fresh temporary directory and run
   its documented verifier.
7. Run the sector and foundational replay in an environment where the
   original workspace cannot be reached.
8. Record software versions, commands, exit codes, wall times, and logs.
9. Obtain two independent audit decisions for any newly load-bearing
   mathematical interface.
10. Update the manuscript, status ledger, asset index, checksum list, and
    changelog in one reviewable commit.

## Tag and asset convention

- Audit snapshots: `audit-YYYY-MM-DD.N`
- Proof candidates: `proof-candidate-N`
- Final release: `v1.0.0`, only after the proof gate closes

Attach large archives to the corresponding GitHub release using their exact
basenames.  Do not recompress a sealed archive under the same name: archive
metadata changes its SHA-256 even when payload files are unchanged.

## Public-release checklist

- [ ] Author name and affiliation supplied.
- [ ] Repository license and third-party redistribution rights decided.
- [ ] Rank/generation gate independently closed.
- [ ] Downstream sieve/local-log consumption audited.
- [ ] Manuscript claim matches the audited boundary.
- [ ] Paper compiles without unresolved references or overlapping material.
- [ ] All release assets match `evidence/assets.json`.
- [ ] Clean-extraction complete replay passes.
- [ ] Two independent final audit decisions pass.
- [ ] Release notes distinguish new results, repairs, and inherited facts.

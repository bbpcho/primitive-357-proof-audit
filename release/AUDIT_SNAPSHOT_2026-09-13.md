# Audit snapshot — rank gate open

This snapshot establishes a clean Git-based review boundary for the proposed
proof of the primitive generalized Fermat equation `x^3 + y^5 = z^7`.

## Included in Git

- the current V3 manuscript source and reference PDF;
- the V3 dependency indexes, strict manifests, compact sector logs, and
  release verifiers;
- the independent V2 review and Section 7 Kummer repair materials;
- readable control files for the post-V3 p=5 obstruction closure;
- readable control files for the post-V3 B124/D4 reconstruction;
- readable control files for the corrected-66/second-dyadic closure;
- a machine-readable proof-status ledger and exact rank-gap completion
  contract.

## Release assets

The seven large immutable archives are listed in `evidence/assets.json` and
`evidence/checksums/RELEASE_ASSETS_SHA256.txt`.  Verify downloaded copies with:

```bash
python3 -B scripts/verify_assets.py --assets-dir /path/to/downloads
```

The p=5 obstruction and corrected-66/second-dyadic dependency closures are
attached to this prerelease.  The remaining listed archives are
checksum-pinned but not yet attached.

## Current result

Repository integrity, archive identity, and paper compilation pass.  The V3
clean-extraction replay is preserved.  The p=5, B124/D4, corrected-66, and
second-dyadic provenance gaps now have closed replay packages.

The saturation and split-23 logarithm calculations are complete at the current
evidence boundary.  The mathematical Mordell--Weil rank upper-bound and
composition audit remains open.  Therefore this is deliberately a prerelease
audit snapshot, not a claim that the final proof has been independently
completed.

See `docs/RANK_GAP.md` for the exact completion gates.

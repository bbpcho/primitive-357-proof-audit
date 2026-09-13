# Primitive (3,5,7): proof audit and reproducible release

This repository is the working control centre for the proposed proof of the
primitive generalized Fermat equation

\[
  x^3+y^5=z^7.
\]

Private working remote: <https://github.com/bbpcho/primitive-357-proof-audit>

It separates three things that had become too easy to confuse:

1. a mathematical claim;
2. a successful replay of a particular certificate;
3. a publication-ready proof.

The present state is **audit in progress**.  The paper compiles, the V3
dependency-closed release and its sector replays are preserved, and two later
dependency packages close important provenance omissions.  The final theorem
is **not yet marked proved here** because the Mordell--Weil rank chain still
needs a clean independent reconstruction from its upstream inputs.

That conservative status is intentional.  A green integrity check means that
the named bytes are present and consistent; it does not silently promote an
open mathematical interface into a theorem.

## Start here

- [Current proof status](docs/PROOF_STATUS.md)
- [Exact rank-gap completion contract](docs/RANK_GAP.md)
- [Rank reconstruction workplan](audit/rank-gap/WORKPLAN.md)
- [Evidence and release-asset model](docs/EVIDENCE.md)
- [Release procedure](docs/RELEASE_PROCESS.md)
- [GitHub publication handoff](docs/GITHUB_SETUP.md)
- [Decision log](docs/DECISION_LOG.md)
- [Current manuscript](paper/manuscript.tex)
- [Compiled V3 manuscript](paper/manuscript-v3.pdf)

Run the fast repository checks with:

```bash
make verify
```

If the large evidence archives have been downloaded into one directory:

```bash
python3 -B scripts/verify_assets.py --assets-dir /path/to/assets
```

For the present local workspace, the exact same check can be made with:

```bash
python3 -B scripts/verify_assets.py --workspace-root ..
```

The paper can be rebuilt with:

```bash
make paper
```

## Repository versus release assets

Git tracks the manuscript, audit state, indexes, verification programs,
small certificates, and replay logs.  Large closed evidence archives are not
put into ordinary Git history.  They are named and SHA-256 pinned in
`evidence/assets.json` and are intended to be attached to a GitHub release.
This avoids GitHub's ordinary object-size limit while retaining exact,
downloadable evidence.

The complete V3 reproducibility archive is about 263 MB; the p=5 obstruction
closure is about 150 MB; and the B124/D4 reconstruction package is about
42 MB.  Their cryptographic identities, byte sizes, roles, and local source
paths are all recorded.

## Publication rule

No tag may be described as a proof release until every mandatory gate in
`audit/status.json` is `pass`, two independent audit records agree, the paper
states exactly the proved boundary, and a clean extraction reproduces the
claimed computations without reaching into the original workspace.

Until then, repository releases should be labelled **audit snapshots**.

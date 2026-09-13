# GitHub setup and publication handoff

The repository is initialized on branch `main` and pushed privately to:

https://github.com/bbpcho/primitive-357-proof-audit

The remote is named `origin`, and local `main` tracks `origin/main`.

## Recommended first publication state

Create the repository as **private** while the Mordell--Weil rank audit is
open.  This still provides branches, issues, pull requests, Actions, and a
durable review history without presenting the current manuscript as a
finished public proof.  Change it to public when authorship, licensing,
third-party redistribution, and the proof gate are settled.

## Authentication

The GitHub CLI is authenticated as `bbpcho` using HTTPS.  If authentication
expires, restore it from a terminal with:

```bash
gh auth login -h github.com
```

Use the intended GitHub account and complete the browser/device flow.  No
token should be committed to this repository.

## Existing remote repository

The creation command used from this repository root was:

```bash
gh repo create primitive-357-proof-audit \
  --private \
  --source . \
  --remote origin \
  --push \
  --description "Audit and reproducibility repository for the primitive (3,5,7) equation"
```

## Create the first audit snapshot

After the remote exists and the rights review permits uploading the selected
assets, create a prerelease from `release/AUDIT_SNAPSHOT_2026-09-13.md` and
attach the exact files named in `evidence/assets.json`.

The first release should be a prerelease titled “Audit snapshot — rank gate
open,” not a final proof release.

## Later fixed release

When the rank gate closes:

1. merge the two independent rank audits;
2. update `audit/status.json` and the manuscript in the same pull request;
3. regenerate the tracked snapshot and release-asset index;
4. run the clean extraction and paper build;
5. tag a proof candidate;
6. attach the dependency-closed archive and arXiv source bundle;
7. publish only after the final audit and rights checks pass.

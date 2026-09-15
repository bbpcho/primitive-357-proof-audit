# Additive current-paper publication binding

Install `verify_current_publication.py` beside `verify_current_distribution.py` and `current_replay_coverage.py`. It makes no network calls and does not run mathematical programs. It authenticates the actual local paper and source ZIP, invokes the companion record checker, and compares saved public-download observations with the same paper/source/companion identities. Publication does not imply arXiv submission, mathematical proof formalization or peer review.

Do not change the historical `release_tag`, `release_asset_id`, `fresh_replay` or original gates in `audit/status.json` to satisfy this checker. They belong to the baseline verifier. This module neither writes status nor promotes an incomplete record.

## Status interface

While preparing the release, add only `"current_publication": {"state": "pending"}` and keep `arxiv_submission_ready` false. An absent or pending publication record returns `CURRENT_PUBLICATION_NOT_VERIFIED`, not PASS. No new paper/publication file is required in that state. Any top-level `arxiv_submitted` or `arxiv_submission_made` field must be false if present.

After actual publication and download observations, use exactly these four keys:

```json
"current_publication": {
  "state": "published",
  "paper_revision": {"path": "audit/replacement-release-2026-09-15/PAPER_REVISION.json", "bytes": 0, "sha256": "<actual SHA-256>"},
  "publication": {"path": "audit/replacement-release-2026-09-15/PUBLICATION.json", "bytes": 0, "sha256": "<actual SHA-256>"},
  "public_access": {"path": "audit/replacement-release-2026-09-15/PUBLIC_ACCESS_CHECK.json", "bytes": 0, "sha256": "<actual SHA-256>"}
}
```

The existing `current_paper_revision`, `current_paper_publication` and `public_access_check` string pointers must equal the respective paths. `arxiv_submission_ready` and `arxiv_submission_holds` must agree with the revision's submission object below. Other historical fields are untouched. A separate `current_release_publication_verification` pointer may name the checker's saved output, but this module does not read its own output or use it as a premise.

All paths are relative to R; absolute paths, traversal and symlinks are rejected. Every `{path,bytes,sha256}` row contains observed byte counts and lowercase SHA-256, not placeholders. The zeroes and angle brackets in this document are schematic and cannot pass verification.

## PAPER_REVISION.json

Required fields:

```json
{
  "schema": "primitive357_current_paper_revision_v1",
  "release_tag": "replay-companion-2026-09-15.2",
  "companion_binding": {"path": "<exact status.current_distribution.binding.path>", "bytes": 0, "sha256": "<actual>"},
  "paper_files": {
    "manuscript.tex": {"path": "paper/manuscript.tex", "bytes": 0, "sha256": "<actual>"},
    "rank-proof.tex": {"path": "paper/rank-proof.tex", "bytes": 0, "sha256": "<actual>"},
    "manuscript.pdf": {"path": "paper/manuscript.pdf", "bytes": 0, "sha256": "<actual>"}
  },
  "source_bundle": {
    "archive": {"path": "release/PRIMITIVE_357_ARXIV_SOURCE_2026-09-15_V2.zip", "bytes": 0, "sha256": "<actual>"},
    "members": [
      {"path": "manuscript.tex", "repository_path": "paper/manuscript.tex", "bytes": 0, "sha256": "<actual>"},
      {"path": "rank-proof.tex", "repository_path": "paper/rank-proof.tex", "bytes": 0, "sha256": "<actual>"}
    ]
  },
  "assets": {
    "paper_pdf": {"name": "primitive_357_peter_chocian_submission_2026_09_15_v2.pdf", "bytes": 0, "sha256": "<actual>", "url": "<exact GitHub download URL>"},
    "source_zip": {"name": "PRIMITIVE_357_ARXIV_SOURCE_2026-09-15_V2.zip", "bytes": 0, "sha256": "<actual>", "url": "<exact GitHub download URL>"},
    "companion": {"name": "<name from current companion binding>", "bytes": 0, "sha256": "<actual>", "url": "<exact GitHub download URL>"}
  },
  "submission": {
    "arxiv_submission_made": false,
    "arxiv_submission_ready": false,
    "dahmen_reply_pending": true,
    "holds": ["Requested Dahmen reply pending"]
  }
}
```

`companion_binding` must equal the complete current distribution binding row, and the companion asset must equal that binding's complete `asset` object. All three public assets use the companion's release tag. Their URLs must be exactly `status.github_repository + /releases/download/<URL-encoded tag>/<URL-encoded name>`.

The source member array must be sorted by member path and cover every ZIP entry exactly, with no directory, link, duplicate or undeclared member. Both canonical TeX files are mandatory. Add entries for a source README or other legitimate files and preserve identical bytes in R at their `repository_path`. Each repository path is unique. The PDF/source asset identities must match the checked local PDF/ZIP bytes. This is identity verification; PDF rendering and TeX compilation remain the separately recorded build checks.

If the requested Dahmen reply is still pending, readiness must be false and a nonempty hold mentioning Dahmen must remain. Even after all holds are cleared, readiness is a separate flag from submission; `arxiv_submission_made` must remain false in this contract.

## PUBLICATION.json

Use schema `primitive357_current_publication_v1`, the exact `repository`, `release_tag`, positive integer GitHub `release_id`, `draft: false`, `paper_revision_sha256`, `arxiv_submission_made: false`, and an observed timezone-qualified `published_utc` timestamp. `assets` is an array containing exactly the roles `paper_pdf`, `source_zip`, `companion`. Each entry is its revision asset row plus `role` and its positive integer GitHub `asset_id`; all three IDs must differ. Obtain these values from the actual public GitHub API record. Additional observation metadata may be included; it does not replace byte-identity checks.

## PUBLIC_ACCESS_CHECK.json

Use schema `primitive357_current_public_access_v1`, matching `repository`, `release_tag` and positive integer `release_id`, `draft: false`, a timezone-qualified `checked_utc` at or after publication, `unauthenticated_request: true`, and `repository_visibility: "public"` from the actual observation. `downloads` contains exactly the same three roles. Each entry contains `role`, `name`, matching positive integer `asset_id`, `url`, actual downloaded `bytes`, actual downloaded `sha256`, and integer `http_status: 200`.

These records must come from the actual public downloads, including the companion ZIP. The offline checker can authenticate consistency and record integrity; it cannot create or independently recreate a network observation. It does not require the large downloaded companion to be committed in R. If supplied with `--companion-archive`, it also invokes the complete companion ZIP/member check against the actual local archive bytes.

## Invocation

```text
python3 -B scripts/verify_current_publication.py --root .
python3 -B scripts/verify_current_publication.py --root . --companion-archive /path/to/final-companion.zip
```

The callable interface is `verify_current_publication(root, status, companion_archive=None)`. It can be invoked additively from the repository verifier after the existing baseline checks. Output can be saved as `PUBLICATION_VERIFICATION.json`; do not construct any circular hash dependency on that output.

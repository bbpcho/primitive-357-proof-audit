# Public copy inventory: Dahmen–Siksek paper

The pre-removal public GitHub API listed three releases and nine assets. **Two assets contained the exact Dahmen–Siksek PDF. Both were subsequently withdrawn and independently verified unavailable.** The older p=5 and rank packages do not contain that PDF. No copy occurs in the complete Git history reachable from the published branches and tags.

Target: `GFE357.pdf`, 235,180 bytes, SHA-256 `8b69da80fe79959ed1e05d35b613f7f728f599571b8f84f0a0d29c78e4c205c6`.

## Public assets that contained the paper

| Release ID / tag | Asset ID | Exact filename and original download URL | Bytes | Evidence |
|---|---:|---|---:|---|
| 389036163 / `first-submission-2026-09-15.1` | 565450862 | [PRIMITIVE_357_FIRST_SUBMISSION_COMPANION_V1.zip](https://github.com/bbpcho/primitive-357-proof-audit/releases/download/first-submission-2026-09-15.1/PRIMITIVE_357_FIRST_SUBMISSION_COMPANION_V1.zip) | 601,649,354 | Confirmed: embeds the verified ZIP byte for byte; outer digest matches the public API. |
| 388385413 / `verified-2026-09-14.1` | 563394734 | [PRIMITIVE_357_VERIFIED_RELEASE_2026-09-14_V1.zip](https://github.com/bbpcho/primitive-357-proof-audit/releases/download/verified-2026-09-14.1/PRIMITIVE_357_VERIFIED_RELEASE_2026-09-14_V1.zip) | 588,945,520 | Confirmed: recursive archive scan finds the exact PDF; outer digest matches the public API. |

The verified ZIP contains exactly one matching member at:

```text
PRIMITIVE_357_VERIFIED_RELEASE_2026-09-14_V1/
  evidence/v3/repository/results/2026-09-09_putz_hunter_local_algebra_covering_v6/
    inputs/local_algebra_covering_evidence_v6.tar.gz
      ! primary/dahmen-siksek/GFE357.pdf
```

The companion's member `computational_materials/PRIMITIVE_357_VERIFIED_RELEASE_2026-09-14_V1.zip` has the exact verified-ZIP digest, so the same copy is present one level deeper.

- Verified ZIP: SHA-256 `27e3e6eeb50f83ea484e7cd0c94dbd88de0141ab9f47634ed5181e7db0ecba33`.
- Companion: SHA-256 `fa0eaae5e193010a0714b1e72fd141f146e3e155148d530706258e3bb42e9a90`.

These are byte-identity conclusions: the local archives were hashed against the public GitHub asset digests, then their actual contents were inspected. The large archives were not downloaded again solely to repeat that inspection.

## Older public packages unaffected by this removal

| Release ID / tag | Asset ID | Exact filename and download URL | Bytes | Evidence |
|---|---:|---|---:|---|
| 387970666 / `audit-2026-09-13.1` | 561595084 | [2026-09-13_p5_literal_c_obstruction_dependency_closure_v1.zip](https://github.com/bbpcho/primitive-357-proof-audit/releases/download/audit-2026-09-13.1/2026-09-13_p5_literal_c_obstruction_dependency_closure_v1.zip) | 149,934,212 | No matching PDF and no nested archives; local SHA-256 matches the public API. |
| 387970666 / `audit-2026-09-13.1` | 561674379 | [2026-09-13_corrected66_predyadic_and_p2_place2_dependency_closure_v1.zip](https://github.com/bbpcho/primitive-357-proof-audit/releases/download/audit-2026-09-13.1/2026-09-13_corrected66_predyadic_and_p2_place2_dependency_closure_v1.zip) | 137,069,860 | No matching PDF and no nested archives; local SHA-256 matches the public API. |

The p=5 digest is `03f3bfe077372275e570dd2541c033ba9a3c0701c80fecadfe1b575f3991d6eb`; the rank digest is `ec90f7ce74fcdebfb3c398a7ac7da8426d590ff9abc0ef115e4824c0e2918248`. All ZIP member sizes were inspected, so an exact copy with a different filename would still have been checked. This negative result concerns the identified DS PDF, not a general licence clearance for these packages.

The local `PRIMITIVE_357_REPRODUCIBILITY_V3.tar.gz` (262,784,980 bytes; SHA-256 `99ef2fa0466277092ed39570748870648c08c596a68ecb50f55cfc5d59107f26`) also contains the same nested paper. **No standalone V3 archive is listed among the current public release assets.** The V3 component is present in the two affected public outer assets above. Neither the V3 TAR nor the older V3 upload ZIP/TAR appears as a tracked blob in the published Git history. This inventory makes no claim about previously deleted, externally hosted, or independently shared copies.

## Other listed public assets

The following are the author's paper/source or checksum records, not identified copies of the DS PDF. They need not be deleted for this exact-paper removal.

| Asset ID | Exact filename | Release tag |
|---:|---|---|
| 565438434 | [PRIMITIVE_357_ARXIV_SOURCE_PETER_CHOCIAN_V1.zip](https://github.com/bbpcho/primitive-357-proof-audit/releases/download/first-submission-2026-09-15.1/PRIMITIVE_357_ARXIV_SOURCE_PETER_CHOCIAN_V1.zip) | `first-submission-2026-09-15.1` |
| 565436930 | [PRIMITIVE_357_PETER_CHOCIAN.pdf](https://github.com/bbpcho/primitive-357-proof-audit/releases/download/first-submission-2026-09-15.1/PRIMITIVE_357_PETER_CHOCIAN.pdf) | `first-submission-2026-09-15.1` |
| 565437005 | [SHA256SUMS.txt](https://github.com/bbpcho/primitive-357-proof-audit/releases/download/first-submission-2026-09-15.1/SHA256SUMS.txt) | `first-submission-2026-09-15.1` |
| 563372399 | [PRIMITIVE_357_VERIFIED_MANUSCRIPT_2026-09-14.pdf](https://github.com/bbpcho/primitive-357-proof-audit/releases/download/verified-2026-09-14.1/PRIMITIVE_357_VERIFIED_MANUSCRIPT_2026-09-14.pdf) | `verified-2026-09-14.1` |
| 563371998 | [PRIMITIVE_357_VERIFIED_RELEASE_2026-09-14_V1.zip.sha256](https://github.com/bbpcho/primitive-357-proof-audit/releases/download/verified-2026-09-14.1/PRIMITIVE_357_VERIFIED_RELEASE_2026-09-14_V1.zip.sha256) | `verified-2026-09-14.1` |

The retained checksum files identify historical assets; retaining a checksum is not retaining the PDF itself. The release notes now mark the corresponding archive withdrawal. Automatic GitHub source ZIP/TAR downloads for the three tags derive from the clean Git trees described next.

## Published Git history

The public refs endpoint returned one branch and three tags. Every object ID exactly matched the local refs, including annotated tag objects. The local checkout is not shallow. Its full reachable history contains 12 commits and 309 unique blobs; main was `8e1b03f6084339ab9286b4e6c8c1618abbfb75c7` at inspection.

Every reachable blob with the target byte length, and every ZIP/TAR/GZIP-named blob, was checked. There is only one tracked archive across that history: the 41,554-byte `release/PRIMITIVE_357_ARXIV_SOURCE_REVIEWER_CORRECTED_2026-09-15.zip`, containing the author's TeX sources and no DS PDF. There is no direct matching PDF blob. Thus neither a Git-history rewrite nor deletion of a branch/tag is called for by this exact PDF's distribution.

The scope is all history reachable from the currently published heads and tags. This does not purport to inspect unrelated private, deleted, or third-party repositories.

## Independent removal verification

At **2026-09-15T12:56:48.545985+00:00**, all of the following checks passed:

- The public release list no longer contains asset IDs 565450862 and 563394734.
- Each corresponding public asset API endpoint returns HTTP 404.
- Both original browser-download URLs return HTTP 404 after redirects are followed.
- Cache-busted versions of those URLs also return HTTP 404.
- The p=5 and rank assets remain listed with unchanged digests.
- Public main remains `8e1b03f6084339ab9286b4e6c8c1618abbfb75c7`.

This supports the statement that the identified affected public GitHub downloads have been withdrawn. It does not describe files already downloaded by other people as recalled or erased.

## Reproducibility records

- `PUBLIC_RELEASES_BEFORE.json`: complete unauthenticated public API response before removal, including exact release/asset IDs, URLs, sizes and digests.
- `PUBLIC_REFS_BEFORE.json`: complete public branch/tag identity response.
- `scan_public_archive_copies.py`, `PUBLIC_COPY_SCAN.json`, `PUBLIC_COPY_SCAN.log`: read-only recursive archive and Git-object inspection. Nested ZIP, TAR and GZIP members and every member of the target byte length are checked; failures are not suppressed.
- `verify_public_removal.py`, `PUBLIC_REMOVAL_VERIFICATION.json`: requests, final HTTP statuses, effective URLs, response headers/bodies, and the explicit post-removal assertions.
- `PUBLIC_RELEASES_AFTER.json`: complete after-removal public release list.

No public mutation was performed by this inventory/review task. The parent performed the authorized release-asset withdrawals and note updates.

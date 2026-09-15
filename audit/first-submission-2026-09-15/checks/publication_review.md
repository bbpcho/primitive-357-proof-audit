# Bounded public-release review

Reviewed 15 September 2026 without modifying the repository, archives or Git history, and without network access. The control repository inspected was `work/verified_release_2026_09_14/control_repository` at commit `f65e4ed9e68fc4203b5339561b64f1a77f280691`. The first-submission component manifest identifies companion SHA-256 `fa0eaae5e193010a0714b1e72fd141f146e3e155148d530706258e3bb42e9a90` in its associated output record.

## Credentials and unrelated files

No credential candidate or unrelated personal-file candidate was found in the bounded scan.

The inspection covered 128 control-repository working files, the manifests and entries of the first-submission collection and its source/data, logical-audit, Magma and arXiv-source components, and their text-bearing files. The initial pass examined 2,330 ZIP entries and 2,078 archive text files, scanning approximately 84.6 MB of text including the control files. A recursive pass inspected the additional embedded historical ZIP, tar and gzip packets: 922 entries and 748 text files, approximately 81.2 MB, with no size/depth skips. Counts include repeated evidence where components preserve the same material.

The pattern checks covered private-key headers, common GitHub/OpenAI/Slack/AWS credentials, quoted credential assignments and passwords embedded in HTTP URLs. Filename checks covered environment/credential files, private-key stores, mailboxes, cookie/keychain directories and personal database formats. No such candidate was reported. The archive inventory consists of mathematical source, exact data, certificates, logs, papers and review materials; the inspected names did not identify unrelated personal collections. The known author identity and local/home paths are provenance, not credential findings.

Using the standalone Command Line Tools Git binary, I inspected all 263 objects reachable through the available local refs: eight commits, one tag, 75 trees and 179 blobs, approximately 4.45 MB. The same credential checks found no candidate in these objects, the local remote configuration or the HEAD reflog. This covers the locally available history, not inaccessible or deleted remote objects. Compressed mathematical binaries and PDF contents were not interpreted as executable objects or exhaustively decoded by this review.

## Public presentation

The first-submission companion README correctly identifies Peter Chocian's first submission, distinguishes other authors' literature from data-release versions, identifies the canonical paper, and states that the work is not proof-assistant certification or external human peer review. It also distinguishes checksums from arithmetic replay and retains the imported theorem/software boundaries.

The inspected older control-repository presentation needs these targeted updates when publishing the new companion:

1. `README.md` still presents the 14 September release and its manuscript as current. Add the new companion and canonical first-submission paper, retaining the old release as an identified component.
2. Its sentence saying that the audit does not claim fresh Magma executions must be explicitly scoped to the 14 September release. The companion now includes the separate seven-job Magma execution records. The dated `docs/PROOF_STATUS.md` can remain a historical record if it is clearly linked as such.
3. `NOTICE.md` incorrectly says the manuscript author is unresolved. The author is now supplied. No project-wide licence was selected in the material reviewed; identifying the author does not itself select one.
4. Add the companion's short boundary about proof-assistant certification and external human peer review to the public-facing repository README. The present README makes no explicit false claim of either, but “independent audit” should have the same clear scope there.

These are presentation updates, not findings of exposed credentials or a new mathematical defect. This review is a bounded contents and wording inspection; it does not independently determine the redistribution licence of every third-party reference or software component.

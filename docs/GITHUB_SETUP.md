# GitHub publication and arXiv source

The public repository is [bbpcho/primitive-357-proof-audit](https://github.com/bbpcho/primitive-357-proof-audit). The current computational companion is published under [`replay-companion-2026-09-15.2`](https://github.com/bbpcho/primitive-357-proof-audit/releases/tag/replay-companion-2026-09-15.2). Its [replacement audit](../audit/replacement-release-2026-09-15/README.md) binds the final archive, paper, source ZIP, external-input lock and fresh complete replay.

The canonical paper is Peter Chocian's **A computer-assisted proof**, with affiliation **Independent researcher**. This will be his first arXiv submission on the equation. No arXiv submission has been made; Dahmen's requested reply remains the submission hold. GitHub publication and arXiv submission are separate actions.

## Which file goes where

| File | Destination and role |
|---|---|
| [paper/manuscript.pdf](../paper/manuscript.pdf) | The current paper for readers. |
| [PRIMITIVE_357_ARXIV_SOURCE_2026-09-15_V2.zip](../release/PRIMITIVE_357_ARXIV_SOURCE_2026-09-15_V2.zip) | The small arXiv source package for use once submission is cleared. It contains `manuscript.tex` and `rank-proof.tex`; use pdfLaTeX with `manuscript.tex` as the main file. |
| `PRIMITIVE_357_REPLAY_COMPANION_2026-09-15_V2.zip` | The separately hosted GitHub computational companion. Extract it and follow its README to acquire pinned external inputs and run the complete offline suite. It is not an arXiv upload. |

Use the exact release links in the [repository README](../README.md). The source contains its bibliography and supplied author/affiliation. No contact email was supplied; arXiv account and submission-form information remain the author's responsibility.

## Records and scope

The replacement's fresh run covers 13 sector/interface records, 65 prior jobs and 16 rank-local checks, with the latter joined to five freshly generated inputs. Seven official Magma V2.29-10 executions and four negative controls remain separately authenticated earlier records; this replacement suite does not execute Magma. The 118-claim audit and 70 named imports retain their own scope. No proof-assistant certification or external human peer review is claimed.

The tags `first-submission-2026-09-15.1` and `verified-2026-09-14.1` identify earlier releases. Their large archive downloads containing the DS paper were withdrawn, as were the older p=5/rank downloads containing the BPS paper. Original identities and audit records remain as provenance. Historical manuscript dates and archive versions are not previous papers or arXiv submissions by Peter Chocian.

The replacement acquires the required unlicensed upstream inputs privately and retains only the identified licensed third-party exceptions with their notices. See [NOTICE.md](../NOTICE.md) and [EVIDENCE.md](EVIDENCE.md). Repository credentials are not release materials. Later changes require new artifact identities; sealed archives are not overwritten under an existing basename.

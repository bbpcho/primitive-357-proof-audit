# Proof status — 14 September 2026

The named Mordell–Weil rank-upper-bound and composition gate is **closed by the combined independent audit and adopted replacement checks**. The new release integrates those checks and the manuscript corrections. The GitHub control repository separately records publication readiness in its machine-readable status ledger. The extracted archive carries the final clean-extraction replay records and artifact identities; its supported entry point is `scripts/verify_release.py`.

| Mathematical interface | Audited conclusion |
|---|---|
| Corrected global squareclasses and local restrictions | All relevant fake Selmer classes are represented in the corrected 66-dimensional space; the selected complete local conditions give dimensions 66→23→22→20→19→18→15→12. |
| Complete local image at 7 | The actual closed-point image is nonzero; the cycle P4−P1 lies in the full fake kernel and has correction −1. Local Kummer dimension two forces fake-image dimension one. |
| Complete second-dyadic local image | Three independent actual fake images and a nonzero fake-kernel correction in a four-dimensional local Kummer group force fake-image dimension three. |
| Final containing quotient | Modulo the seven-dimensional diagonal, the quotient is exactly B⊕⟨c⟩, with dim B=4 and the same literal c used at 5. |
| Obstruction at 5 | Both coherent lifts of c are excluded; the true-to-fake comparison kernel is zero. Every coset c+B is therefore excluded. |
| Pure-septic Jacobian rank | The true 2-Selmer dimension and Mordell–Weil rank are both four; Sha[2]=0. |
| Saturation and finite coefficient coverage | H0=⟨D2,D3,D4,D5⟩ has odd index. H1=⟨D2,E,D4,D5⟩ contains H0 and is 5-saturated. The index of H1 is coprime to 400, so it covers J(K)/400J(K). |
| Global logarithms | Both split-23 logarithm branches are reconstructed. The annihilator of the finite-index subgroup H0 annihilates all of J(K). |
| Exceptional septic field | The conservative Hecke ambient argument and terminal trace comparison retain the earlier audited conclusion; no complete-newspace or old/new-subtraction assumption is introduced. |
| Cubic–quartic sector | The p=173 Kummer repair supplies the missing 2-saturation step. The stated published/Magma rational and twist rank/torsion premises remain explicit inputs. |

The completed rank proof is [RANK_GAP.md](RANK_GAP.md), despite the historical filename. The manuscript includes the argument in its rank appendix. [H0_H1_CORRIGENDUM.md](H0_H1_CORRIGENDUM.md) corrects an ambiguity in the preceding audit addendum without altering the sealed audit archive.

## Verification boundary

The new release must be read together with its final verification result. A manifest check establishes the identity and completeness of named files. Arithmetic replay reconstructs the specified calculations. The human-readable proof states why those calculations imply the local and global bounds.

The original historical PASS scripts alone do not contain all of the new local completeness proofs. The integrated route adopts the independent actual-field, geometric, finite-module and rank-composition checks. The absent historical p=7 cycle-3 workers are replaced mathematically by the supplied exact-data reconstruction; their absence is not hidden by a successful summary parser.

Published results remain bibliographic premises. Authenticated Magma transcripts remain computational premises where identified by the guide. No fresh proprietary Magma execution is claimed in the independent release audit. These boundaries apply to the complete theorem just as they did to the earlier sector reviews.

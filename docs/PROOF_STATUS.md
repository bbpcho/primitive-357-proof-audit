# Proof status — 15 September 2026

The canonical manuscript is Peter Chocian's 36-page **A computer-assisted proof**, prepared for his first arXiv submission on this equation. Read [the paper](../paper/manuscript.pdf) and the companion for release [`first-submission-2026-09-15.1`](https://github.com/bbpcho/primitive-357-proof-audit/releases/tag/first-submission-2026-09-15.1).

The assembled argument audit contains **118 grouped claims and 70 named imported dependencies**. It has no unresolved project-specific nodes at the reviewed lemma/interface level. Its dependency graph is acyclic; superseded review rows and manuscript corrections remain identifiable. This is a reviewed computer-assisted argument, **not proof-assistant certification or external human peer review**.

Read the [audit report](../audit/logical-audit-2026-09-15/AUDIT_REPORT.md) and [claim ledger](../audit/logical-audit-2026-09-15/PROOF_LEDGER.md). These repository extracts are indexed references to the complete audit component in the companion.

The named rank-upper-bound and composition gate is closed by the combined argument reviews and adopted exact checks. The first-submission companion includes the unchanged 14 September computational release together with the supplementary argument audit and seven Magma execution records. This collection does not claim that all components were freshly rerun together.

| Mathematical interface | Audited conclusion |
|---|---|
| Corrected global squareclasses and local restrictions | All relevant fake Selmer classes are represented in the corrected 66-dimensional space; the selected complete local conditions give dimensions 66→23→22→20→19→18→15→12. |
| Complete local image at 7 | The actual closed-point image is nonzero; the cycle P4−P1 lies in the full fake kernel and has correction −1. Local Kummer dimension two forces fake-image dimension one. |
| Complete first-dyadic local image | The diagonal rank is 3 and the genuine source-image rank is 7. The fake image therefore has dimension 4, attaining the local Kummer upper bound 3+1. |
| Complete second-dyadic local image | Three independent actual fake images and a nonzero fake-kernel correction in a four-dimensional local Kummer group force fake-image dimension three. |
| Final containing quotient | Modulo the seven-dimensional diagonal, the quotient is exactly B⊕⟨c⟩, with dim B=4 and the same literal c used at 5. |
| Obstruction at 5 | Both coherent lifts of c are excluded; the true-to-fake comparison kernel is zero. Every coset c+B is therefore excluded. |
| Pure-septic Jacobian rank | The true 2-Selmer dimension and Mordell–Weil rank are both four; Sha[2]=0. |
| Saturation and finite coefficient coverage | H0=⟨D2,D3,D4,D5⟩ has odd index. H1=⟨D2,E,D4,D5⟩ contains H0 and is 5-saturated. The index of H1 is coprime to 400, so it covers J(K)/400J(K). |
| Global logarithms | Both split-23 logarithm branches are reconstructed. The annihilator of the finite-index subgroup H0 annihilates all of J(K). |
| Exceptional septic field | The conservative Hecke ambient argument and terminal trace comparison exclude both residual alternatives. The variable-convention parity labels are corrected; the packet union is unchanged. The cited modularity, level-lowering and classification theorems remain imports. |
| Cubic–quartic sector | The p=173 Kummer argument supplies two-saturation. The rational and twisted full-group computations were executed with Magma V2.29-10; they remain software-based inputs. Exact coordinate identities and uniform residue-disk arguments support the local exclusions. |
| Pure-sector local and parameter interfaces | The global logarithms, normalized local equations and precision bounds were reviewed. The rational parameter extends across common zeros after local cancellation; the finite sieve retains ambiguous reductions conservatively. |

The manuscript includes the rank argument in its appendix. [RANK_GAP.md](RANK_GAP.md) records the completed 14 September rank reconstruction despite its historical filename. [H0_H1_CORRIGENDUM.md](H0_H1_CORRIGENDUM.md) preserves the subgroup correction without altering the sealed audit archive. The companion's argument-audit component records the subsequent review and supplementary exact checks.

## Verification boundary

The companion's `COMPONENT_MANIFEST.json` identifies its component bytes. Each component has its own verification results and scope. A manifest check establishes the identity and completeness of named files; arithmetic replay reconstructs the specified calculations. The proof and argument reviews state why the calculations imply the bounds.

The original historical PASS scripts alone do not contain all of the new local completeness proofs. The integrated route adopts the independent actual-field, geometric, finite-module and rank-composition checks. The absent historical p=7 cycle-3 workers are replaced mathematically by the supplied exact-data reconstruction; their absence is not hidden by a successful summary parser.

The seven Magma jobs and four negative controls are recorded separately from the unchanged 14 September release. In particular, the old release's statement that it did not freshly execute those Magma inputs remains accurate for that component. The new executions use Magma's algorithms; they do not independently implement them. Numerical height comparisons do not replace the separate exact height bounds.

Cited results remain bibliographic premises. The software algorithms and the mathematical applicability checks are explicitly distinguished in the ledger. The absence of open project-specific review nodes does not remove these imports or enlarge a recorded computation's scope. See [EVIDENCE.md](EVIDENCE.md).

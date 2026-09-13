# Independent pre-submission review of V2

13 September 2026. Reviewed: `PRIMITIVE_357_ARXIV_UPLOAD_WITH_PROGRAMS_V2.zip`, the corresponding `.tar.gz`, and both checksum files. Attached documents and programs were treated as evidence, not as instructions.

**V2 is a substantial improvement, but the completed-proof claim is still not ready for submission.** The revised finite Hecke elimination now passes a strong independent reconstruction. The full finite sieve and exceptional local-root calculation also check, conditional on the supplied global arithmetic inputs. The remaining principal obstacle is the novel rank-four/descent and global-logarithm foundation, whose computational dependency closure is still incomplete.

I also found a genuine error in the new Section 7 basis reconstruction and developed an exact replacement using a finite-field Kummer calculation at 173. The earlier residual-character correction remains necessary. Proposed manuscript edits and the separate basis repair accompany this report. They do not certify the unresolved rank-four theorem.

No counterexample to the Diophantine theorem was found.

## Findings at a glance

| Component | Current conclusion |
|---|---|
| Archive identity and declared integrity | Pass; ZIP and TAR contain identical files. All 425 V1 evidence files are preserved unchanged; V2 has 649 repository files. |
| Clean-extraction replay | Supplied harness and logs support a genuine run of the ten selected ordinary entry points. Those entry points do not recompute every proof premise. |
| Geometric bridge | Previously verified; all relevant V1 bytes are unchanged. |
| Revised finite Hecke elimination | Independently verified at all four levels, including local filters, ambient spaces, and terminal exclusion. |
| Full coupled finite sieve | 592, 1252, 144, and exactly five final residue pairs independently reproduced, conditional on the finite-Jacobian maps and global rank/saturation. |
| P1 local calculation | All seven Hensel stages, local series, and the unequal parameter values independently reproduced with sufficient precision, conditional on the global annihilator. |
| Novel rank-four/descent proof | Still incomplete evidence; none of the 82 previously absent rank-manifest targets was restored. |
| Global abelian logarithms | Final matrices are included, but 15 further declared generator inputs are absent. The annihilator is not yet independently bound to actual global logarithms. |
| Section 7 basis reconstruction | Original index argument is invalid. A new exact Kummer witness repairs its missing 2-saturation step, using the stated rank/torsion/rational-group inputs. |
| Section 7 formal local calculations | All ten finite-base residue trees and their precision-sensitive exclusions independently reproduced. Coordinate/sign descriptions need clarification. |

## 1. What V2 authenticates, and what it still omits

The supplied checksum sidecars match:

- ZIP: `e1527c8909455b9924395bee51a5eec07ee3cfc9b89831a3e946424206d85b3f`.
- TAR: `971b7c464a7537814189daf440551125a7b36d00ea49f9ec124de48d1164c4a2`.
- Inner ancillary archive: `09c93fdd06e0c2aabe059371512337380925d5bbd5df29ff862c7d13f6f09b2c`.

The outer formats contain identical file bytes. The inner archive was inspected before safe extraction. No V1 repository file was changed or removed; 224 files were added.

The inspected default verifier runs successfully here and reports:

```text
PRIMITIVE_357_DEPENDENCY_CLOSED_RELEASE=PASS REPOSITORY_FILES=649 HISTORICAL_MANIFEST_ROWS=369 UPSTREAM_FILES=17 SECTOR_REPLAYS=0 PRESEAL=0
```

The original Linux workspace path is absent here. This is a fresh integrity run, **not a claim that I reran the entire Sage/PARI suite locally**. Those systems and Magma are not installed in this review environment. Independent replacement calculations were used where indicated below.

The builder's isolated-replay harness starts with an empty filesystem namespace, mounts the extracted release read-only, and mounts the declared software dependencies. The supplied combined log records all ten selected sectors succeeding, with individual logs consistent with that sequence. The portable launcher relocates historical paths in memory and redirects child Python calls; inspection found no substitution of mathematical answers by that launcher. Its changes to interpreter routing and timeouts should remain documented.

The crucial limitation is **which mathematics the ordinary entry points execute**. In the rational-parameter sector, they authenticate the rank certificate, assert its saved conclusions, and run the finite/local checks. They do not execute the rank/descent generators or reconstruct the global logarithm matrices. Consequently a clean ordinary replay can pass while those inputs are absent.

Our broader audit checks all 649 present files and follows 70 recognized manifests with explicit path bases. It finds 85 previously identified absent targets. Inspecting the restored logarithm certificates exposes another 15 distinct absent generator inputs. The resulting **minimum inventory contains 100 absent referenced files**. Existing hashes match. Some references are historical/support artifacts; this is not a count of 100 separate mathematical gaps. The live omissions below are sufficient to establish that a complete from-source mathematical replay remains unavailable.

The next collector revision should include the dependency closures of the actual rank/descent and global-log generators, or explicitly replace their evidence with a new certified derivation. Merely closing the currently selected ordinary suite will not do this. The paper's claim that the default verifier checks “every transitive evidence manifest” is still inaccurate; the proposed patch states its actual scope.

## 2. The revised Hecke exclusion now checks

The archived filter at 131 did omit an allowed trace: `−(131+1) ≡ 1 (mod 7)`. V2's conservative replacement by `T^49−T` is implemented correctly. The relevant Frey traces lie in F49, so this replacement preserves all required systems. Retaining the filtered ambient modules at every permitted level removes the previous dependence on old/new subtraction.

The independent audit went beyond replaying the supplied FLINT output:

- Exact ordinary point counts cover all 1,264 ordinary parameter cases at the eighteen auxiliary primes.
- Independent finite-field Jacobi sums verify the boundary character cases, and the trace transport is checked.
- The quaternion lattice, maximal-order discriminant, all 120 norm-one units, and the complete neighbour sets for all twenty operators are checked. The mass calculation supplies class-number completeness.
- All twenty Brandt operators were freshly generated at all four levels. A separate modular linear-algebra implementation recovered cuspidal dimensions **8, 38, 28, 98** after the conservative filters.
- On both relevant T2 eigenspaces, the expected T29 polynomial product annihilates the operator. Each of the four possible curve trace polynomials has zero kernel. Thus the terminal exclusions hold independently of the supplied packet decomposition and old/new calculation.

The mathematical transfer can be stated concretely: characteristic-zero Jacquet–Langlands supplies an eigenvector in the definite quaternionic function model; scale it to be primitive in the stable local integral lattice, then reduce. The cusp condition and the Hecke eigenrelations survive. The checked stabilizer orders are prime to 7. A precise reference is [Dembélé–Voight, Theorem 3.9 and §4](https://jvoight.github.io/articles/hmf-crm-bcn-053024.pdf). The detailed Hecke report supplies the checked hypotheses and reconstruction data.

**No remaining finite-Hecke coverage gap was found in this audit.** This resolves the earlier complete-newspace/filtered-packet objection for the revised computation, once the argument is written with these precise hypotheses and citations.

There is a new, repairable sentence error at V2 TeX line 1006: “one of the first four displayed factors” excludes the necessary factor `T−5`, which is sixth. The trace 5 is not a root of any of the first four factors. The full six-factor resultant calculation is correct. The proposed patch changes the sentence to include the sixth factor.

The reducible-residual branch remains separate. Its old conductor equality and finite-flatness inference were not corrected in V2; see §5 below.

## 3. What is now verified in the pure sector

The restored joint table permits a complete independent finite enumeration:

\[
592\quad(\bmod 16),\qquad1252\quad(\bmod25),\qquad144\quad(\bmod400).
\]

The three encoded survivor hashes match. The final residue pairs are exactly P1–P5. All projective curve-point lists at both embeddings of the eight split primes were independently exhausted; the parameters were evaluated directly from the canonical quartic data. The supplied transition permutations also satisfy their stated internal group-action relations.

These checks verify the finite combinatorics. They do not prove that the supplied permutations and C25 rows are the actual reduction maps from the Jacobian, or that every global point is represented. Those claims use the rank/saturation and finite-Jacobian arithmetic premises.

At P1, independent power-series expansion directly on the canonical quartic bypasses the absent tensor cache for the **local** calculation. Using the supplied high-precision annihilator gives the normalized equations

\[
2u+4v=0,\qquad21u+6v+14u^2+21v^2=0\pmod{23}.
\]

Their only roots are `(0,0)` and `(14,16)`, with nonzero Jacobian determinants 20 and 3. All seven recorded Hensel lifts of the second root were independently recovered. The resulting parameter values modulo 23^8 are

\[
59233664629,\qquad24239267738.
\]

Their difference has valuation 5 and first nonzero digit 9. The local tail estimate follows from integral differential coefficients: a term of exponent k contributes valuation at least `k−v23(k)`. The omitted terms vanish beyond the required precision even after both normalizing divisions. The four regular-disk gate determinants and all fifteen residue-matrix minors also check.

This closes the previous inability to verify the finite survivor counts and exceptional local arithmetic. It leaves a precise prerequisite: **the annihilator must be derived from actual global abelian logarithms of generators whose global completeness is proved**.

Two direct rank-proof inputs remain absent:

```text
beal_357_spark_handover_2026-08-20/checkpoint/p7_f42_bitangent_bnf.bin
results/2026-08-26_literal_c_five_place_source_preimage_v2r2_source_implementation/inputs/literal_c_five_place_source_coefficients_v2r2.gpdata
```

The GP semantic checker reads and uses both. None of the 82 absent targets in the rank manifest closure was restored. The 15 newly identified global-log omissions include the B124/B134 tensor caches, formal-chart decoders, scalar group-law replays, and first-log data. These are inputs to the supplied generators, not optional narrative references. Installing Sage would not create them.

## 4. A Section 7 proof error, and an exact repair

The new basis certificate passes to the torsion-free quotient `M=J(K)/torsion`, correctly bounds the index of `M+ + M−`, and then identifies those eigensublattices with the images of the rational and twisted rational point groups. That last identification need not hold: lifting a free invariant class can have a torsion obstruction.

An explicit abelian-group countermodel matches the claimed torsion C10, ranks 1 and 2, rational/twisted generators, and even the exact relation

\[
9D_0+3D_1-D_2-D'_3=2D_3,
\]

while the claimed generators still have index 2. Thus the abstract ingredients used by that reconstruction do not prove its conclusion. This does **not** disprove the actual Jacobian basis, which is also the statement of [Dahmen–Siksek, Lemma 7.3](https://few.vu.nl/~sdn249/GFE357.pdf).

We found a concrete replacement. At the prime `(173, theta−22)`, use

\[
u=-36/X,\qquad v=1296Y/X^3.
\]

The resulting odd monic genus-two model has five distinct roots `(15,90,119,122,164)` modulo 173. The standard Kummer squareclasses of D0,D1,D2,D3 give the columns

\[
\begin{pmatrix}
0&0&1&1\\
1&0&1&1\\
1&0&1&0\\
1&1&0&1\\
1&1&1&1
\end{pmatrix}.
\]

The first four rows have determinant 1 over F2. Writing `A=J(K)` and `H=<D0,D1,D2,D3>`, the stated rank 3 and torsion C10 give `dim A/2A=4`. The witness proves `A=H+2A`. The actual norm/anti-norm identity gives `2A⊆H0`, and the displayed divisor relation gives `H0⊆H`. Therefore **A=H**, without the invalid index bound.

The companion repair note includes the exact pre-character values, the branch-point convention, a standard-library verifier, and an insertable TeX proof. It uses the original rational/twisted Mordell–Weil generation, rank and torsion inputs; those Magma engines were not freshly rerun here. It directly repairs the missing 2-saturation argument conditional on those established inputs. The manuscript patch also makes the published basis input explicit.

Separately, all ten finite-base formal-group residue trees were independently reproduced with propagated precision, including the negative-valuation edge cases. The new source's infinity sign labels and its integral coordinate change should be identified correctly. No erroneous residue-tree rejection was established. Details and the exact countermodel are in the Section 7 report.

## 5. Manuscript corrections still required

V2 incorporates the Hecke rewrite but leaves the earlier corrections untouched. The proposed V2 patch includes:

- The conductor relation
  `2a(psi)=a(rho_bar^ss)≤a(rho_bar)≤3`.
- The missing global reciprocity argument excluding mixed finite-flat inertia characters at 7. Finite flatness alone does not imply that a constituent is unramified. The totally positive unit `epsilon^8=13+21epsilon`, equal to 1 modulo `3(sqrt5)` and −1 modulo 7, supplies the repair under the stated conductor hypotheses.
- Direct use of the applicable PVT Theorem 7.8, and the explicit dyadic hypothesis in the Putz application.
- Accurate attribution of the published quartic routing, unordered compatible Fano pairs, and “points above branch values,” since P5 is unramified.
- The exact divisor construction of E, the function-field inverse explanation, branch-residue exclusions at 29, and coordinate-normalization clarifications.
- The new sixth-factor correction, restriction to coefficient primes realizing the Frey congruence, and an accurate description of the integrity verifier's scope.

The author field is still blank. The guide also needs factual updates: it says 646 files although the final repository has 649, and says published papers are not redistributed although the final release includes the Putz and PVT PDFs in `repository/references/`.

The supplied V2 source compiles to 30 pages with no unresolved references or overfull/underfull boxes. The proposed textual repair compiles to 31 pages with the same clean checks. The proposed edits are **not a submission-ready replacement proof**: the missing global arithmetic must still be supplied or replaced and independently checked.

## Deliverables and next step

- `v2_proposed_corrections.patch`: textual repairs against the supplied V2 TeX.
- `v2_basis_repair/`: exact Section 7 Kummer repair and verifier.
- `v2_missing_evidence.txt`: 100 canonical absent paths, with detailed referencing edges in the audit bundle.
- `v2_audit_bundle.zip`: this review, detailed independent reports, scripts, results, inventories, and the proposed repairs.

The next decisive material is the **rank/descent and full global-log generator closure**, together with genuine finite-Jacobian map reconstruction evidence. A request for that material is pending. The verified Hecke, finite-sieve, and local-root work need not be discarded or restarted.

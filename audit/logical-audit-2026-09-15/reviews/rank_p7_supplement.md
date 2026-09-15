# Supplementary logical audit of the three open 7-adic arithmetic claims

RANK-14, RANK-15 and RANK-18 can be closed as project-specific arithmetic obligations. The sources bind the same actual point differences and local components, the required Hensel/model-perturbation inequalities hold, and the nonzero fake-image cycle is genuine. This conclusion retains the separately audited geometric line/contact dictionary and BPS correction formula as explicit dependencies. In particular, a target's factor-degree profile alone does not prove its correction character is nonzero.

Let R denote `/Users/pcho/Documents/Codex/2026-09-13/ple/work/verified_release_2026_09_14/staging/PRIMITIVE_357_VERIFIED_RELEASE_2026-09-14_V1`. The actual implementations reviewed are `R/audit/work/rank_local/scripts/predyadic.gp`, `p7_witness.py`, and `p7_nonzero_source.gp`; the corresponding fresh release evidence is in `R/verification/rank_local`. The earlier detailed reports in `R/audit/work/rank_closure_audit/{p7_replacement,predyadic}` were read as explanations, then compared with these implementations and the actual arithmetic output. This audit leaves the source ledger unchanged; replacement rows are in `rank_p7_supplement.json`.

## RANK-14: the whole semilocal fake kernel

Here the base field is K=Q(s), s²=−7. The `main_narrow` construction at `predyadic.gp:81–105` identifies the number-field polynomial with the exact tower polynomial, embeds s with an exact s²+7 test, and uses the actual normalized universal line. The five explicit points are checked on the exact integral quartic. Its fourth point is `[5+s:400:0]`; its first is `[-113−139s:32925+11475s:−138600−57960s]`. Thus `Diffs[3]` is precisely the line ratio for z3=P4−P1, rather than an independently labelled stored class.

At lines 69–78, the program freshly computes `idealprimedec(FP_nf,7)` and compares the entire prime inventory with the supplied list. Every supplied local uniformizer is checked to have valuation one. The seven actual absolute (e,f) pairs are `(8,1),(8,1),(8,1),(4,1),(8,1),(4,1),(8,2)`, as the release log records. There is therefore no omitted local component.

The element tested is exactly `Diffs[3]/3`. It is converted to the integral-basis coordinate vector `bc`, and then multiplied by the square of a common rational denominator before calling `nfislocalpower(...,2)` at **each** of the seven primes. Multiplication by this nonzero rational square does not change the local squareclass. These are exact number-field/local-power tests, not an approximate target-only test. Independently, the same source computes valuation parity and the unit's Euler character at every odd component, and its known-point matrix agrees with the all-component square conclusion. The actual fresh log states `P7_Z3_OVER3_LOCAL_SQUARE=7` and gives the full decomposition above.

This proves that a square root can be chosen in every factor of L⊗K K7, with the same diagonal a=3 throughout. It is exactly the required full fake-kernel membership. It does not yet prove that the Kummer class is nonzero; that follows from the nonzero correction under RANK-15/16/17.

## RANK-15: the exact target and the true incidence fields

The worker reads the same exact `contact_data.json` reconstructed by the prior geometry check. It does not read a desired sign or a historical ROOT5 mask as an algebraic input. In coefficients over w²−w+2, it writes the degree-42 target polynomial as R0+wR1 and forms the exact rational polynomial

`F=R0²+R0R1+2R1²`.

The selected precision-100 shifted degree-eight factor has coefficient valuations `[1,1,1,1,1,1,2,1,0]`; its exact lifted integer coefficients are recorded in the JSON. Thus the exact modulus is Eisenstein, and the field A has absolute (e,f)=(8,1). Its derivative at the uniformizer has valuation seven. In A, the original **exact** target polynomial satisfies v(F(r))≥800 and v(F′(r))=7. Strong Hensel gives a true root r* with v(r*−r)≥793.

The precise field identification also follows. All seven other conjugates of the Eisenstein uniformizer have distance at least one; the derivative valuation, the sum of those seven distances, is exactly seven. Hence every distance is exactly one. Krasner's lemma applies to the radius793 lift, so r* generates the same degree-eight field. The rational expression w*=−R0(r*)/R1(r*) then satisfies w*²−w*+2=0 exactly because F(r*)=0; s*=2w*−1 embeds K7. Therefore A/K7 has (e,f)=(4,1). This is a genuine exact-field argument, not a claim that a finite-precision polynomial vanishing establishes an exact identity.

The denominator is checked stable before evaluating w. For an integral root, a rational polynomial h obeys

`v(h(r*)−h(r)) ≥ 793 + min_i v(h_i)`.

The worker's Gauss bounds use v_A(q)=8v7(q). The displayed quotient-error formula for w follows by expanding the difference of two fractions with a denominator of fixed valuation. For each coefficient f0(r)+w f1(r), the minimum of the two input errors and their cross terms is used. Those errors are installed with `add_bigoh`. At precision100 the smallest incidence/contact input bound is769; the incidence polynomial itself retains at least785. There is consequently no unaccounted denominator loss in transferring the exact target root to the contact/line inputs.

### The factorization error and why the line residues survive it

The incidence reduction is `(l−c)²` times an irreducible quadratic. These two factors are coprime modulo the maximal ideal, despite the repeated linear factor inside the first block. The computed monic quadratic pair has product error at least256. The unit-resultant factor Hensel lemma therefore supplies exact monic factors with coefficient differences at least256. This is the relevant exact factor-lifting statement; merely working in the displayed approximate quadratics would not suffice.

The first factor is translated by c and rescaled by l=c+a z, dividing by a². Its coefficient error is thus at least254. The second has no such loss, so its bound remains256. Both transformed reductions are irreducible quadratics over F7. They are unramified quadratic extensions, and their derivatives at the residue roots are units. Their true roots can be identified with the approximate-model roots within valuations254 and256 respectively. This proves the required profile `B1/A=B2/A: (e,f)=(1,2)` and supplies the field-isomorphism error needed for evaluation.

I checked the remaining evaluation loss by a short fresh read-only diagnostic of the already inspected worker. It removed only the final output-file write and printed the actual numerator, denominator and polynomial Gauss valuations before division. It completed in about two seconds and gave:

| quantity | first incidence factor | second incidence factor |
|---|---:|---:|
| v(line(P4)) | 10 | 8 |
| v(line(P1)) | 8 | 8 |
| Gauss bound of line(P4) polynomial after substitution | 10 | 8 |
| Gauss bound of line(P1) polynomial after substitution | 8 | 8 |
| exact-model root displacement lower bound | 254 | 256 |

For a polynomial evaluated at two integral roots, the displacement times its Gauss bound controls the difference. Therefore both numerator and denominator have **relative** errors at least254 in the first factor and256 in the second. The independent input-coefficient error769 is much larger; the point coordinates are integral and use the same controlled w, so it does not weaken these bounds. Both line ratios retain their valuations and normalized residue squareclasses after passage to the true incidence fields. This makes explicit a perturbation bridge that the earlier report described only briefly.

The line ratio divided by3 has valuations2 and0. After dividing by the appropriate even power of the A-uniformizer, the residues in F49 are squares. Both nonzero residue square roots are simple, so they Hensel-lift. Their norm residues are `u^4` in F7: if α²=u in F49, then Norm(α)=α⁸=u⁴. Both values are1. The first uniformizer contribution has norm a²; the second is trivial. Changing either square-root sign has norm1, because each incidence extension has degree two. Thus these values apply to the restrictions of any all-component square root from RANK-14, without needing to guess its sign.

The diagnostic also gave conic numerator and denominator valuations2 and0, with coefficient-input error at least769. Its relative error is therefore at least767. Combining this with the two incidence bounds shows that the normalized correction's residue is stable with margin at least254. The actual residue is6, i.e.−1. The original worker's stronger printed sign margin255 is consistent, but the logical conclusion only needs the proved positive margin.

Finally, the exact contact identity imported under RANK-03/16 gives `r(z)²=tau(f(z))`. With f(z)=3λ², the correction `r(z)/(3² tau(λ))` is exactly in μ2. Reduction at residue characteristic7 is injective on μ2, so the stable residue6 proves the exact correction is−1. A numerical near-square alone would not prove this; the exact identity is essential. Omitting the diagonal factor9 fails the worker's square test, and the different cycle z1 gives+1 as a useful calibration. The finite carrier audit in RANK-17 still supplies descent to the quotient; its profile has both zero and nonzero possible characters, so it is the actual−1 value that selects a nonzero one.

The source/input binding here is to the geometric dictionary already audited under RANK-03 and the complete finite carrier check RANK-17. This supplement does not infer either solely from the target's local degrees.

## RANK-18: an actual nonzero fake image

`p7_nonzero_source.gp` chooses a stored candidate by a rank-increase test and then verifies its mathematical existence; the selection is not itself the proof. The absolute model `z⁴+16z²+36` contains s=(z−6/z)/2 and i=(z+6/z)/2. Exact checks give s²=−7 and i²=−1. Fresh prime decomposition gives a single prime over7 with absolute (e,f)=(2,2), so the local source extension K7(i)/K7 is unramified quadratic.

The stored coordinate pairs a_j+i b_j specify an approximate point in that exact extension. The program transforms **both** the quartic and the universal line by

`(X,Y,Z)_original = (X,Y,−7Z)_local`.

At this approximate point the quartic, its X derivative and the coefficient content have valuations `(24,8,8)`. Dividing the quartic by an element of valuation8 gives integral coefficients and a unit X derivative; the residual value has valuation16. Strong Hensel therefore yields an actual point, with the Y,Z coordinates fixed and X changed by valuation at least16. The nonzero derivative also proves smoothness. No assumption that the original singular reduction was smooth is used.

The norm line is computed exactly as A²+B². The resulting 14-component squareclass vector is `[0,0,0,1,0,1,0,0,0,0,0,0,0,0]`. For every one of the same seven actual L-components, let m=min(v(A),v(B)). The two conjugate line values have valuations at least m; their valuation sum is v(A²+B²). Each is consequently at most v(A²+B²)−m. The Hensel correction changes a line value by valuation at least

`v(line_X) + (e_L/2)*16`.

The recorded differences from the preceding upper bounds are `[64,64,64,30,64,30,64]`, all positive. This argument also covers the final component where the quadratic source extension splits: apply it to the two individual conjugate factors. A ratio congruent to1 is a square at an odd residue prime, so the norm of the true point has the same squareclass as the approximate norm in **every** component.

The associated degree-zero cycle is Norm(P)−2P1. Dividing its line value by line(P1)² does not change the squareclass, which explains why the source can test the unnormalized norm line. The exact rank calculation gives diagonal rank2, rank3 after this column, and equality with the supplied allowed rank3 span. It proves a genuine nonzero fake image and identifies its line. It does not alone prove an upper bound; together with the domain dimension2 and the nonzero fake-kernel correction above, it gives the full image dimension1 as asserted in RANK-19.

## Audit scope

The all-component local-power calculation and genuine-source existence/rank values are supported by the prior fresh sealed replays, whose actual source and detailed valuation outputs were read here. They were not treated as mathematical consequences of a PASS label. The target worker was additionally run with read-only valuation diagnostics to close the factor-model transfer bound. No sealed file, manuscript, or existing claim ledger was modified. The remaining dependencies are the already separately audited global geometric/descent correspondence, not unresolved numerical or local-uniformity obligations in these three claims.

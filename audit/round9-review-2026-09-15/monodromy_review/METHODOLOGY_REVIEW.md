# Printed-cover monodromy: scope and methodology review

This review concerns the supplied `monodromy.gp` and report §9.2. The script is an independent calculation from the printed quartic and parameter coefficients, with `t_coeffs.gp` reconstructed separately from all 84 rational components in manuscript Table 2. No certificate-archive data are used by this replay. The supplied script is preserved unchanged; separate repaired code is labelled explicitly.

## Completed replay results

The supplied tracking completed at 400-digit requested precision, with 1617 accepted steps around 0 and 7661 around 1. Its permutations have cycle types 5³, 3⁵, and 7²1 for the inverse product. Exact breadth-first closure on those permutations has 2520 elements, a 15-point orbit, and every cycle-type count printed in the report. These results and the actual permutations are retained in `RESULTS.json` and `PERMUTATIONS.json`. The parent audit separately checks the abstract finite-group identification.

The repaired exact discriminant calculation gives valuations [12,10] and reduced degree 78. Its 78 numerical roots give the same two distance minima as the supplied diagnostic, so the diagnostic defect does not change these reported numerical minima. A follow-up checks the leading x-coefficient of the residual elimination polynomial, which has degree 4 in t: its four numerical roots are also away from the tracking circles, with minimum distances approximately 0.4966453494 and 0.1794188066. This addresses a separate possible finite-x chart issue; these distances remain numerical.

Two initial filename-based invocations returned only the opening stack-size warning and no calculation output; one also encountered an environment restriction in the external timing utility. Their logs are retained. The completed replay used GP with standard input redirection, and the recorded printed results—not exit status alone—establish what executed.

## Exact elimination and birationality

The construction `F=Res_z(Q,G+tH)` is exact over K=Q(s), s²=−7. So are the removal of the fixed base-locus polynomial B, the degree computations for F/B, and the computation of its discriminant before substituting the complex embedding. In the supplied replay they give deg_x F=20, deg_t F=4, deg_x(F/B)=15, deg_t(F/B)=4, exact divisibility, and a nonzero x-discriminant of degree 100 in t.

The report's birationality conclusion is valid together with its preceding exact divisor/degree calculation: the degree-15 map t has 15 points in a generic fibre, and the residual elimination polynomial has 15 distinct x-values. Hence x distinguishes those generic points, [K(C):K(x,t)]=1, and (x,t) is birational onto its image. Nonzero discriminant of an arbitrary elimination polynomial, without this account of the degree and base locus, would not alone supply all those premises. The separate exact-divisor review is responsible for checking that account here.

## Reproduced defect in the supplied discriminant diagnostics

The script applies `valuation` at t=0 and t=1 **after** evaluating s=i√7 at finite precision. Although 400 digits is ample for the numerical experiments, it does not preserve exact cancellation when translating the polynomial by t+1. The supplied run prints valuations `[12,0]`, contrary to its own expected `[12,10]`, and therefore labels 88 roots as 'other discriminant roots'. Ten of those belong to the t=1 fibre and should first be divided out exactly. These diagnostics are retained in `run_supplied/supplied_stdin.log`; a zero exit status is not treated as success of every printed check.

The repaired discriminant-only script computes both valuations and divides out t^v0(t−1)^v1 in K[t], then evaluates the reduced polynomial numerically. It saves its exact elimination polynomial and discriminant locally as `exact_model.gpbin` and deliberately does not rerun the root tracking. The complete difference against the supplied script is recorded in `DISCRIMINANT_REPAIR.diff`.

This defect does not alter F/B or the original tracking calculation, which uses that exact polynomial directly. It affects the interpretation of the discriminant-root list. The supplied distance minima are approximately 0.0274732840441173 and 0.0673547853662103; they are floating-point results, not certified lower bounds.

## Numerical root continuation

The script matches roots at consecutive endpoints by nearest neighbour, requires distinct matches, and rejects a step if any matched displacement exceeds one quarter of the smaller endpoint root separation. It starts with parameter step 1/200 and halves unsuccessful steps; all arithmetic root calculations use requested precision 400 digits. Endpoint rematching correctly converts the accumulated indices into permutations of the initial roots. The permutation composition and inversion formulas are consistent internally. The product order convention affects labels, not the reported inverse-product cycle type or generated group.

These checks are useful numerical safeguards, but they do not certify continuation between sample points. Small matched endpoint displacement cannot exclude roots moving around one another between the endpoints. There is no interval enclosure, Rouché argument, or certified pathwise root-separation/derivative bound. The discriminant-root distances are numerical as well. Accordingly the returned permutations remain numerical monodromy evidence; agreement with the exact passport is a consistency check, not a proof of path following.

Once integer permutations have been produced, group closure and their cycle statistics can be computed exactly. This separates the numerical source of the permutations from the exact finite-group calculations on them. An independently verified isomorphism of that generated group with A7 still does not make its numerical identification as the cover's monodromy exact.

## Identification, descent, and the sign of s

Conditional on the monodromy group being A7 and on the exact two-dessin classification, the cover is isomorphic over an algebraic closure to one of the two Fano covers as a cover of the labelled t-line. If both covers and their t-maps are defined over K and the cover automorphism group is trivial, such an isomorphism is unique: every Galois conjugate is another isomorphism, so uniqueness makes it Galois-invariant and hence defined over K. This descent argument is valid with those premises.

Conjugating coefficients by s↦−s sends K-rational points to K-rational points and fixes every rational t-value. Therefore a rational-parameter point theorem transfers to the conjugate cover. The numerical group and cycle statistics do not select the paper's orientation; saying that the *printed data themselves cannot decide it* is stronger than this computation establishes. The data specify a cover, while comparison with the reference Fano model and its orientation requires the missing exact identification information.

The appropriate status is **numerical corroboration of one of two Fano-cover identifications, conditional on the exact classification**. Calling it an 'exact identification given a numerical computation' risks confusing that boundary. The manuscript's exact forward/inverse function-field identities remain its proof of the identification and preserve the specified orientation; no change to that mathematical argument is warranted by this numerical replay.

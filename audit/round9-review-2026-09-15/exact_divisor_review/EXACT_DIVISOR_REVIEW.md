# Round 9.2: exact divisor and smoothness audit

The characteristic-zero divisor, degree and Belyi-passport conclusions of §9.2 are confirmed from the printed quartic, five points and Table 2. The supplied `exactdiv.gp` does **not** pass its final distinctness check as written. `exactdiv2.gp` successfully checks the non-base fibres; a separately identified supplement completes the missing common-base-point check. These results do not identify the cover with the Fano resolvent or certify numerical monodromy.

## Input binding and execution

The current manuscript has SHA-256 `70f66fe3605ecbde730e21fbee0308daaf0533fcd566d464274944066c3ef9cf`. All 30 rational quartic components, their 15 monomials, and every coordinate of the five points in both supplied divisor scripts match manuscript lines 1470–1484 and 1496–1500 exactly. `check_printed_binding.py` performs that comparison; its result is `PRINTED_QUARTIC_AND_POINTS_BINDING.json`. The convention is the printed coefficient `(U+sW)/2`, with `s²=−7`.

The scripts' referenced `t_coeffs.gp` was absent from the supplied package. The parent independently reconstructed it from all 84 rational components of the current Table 2; its SHA-256 is `ff7115896a14617e5ecf8cb8fb5cdf0550bb5387e474de2de461fe2cf601ae52`. The helper was inspected and copied unchanged into the isolated run directories. It defines only the two printed homogeneous quintics; it does not read archival coefficients or mathematical verdicts.

PARI/GP 2.15.4 was used. The first filename-argument invocation of `smooth.gp` exited zero after only the stack-size warning and produced none of the mathematical output. This is **not** a PASS. Both that log and the subsequent genuine standard-input execution are retained. All accepted executions fed the original script text to GP on standard input, with the generated helper available in the working directory. The supplied originals and manuscript were not edited. The stack-size warnings were retained; no other PARI error diagnostic appears in the accepted output. Exit status alone was never used to infer success.

## Smoothness: supplied script succeeds

`smooth_original_stdin.log` records:

- On `y=1`, the gcd of `Res_z(Q_z,Q_x)` and `Res_z(Q_z,Q_y)` has degree zero in x.
- On `y=0,z=1`, the gcd of the three partial derivatives has degree zero in x.
- At `[1:0:0]`, the printed derivative vector is nonzero.

These charts cover projective space. Any simultaneous partial zero on the first chart would force a common root of both resultants; their coprimality excludes it over the algebraic closure, not just over K. On the boundary chart the three-way gcd does the same. Thus the plane quartic is geometrically smooth. It is geometrically irreducible (distinct positive-degree plane components would intersect), and its genus is `(4−1)(4−2)/2=3`.

## Exact resultants: reproduced

`exactdiv_original/run.log` gives degree 20 for each of the three resultants. Their factor-degree/multiplicity lists over K=Q(s) are:

| Intersection | Factor degrees and multiplicities |
|---|---|
| Q with H | `(1,7), (1,7), (1,1), (5,1)` |
| Q with G | `(1,5), (2,5), (5,1)` |
| Q with G+H | `(1,3), (4,3), (5,1)` |

Their common monic factor B is irreducible of degree 5 and occurs once in each resultant. The three pairwise intersections have no point on `y=0`, including `[1:0:0]`. The quartic is monic of degree four in z, so projection to x on `y=1` is finite; there is no extraneous contribution from a moving leading coefficient or the projection centre `[0:0:1]`, which is not on Q. Equalities of resultants in the referee report should be read up to nonzero scalar, or with monic normalization.

Two supplied-code issues must remain visible:

1. At `exactdiv.gp:71–72`, the variables labelled “cubic A” and “quintic B'” take the **first irreducible factor**, which in each case is linear. The output correctly prints degree 1; these two lines do not check the entire reduced degree-3/5 fibres.
2. At `exactdiv.gp:89–92`, the high-priority x-polmod representation and generic gcd do not compute the intended polynomial gcd in z over the extension field. Every printed gcd degree is zero and the final output is `distinctness check passed: NO`. This output must not be relabelled a passed original check. Its nearby comment also understates the zero-fibre radical degree: it is 8, not 6.

`exactdiv2.gp` uses a lower-priority tower variable w and an explicit Euclidean gcd in z. Its unchanged run proves degree-one fibre gcds at all five printed points, with matching z-coordinate, and above the irreducible degree-2 and degree-4 factors. It deliberately omits the common quintic B, so a common factor of projected resultants alone would still not prove an actual common base point.

## Separate exact supplement: actual common base locus

`supplement/verify_common_base_and_fibres.gp` retains the reviewed coefficient construction and implements an additional explicit check over `K[w]/B(w)`. It finds that

`gcd_z(Q,H) = gcd_z(Q,G) = gcd_z(Q,G+H) = gcd_z(Q,G,H)`

are the **same monic linear polynomial**. The log prints degrees `[1,1,1,1]` and the exact common z-coordinate. This excludes the possibility that different points above the same x account for the three common resultant roots. Irreducibility and separability of B give five distinct geometric common points. Since B has multiplicity one in each resultant, the local vanishing orders of G and H at each common point are both one. Therefore the common base divisor is reduced, of degree five, and cancels exactly once.

The supplement also checks degree-one fibre gcds for every irreducible factor of all three resultants, the full squarefree reduced zero/one polynomials of degrees 3/5, their disjointness from B and each other, and the exact values at all five printed points. Its full output ends in `PASS_EXACT_COMMON_BASE_LOCUS_AND_FIBRES`; runtime was 15.73 seconds. No saved PASS flag or numerical monodromy value is used as an input.

## Mathematical conclusion and limit

Let A be the reduced degree-three divisor comprising P₁ and the degree-two closed point, and let C be the reduced degree-five divisor comprising P₂ and the degree-four closed point. The characteristic-zero calculations give

`(t)₀ = 5A`, `(t)∞ = 7P₃ + 7P₄ + P₅`, and `(t−1)₀ = 3C`.

Consequently t has degree 15, and A is K-rational. In characteristic zero the map is separable. These fibres contribute ramification `3(5−1)+5(3−1)+2(7−1)=34`; Riemann–Hurwitz gives the total `2·3−2+2·15=34`. Hence there is no other ramification and the passport is `(5³,3⁵,7²1)`. This also independently supplies the divisor premise used in the manuscript's construction of E and relation `5E=D₃+D₄+3D₅`.

This audit makes no claim that the passport uniquely identifies a cover. Exact Fano-resolvent identification remains the separate forward/inverse function-field argument. Numerical continuation and group enumeration belong to the other round-9 checks, not this result.

All original logs, supplement, input copies and result files are indexed by `ARTIFACT_INDEX.json`. Source SHA-256 values: exactdiv `b26d23bcc9947834acf6f9da13c52c5aece94634e0cb7faf22aeb4d04093ddc2`; exactdiv2 `eca57fc7ef5e6e678c48f6be23ecfff61c30bf53347e5d4c40f3912ec5232231`; smooth `79c6be823703464608a23398006811a70d986aae1f8e09de82ceae85bef43574`; supplement `f876c4aaaff0da2ec1b6c32f471df0a9a8dfd1264076d51e30f7602d942fbd81`.

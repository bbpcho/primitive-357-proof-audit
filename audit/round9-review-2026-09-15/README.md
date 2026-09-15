# Round 9: response and independent replay

This review assesses the newly supplied cumulative report's Section 9 and
`audit357_round9_scripts.zip` against repository commit
`4983db9561e00b69a0418d7e7139c333f90cb186`. The input digests are recorded in
`SUPPLIED_INPUTS.json`. The manuscript, rank appendix, 40-page PDF and
reviewer-corrected source ZIP still match their existing revision hashes;
see `BASELINE_CHECK.json`. This review does not change those files.

## Outcome

The report correctly withdraws its two earlier errors: the inference that
branch patterns identify the Fano parameter, and the suggested complete
splitting of the bitangent algebra at the selected prime above 1051.
The new exact counts and geometric computations supply additional checks
of the printed data. The supplied scripts require repairs and an omitted
input before their output can be treated as a reproducible audit.

| Check | Result and scope |
| --- | --- |
| S15 triple count | Both the supplied script and an independent character implementation give 1,591,439,705,856,000 triples and 1217 simultaneous conjugacy classes. |
| Two Fano actions of A7 | Direct independent permutation enumeration gives 5040 triples, two cover classes, centralizer order 1 and normalizer order 2520. This determines a pair of covers, not a selected plus orientation. |
| Quartic smoothness | Exact elimination on both projective charts passes. The 15 printed quartic coefficients and five points agree with the supplied programs. |
| Characteristic-zero divisors | Exact resultants and corrected fibre computations give the stated zero, pole and unit fibres. An additional check proves that the common quintic consists of actual common base points, each of multiplicity one. |
| Printed parameter | These checks give degree 15 and passport (5^3,3^5,7^2 1). They corroborate Appendix A directly from the printed data without using the withdrawn coefficient archive. |
| Numerical monodromy | The 400-digit run completed after 1617 and 7661 accepted steps. Returned permutations have the reported cycle types and generate a group of order 2520. A separate exact simultaneous-conjugacy check identifies that permutation group with the faithful Fano action of A7. Root continuation itself remains numerical. |

For the exact divisor check, the resultants factor over Q(s), s²=−7, as
follows; entries are [irreducible factor degree, multiplicity]:

| Resultant | Factor data |
| --- | --- |
| Res(Q,H) | [1,7], [1,7], [1,1], [5,1] |
| Res(Q,G) | [1,5], [2,5], [5,1] |
| Res(Q,G+H) | [1,3], [4,3], [5,1] |

The common degree-five factor has one simple common point of Q=G=H=0
over each root. All other resultant factors also have exactly one
intersection point over each root. There are no missing intersections on
y=0. Thus cancelling the common divisor gives pole orders 7,7,1, three
zeros of order 5 and five points above 1 of order 3. Their ramification
contributions are 12+12+10=34, the full Riemann–Hurwitz total for a
smooth genus-three curve mapping with degree 15 to the projective line.

## Corrections to the supplied replay materials

1. **Missing input.** Three programs call `read("t_coeffs.gp")`, but the ZIP
   does not contain that file. We reconstructed it from all 84 rational
   components in the current manuscript's Table 2, with 21 monomials per
   form and the printed coefficient convention (U+sW)/2. The generated
   coefficients and their binding to the manuscript are recorded separately.
2. **Incorrect tower computation.** The last block of `exactdiv.gp` uses
   an x-polmod with the wrong variable priority. Its actual output says
   `distinctness check passed: NO`; this is not a passed certificate.
   `exactdiv2.gp` uses the proper lower-priority tower variable for the
   non-base factors. Our additional exact check verifies every factor and
   the common base locus itself.
3. **Mislabelled squarefreeness checks.** The first script labels a selected
   first factor “cubic A” or “quintic B'” even though it has degree one.
   The supplement constructs the full reduced zero and unit-fibre
   polynomials and checks their degrees 3 and 5 and their squarefreeness.
4. **Floating-point valuation.** `monodromy.gp` substitutes s=i√7 before
   measuring exact vanishing orders at t=0 and t=1. Its supplied run gives
   [12,0], contradicting its expected [12,10], and labels 88 roots as other
   discriminant roots. The repair measures and removes both vanishing
   factors over Q(s) before numerical substitution. The repaired execution gives exact valuations [12,10] and a remaining polynomial of degree 78; numerical root count 78 and the two distance minima agree with that repair.
5. **Exit status is insufficient.** In the available PARI/GP build,
   filename-based invocation can stop after the opening stack-setting
   warning with exit status zero. Replays through standard input execute
   the checks. Empty logs, negative printed checks, and diagnostic errors
   are not counted as successful verification.

The original supplied scripts are preserved unchanged in the local review
workspace. Original failures and repaired/supplementary executions have
separate logs and identities. The publicly recorded results do not
represent an unchanged successful run of the supplied ZIP.

## Mathematical qualifications to Section 9

The exact count makes the earlier passport error concrete: there are 1217
cover classes with these branch types. Adding the Fano action of A7 narrows
this to **two** classes. The report's sentence “the monodromy group does”
should therefore say that passport plus that A7 action determines the
pair. The exchange is under the nontrivial automorphism of Q(s)/Q,
s↦−s; “conjugate over K7” can misleadingly suggest an automorphism fixing
K7. Non-isomorphism here means as covers of the labelled t-line.

Nearest-neighbour matching of numerical roots, even at 400-digit
precision with a small endpoint-displacement condition, does not certify
root continuation between the sample points. The program has no interval
or Rouché bound along each step. Exact arithmetic on the resulting
integer permutations does not turn their numerical derivation into an
exact monodromy proof. These computations are numerical corroboration;
the paper's exact forward and inverse function-field identities remain
its proof of the Fano identification and its orientation.

The report's descent-by-uniqueness argument is valid once the two covers
and their maps are defined over K7 and an isomorphism over its algebraic
closure has actually been established: a unique isomorphism is fixed by
Galois. Conjugation by s↦−s also correctly transfers the rational-parameter
point theorem. The present group statistics do not determine the
orientation; they do not prove that the printed data could never decide
it with a further exact comparison.

## Submission status

No new manuscript error has emerged in the portions checked here. These
checks do not rerun the Selmer, Coleman, sieve or Hecke computations, and
the numerical monodromy is not substituted for the exact Fano certificate.
There is no claim of proof-assistant certification or independent human
peer review.

The outstanding release work is unchanged: produce a complete replacement
companion with resolved third-party distribution arrangements, authenticate
its external inputs and dependencies, and replay it from a clean extraction.
Then update Section 8.5 to its actual available identity and rebuild the
PDF. The optional sentence about the two Magma proof flags can be added
in that source revision. The requested Dahmen reply is still pending;
no arXiv submission is recorded.

## Recorded evidence

- [Exact dessin count and permutation-group review](dessins_review/DESSINS_REVIEW.md).
- [Exact divisor review](exact_divisor_review/EXACT_DIVISOR_REVIEW.md).
- [Numerical monodromy review](monodromy_review/METHODOLOGY_REVIEW.md).
- [Independent exact recognition of the returned permutations](MONODROMY_GROUP_CHECK.json).
- [Local review file identities](LOCAL_REVIEW_FILE_INDEX.json).

This directory publishes the review, input identities, selected generated
data and recorded outputs. It is not a complete replay package. Script
locations in the detailed notes refer to the local review workspace, where
the supplied originals and separately identified repairs are preserved.
The supplied ZIP itself contains five programs and omits the coefficient
helper; publishing these records does not change that fact or replace the
full computational companion.

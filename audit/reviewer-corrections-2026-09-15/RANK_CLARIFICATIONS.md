# Rank clarifications: the place above 1051 and rational two-torsion

The reviewer is correct that **1051 splits in K=Q(s), s²=−7**. The further suggestion that the bitangent algebra splits completely is false at the place used by the proof. The exact arithmetic uses

\[
 v_{1051}=(1051,s-815),\qquad s\equiv815,\quad w=(1+s)/2\equiv408\pmod{v_{1051}}.
\]

At this place the degree28 bitangent algebra has residue factor degrees **1⁸2¹⁰**. Its local two-torsion dimension is4, as stated in the appendix. The historical word “nonsplit” described the bitangent algebra, not the quadratic base field. It should be replaced with an explicit prime and factor pattern.

The assertion **J(K)[2]=0 is correct**. It follows from transitivity on the28 bitangents together with their standard genus-three two-torsion realization. Full affine Galois image, and even the four-candidate classification, are unnecessary for this particular vanishing. The separate assertion dim C(K)=1 still uses the audited finite Galois-module computation.

## Suggested manuscript paragraphs

The following text is intended for the local-image table and the explanation immediately after it. Use “the four places where the bitangent algebra splits completely” in place of an ambiguous “four split primes” if the distinction is not already explicit.

```tex
The next cut uses the good prime
$v_{1051}=(1051,s-815)$ of $K$.  Although $1051$ splits in $K/\Q$,
the bitangent algebra at this place has residue factor degrees
$1^8 2^{10}$, so it does not split completely.  In particular
$L\otimes_K K_{v_{1051}}\simeq K_{v_{1051}}^8\times E^{10}$,
where $E/K_{v_{1051}}$ is the unramified quadratic extension.
The Frobenius action gives
$\dim_{\F_2}J[2](K_{v_{1051}})=4$.
The exhibited point images have rank four and therefore fill the local
fake image by Lemma~\ref{lem:rank-local-completeness}.
```

A short conceptual explanation can replace the unelaborated J(K)[2]=0 assertion near the start of “Excluding the complementary class.” This uses the appendix's existing E_Δ, R_Δ and q notation.

```tex
In fact, $J(K)[2]=0$ follows already from transitivity on $\Delta$.
Identify $E_\Delta^\vee$ with
$\F_2^\Delta/\langle\mathbf1\rangle$, using the standard dot product.
The bitangent realization gives
$J[2]\simeq R_\Delta^\perp/\langle\mathbf1\rangle$.
Each nonzero class has two complementary representatives of weights
$12$ and $16$.  If such a class were Galois invariant, its unique
weight-$12$ representative would have Galois-invariant support,
a nonempty proper subset of the transitive set $\Delta$.
This is impossible.  Separately, the finite Galois-module calculation
gives $\dim\mathcal C(K)=1$ for every transitive affine subgroup
compatible with the actual bitangent action.
```

If the referee wants the small code computation visible in the argument, add:

```tex
The weight enumerator of $R_\Delta^\perp$ is
$1+63T^{12}+63T^{16}+T^{28}$; it follows by taking the orthogonal
complement of the $315$ tetrad incidence vectors of rank $21$.
```

This weight statement was independently recomputed below. It is a property of the actual bitangent code, not an inference from transitivity of an arbitrary permutation module. Transitivity alone would not prove that the fixed part of E_Δ^∨ vanishes for an arbitrary28-point action; one must use the J[2] submodule.

## Exact arithmetic at 1051

The source inspected is, relative to the sealed release root:

`audit/work/rank_local/scripts/predyadic.gp`, lines58–67.

It factors the exact absolute degree56 bitangent polynomial. It verifies squarefreeness, selects exactly those factors for which the stored base element s_L reduces to815, checks that their degrees sum to28, and reconstructs all66 restriction columns. Its allowed-image calculation starts with the diagonal column, finds smooth finite-field point witnesses, and obtains total rank5; quotienting the rank1 diagonal leaves fake-image rank4. The invocation is `nonsplit_check(1051,815,...)`.

The sealed fresh replay `verification/rank_local/logs/predyadic_raw66.log`, line10, records:

```text
NONSPLIT_PASS=[1051, 815, [1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2], 66, 9, 5]
```

I reran the bounded factorization directly from `evidence/rank/repository/results/2026-08-20_descent_support/checkpoints/tower_exact.bin` using the previously compiled PARI/GP2.15.4 runtime. This was not a rerun of the large global descent. The results were:

```text
BASE_ROOTS=[236,815]
ABSOLUTE_DEGREE=56
BASE_S=815: DEGREES=1^8 2^10, DEGREE_SUM=28
BASE_S=236: DEGREES=2^2 4^6, DEGREE_SUM=28
BASE_W_815=408
```

The second line makes it important to specify which prime over1051 is used: the conjugate prime has a different factor pattern. The selected irreducible factors modulo1051 were

```text
x+52, x+75, x+255, x+270, x+297, x+478, x+509, x+934,
x^2+234x+145, x^2+343x+488, x^2+495x+410,
x^2+577x+793, x^2+680x+481, x^2+691x+117,
x^2+778x+122, x^2+815x+56, x^2+839x+558, x^2+898x+784.
```

The replay operation was:

```gp
T=read(".../evidence/rank/repository/results/2026-08-20_descent_support/checkpoints/tower_exact.bin");
P=T[2]; sb=lift(T[5]); p=1051; F=factormod(P,p);
/* Assert every factor has multiplicity one. */
/* For s0=815 or236, keep F[i,1] exactly when
   subst(sb,x,Mod(x,F[i,1]))==Mod(s0,p). */
/* Print the kept degrees and verify their sum is28. */
```

The prior exact geometry audit already identifies this stored polynomial and base element with the printed curve's bitangent field and the printed sign of s. This clarification does not infer that identification merely from the finite factor degrees.

## Why the local two-torsion dimension is4

The audited eight-coordinate model is

\[
 W=\{(a_1,\ldots,a_8)\in\F_2^8:\sum a_i=0\}/\langle(1,\ldots,1)\rangle,
\]

with the28 bitangents represented by the two-element subsets of the eight labels. At the unramified place above1051, Frobenius is an involution. The factor pattern1⁸2¹⁰ on two-element subsets corresponds to cycle type1⁴2² on the eight labels. The recorded representative is, in zero-based indexing,

```text
[0,6,2,4,3,5,1,7].
```

It has four fixed labels and two transpositions. An even vector fixed modulo the all-one vector cannot be sent to its complement, because Frobenius has fixed labels. Thus it is actually fixed. There are six coordinate orbits; the even-sum condition gives one independent equation, and quotienting the all-one vector removes one more dimension. The fixed dimension is therefore6−1−1=4.

A fresh enumeration of only the256 eight-coordinate vectors gave:

```text
FROBENIUS_FIXED_EVEN_VECTORS=32
J2_FIXED_CLASSES=16
J2_FIXED_DIM=4
FROBENIUS_BITANGENT_CYCLE_COUNTS={1:8,2:10}
```

Source: `audit/work/rank_closure_audit/predyadic/odd_decomposition_envelope.py`, lines15–24 and38–49. The existing full subgroup check, in `verification/rank_local/predyadic/odd_decomposition_envelope.json`, has the same unique matching involution class and fixed dimension. No replacement of4 by6 is justified.

## Why transitivity proves the global vanishing

The bitangent code proof above can also be viewed through the standard theta-characteristic description: evaluating the quadratic refinement attached to an odd theta characteristic on a fixed nonzero two-torsion vector divides the28 odd theta characteristics into subsets of sizes12 and16. A rational nonzero vector would preserve that partition. Transitivity excludes it.

For a direct exact check in the manuscript's R_Δ notation, I read the actual315 tetrad masks from

`evidence/p5/repository/results/2026-08-21_descent_galois/checkpoints/compatible_even_theta_733177_s237021.json`.

These masks were already independently bound to the actual geometric conics in `work/mathematical_argument_audit_2026_09_15/reviews/rank_geometry_supplement.md`. A fresh integer-bit Gaussian elimination found rank21. I constructed a basis of the7-dimensional orthogonal complement and enumerated its128 elements. The result was exactly

```text
TETRAD_ROWS=315
TETRAD_RANK=21
ORTHOGONAL_DIM=7
WORD_WEIGHTS={0:1,12:63,16:63,28:1}
```

The all-one vector belongs to the code. Quotienting by it gives64 classes, with exactly63 nonzero classes and one uniquely determined weight12 support for each. This proves the short transitivity argument without needing the four affine subgroup cases.

The separate existing global correction computation remains in `verification/prior/logs/global_transitive_correction_envelope.log`. It considers the four transitive affine subgroup cases of orders56,168,168,1344; the two order168 groups are distinct. Each has correction dimension1. This result must not be silently replaced by the transitivity argument for J[2].

## Provenance and scope

Sealed release root:

`/Users/pcho/Documents/Codex/2026-09-13/ple/work/verified_release_2026_09_14/staging/PRIMITIVE_357_VERIFIED_RELEASE_2026-09-14_V1`

Input SHA256 values:

| Input | SHA256 |
|---|---|
| `tower_exact.bin` from evidence/rank | `c5a0eb3d2743bae80a7d76d83eb4cd62f6636647eba9a1591bd046327146c40b` |
| `audit/work/rank_local/scripts/predyadic.gp` | `cd529267f5064e63ebbf62d9ebf6433918a191c637866a1dd32593cd34e2f245` |
| `verification/rank_local/logs/predyadic_raw66.log` | `26c7285c549c7fa960d90fb17095194b4f779a8559f983afcfa542f7952af3af` |
| `verification/rank_local/predyadic/odd_decomposition_envelope.json` | `864a695185bb011c5a142da084814b5ee70bde2d7c5a0c5bb7e61d09e6a7d362` |
| Actual315-mask JSON at s=237021 | `37355c1cd1b3de2c487f0720349be1396f2d01ad1394a5c68570f200e3c2642f` |

All inputs and the manuscript were read-only. Only this note was written. No change to a computational matrix, local dimension, rank conclusion, or sealed artifact is called for by either reviewer question.

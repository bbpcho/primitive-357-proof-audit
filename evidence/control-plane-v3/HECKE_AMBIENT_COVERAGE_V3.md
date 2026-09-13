# Hecke coverage through the local filters

## Why execution of the old program was not enough

Level lowering places a relevant residual representation in a newspace at
one of the four levels `22`, `23`, `32`, `33`. The historical FLINT logs do
not decompose the full cusp spaces. Before packet decomposition, the program
intersects the ambient Brandt module with eighteen kernels

    ker A_ell(T_ell).

Consequently, a packet count from those logs proves coverage only after one
shows that every relevant Frey representation satisfies every polynomial
condition. Nor is a characteristic-zero old/new dimension calculation by
itself a proof that residual packets survive reduction modulo 7.

## Exhaustive local-trace interface

The release now contains the complete authors' `GFE-5p3` repository snapshot
at commit `e88f914c577ab6cf9a45e5cdd82c1993477fb423`, including `GPcode.gp` and
the 6,253-polynomial `Outputs/Data.txt`. The new filter verifier performs the
following chain from those original bytes:

1. It independently reduces all 6,253 polynomials at all 37 primes modulo 7
   and obtains byte-for-byte equality with `p7_level23_data_mod7.m`.
2. It checks the generating loops: all ordinary parameters
   `t=2,...,ell-1`, all five values at `t=0`, and all three values at
   `t=infinity` are present.
3. It adjoins the level-lowering possibilities
   `+(N(q)+1)` and `-(N(q)+1)`.
4. For split primes it performs the required relative-degree-two transport
   `a -> a^2-2 ell`; for inert primes it conservatively permits every
   F_7-valued trace.
5. It forms the squarefree least common multiple of the resulting factors and
   compares it with each hard-coded FLINT polynomial.

This is the computational form of the published Mazur-method trichotomy:
ordinary reduction, the two degenerations `t=0,infinity`, or the
level-lowering case `t=1`. The general local formulas and the modularity,
level-lowering, integral Brandt/Jacquet--Langlands, and Hecke-equivariance
theorems remain explicit mathematical imports.

## The 131 defect and conservative repair

Seventeen archived filters agree exactly. At `ell=131`, however, the
archived degree-48 polynomial omits the allowed level-lowering trace `1`
modulo 7. The published data require that trace because

    -(131+1) = 1 (mod 7).

The replacement computation therefore does not use that filter. It replaces
it in memory by `x^49-x`, which vanishes on every element of F_49. This can
only enlarge the state space. No authenticated historical file is edited.

## Coverage without old/new subtraction

Let `V_N` be the full mod-7 cuspidal Brandt module at level `N`, and let
`W_N` be its intersection with the seventeen verified local conditions and
the conservative no-filter condition at 131. If a hypothetical Frey
representation is placed at level `N`, the local trichotomy above proves that
its Hecke system belongs to `W_N`. We never assert that `W_N=V_N`.

Fresh reconstruction and simultaneous packet decomposition give:

| level | dim W_N | packet count | T2=-1 packets | T2=0 packets |
|---|---:|---:|---:|---:|
| 22 | 8 | 4 | 1 | 2 |
| 23 | 38 | 14 | 2 | 10 |
| 32 | 28 | 12 | 2 | 3 |
| 33 | 98 | 24 | 5 | 11 |

The packet dimensions, with multiplicity, sum to `dim W_N` at every level.
Thus all 36 packets compatible with the proved local trace at 2 are retained.
Their residual `T_29` annihilators are

    T,
    T^2,
    T+2,
    T^2+5T+2,
    T^2+3T+4.

The terminal comparison already contains all five: `T+2` is the same
modulo 7 as its existing factor `T-5`. Together with `T-2`, the unchanged
six-factor terminal resultant matrix has all 24 entries nonzero modulo 7.

This proves coverage directly in the conservatively filtered ambient module.
No old/new subtraction is load-bearing, and no assertion that the replayed
space is a complete newspace is made.

## Replay

Run, in this order:

    python3 -B scripts/verify_hilbert_hecke_filter_coverage.py
    python3 -B scripts/verify_hilbert_hecke_ambient_coverage.py

The final markers are:

    PASS_HILBERT_HECKE_FILTER_AUDIT_WITH_REQUIRED_ELL131_CONSERVATIVE_REPAIR
    PASS_HILBERT_HECKE_CONSERVATIVE_FILTERED_AMBIENT_COVERAGE_NO_NEWSPACE_SUBTRACTION

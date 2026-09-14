# Completed rank reconstruction

The historical rank gap is closed. This document records the accepted proof and the exact group statement used downstream.

Let K=Q(sqrt(−7)), let J be the Jacobian of the printed genus-three quartic, and put Di=[Pi−P1]. Set

- H0=⟨D2,D3,D4,D5⟩;
- H1=⟨D2,E,D4,D5⟩, where 5E=D3+D4+3D5.

The exact relation gives H0⊆H1. They must not be conflated.

## Upper bound

The actual class/unit/support calculations give the corrected 66 global squareclass coordinates. Fresh restriction calculations and complete local-image proofs give

| Stage | Dimension |
|---|---:|
| Four split good primes | 23 |
| Nonsplit good prime 1051 | 22 |
| Place above 3 | 20 |
| Place above 5 | 19 |
| Place above 7 | 18 |
| First dyadic place | 15 |
| Second dyadic place | 12 |

The additional archived good primes and norm condition are redundant on this route. The 12-dimensional space contains the seven-dimensional diagonal. Independent exact coordinate calculations establish Q=B⊕⟨c⟩, where B is the four-dimensional fake image of H0 and c is the literal complementary class of the obstruction calculation.

Completeness at 7 uses the genuine full fake-kernel cycle P4−P1, with diagonal3 and nonzero augmented correction. Its target has relative ramification/residue degrees (4,1), and its incidence consists of two unramified quadratic extensions. A separate genuine closed point gives the nonzero allowed fake-image line. Its coordinate transfer is Z_original=−7Z_local. Local Kummer dimension two forces that line to be the entire fake image.

At the second dyadic place, the three actual fake images and the nonzero correction profile (0,1) exhaust a local Kummer group of dimension four. Every relevant sextic carrier is bound to a character of the actual correction quotient. This proves the entire fake image has dimension three.

At 5, the two coherent lifts of c have obstructions omega00=(1,0) and omega11=(0,1), whose difference is kappa5(rho)=(1,1). The sum-of-coordinates functional excludes both lifts. The actual local fake kernel at 5 is zero and the global correction generator restricts nontrivially, so the true-to-fake Selmer comparison kernel is zero. Subtracting a Kummer class from H0 excludes every fake coset c+B. Thus the true 2-Selmer dimension is at most four. The independently checked rank-four lower bound and absence of rational 2-torsion give

    dim Sel²(J/K)=rank J(K)=4,   Sha(J/K)[2]=0.

## What the saturation and logarithm checks now imply

Rank four makes H0 and H1 finite-index subgroups. The independent 2-saturation proves that H0 has odd index. The 5-saturation concerns H1, not H0. Therefore gcd([J(K):H1],400)=1 and H1→J(K)/400J(K) is surjective. This supplies precisely the global coefficient coverage consumed by the finite sieve. Full saturation at every prime is unnecessary.

The reconstructed logarithmic annihilator vanishes on H0. If nP lies in H0 for a nonzero integer n, its logarithmic value is n times the value at P. Characteristic zero therefore extends the annihilator to every P in J(K).

## Evidence and adoption

The release includes the class/unit and actual geometry foundations, the same-literal-c obstruction, independent local-image and correction proofs, exact linear algebra, and saturation/logarithm checks. The release guide identifies their portable runners and indexes. The complete release replay must reconstruct the adopted chain, rather than merely invoke the older rank-summary verifier.

The original completion contract and earlier open status remain historical records. The new proof and its H0/H1 correction are incorporated into the manuscript; earlier sealed audit bundles are not rewritten.

# Primitive (3,5,7): verified proof release

This repository records the computer-assisted proof of the nonexistence of nonzero primitive integer solutions to

\[
x^3+y^5=z^7.
\]

The independent rank audit is complete. The corrected global squareclass space, complete local images, 7-adic and dyadic kernel witnesses, and the obstruction at 5 give Mordell–Weil rank four for the genus-three Jacobian used in the pure-septic argument. The manuscript now states this proof chain and its precise saturation and logarithm consequences.

The integrated release is **`verified-2026-09-14.1`**, with asset **`PRIMITIVE_357_VERIFIED_RELEASE_2026-09-14_V1.zip`**. The final asset identity and replay decision are recorded in the release index and verification results. Earlier V3 and dependency-closure archives retain their original filenames and checksums.

The proof continues to use the stated published theorems and identified Magma computations, including the rational/twist Mordell–Weil and torsion inputs in the cubic–quartic sector. The new audit does not claim a fresh Magma execution of those inputs. Integrity checks, arithmetic replays and mathematical implications are distinguished in the evidence guide.

## Read the proof and its audit

- [Current manuscript](paper/manuscript.tex) and [compiled manuscript](paper/manuscript.pdf)
- [Rank proof appendix](paper/rank-proof.tex)
- [Current proof status](docs/PROOF_STATUS.md)
- [Completed rank reconstruction](docs/RANK_GAP.md)
- [Evidence and trust boundary](docs/EVIDENCE.md)
- [Programs and certificate guide](release/PROGRAMS_AND_CERTIFICATES.md)
- [Correction to the subgroup notation](docs/H0_H1_CORRIGENDUM.md)
- [Release procedure](docs/RELEASE_PROCESS.md)

Run the repository checks with `make verify` and rebuild the paper with `make paper`. These operations have their stated repository and build scope; they do not replace the mathematical replays.

From a clean extraction of the integrated release, run:

```bash
python3 -B scripts/verify_release.py
python3 -B scripts/verify_release.py --replay \
  --python /path/to/python-with-sympy-and-flint \
  --sage-python /path/to/sage-python --gp /path/to/gp \
  --output-dir /path/to/new-verification-output
```

Use the Python executable of the documented Sage environment. The programs guide identifies the input roots, adopted checks, generated records and imported premises. Failed arithmetic, missing dependencies and unresolved precision are failures, even when an underlying process returns exit status zero.

## Repository and immutable assets

Git tracks the paper, source checks, audit decisions, indexes and compact evidence. Large exact inputs are carried in the separately indexed release asset. Historical evidence remains identifiable; a repair creates a new release and a new manifest rather than changing a sealed archive under its old name.

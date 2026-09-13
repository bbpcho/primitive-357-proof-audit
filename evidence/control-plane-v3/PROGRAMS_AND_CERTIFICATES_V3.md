# Programs and certificates

This guide maps the mathematical claims in *The Primitive Generalized Fermat
Equation \(x^3+y^5=z^7\): From the Published Frontier to a Certified Proof*
to the programs and exact data included with the arXiv submission.

The files are stored in:

    anc/PRIMITIVE_357_REPRODUCIBILITY_V3.tar.gz

The archive preserves the original repository-relative paths.  It contains
765 evidence files, including 222 mathematical program sources:

- 138 Python programs;
- 39 PARI/GP programs;
- 25 SageMath programs;
- 20 Magma programs.

Seven release-level Python programs build and relocate the release, audit the
Hecke filters and ambient modules, run the foundational reconstruction, and
verify the release itself.
Exact
inputs, machine-readable certificates, package manifests, and authenticated
completed logs accompany the source.  Thus a reader can check integrity on a
plain Python installation and rerun the specialist layers when the relevant
computer algebra system is available.

## Quick verification

From the arXiv source directory:

    python3 -B VERIFY_SUBMISSION.py

Or unpack the ancillary archive directly:

    sha256sum -c anc/PRIMITIVE_357_REPRODUCIBILITY_V3.tar.gz.sha256
    tar -xzf anc/PRIMITIVE_357_REPRODUCIBILITY_V3.tar.gz
    cd 2026-09-13_primitive_357_dependency_closed_release_v3
    python3 -B scripts/verify_dependency_closed_release_v3.py

The last command uses only Python's standard library.  It verifies the root
manifest, the exact 765-file repository closure, all 369 rows of the original
52-manifest evidence base, the explicit added-dependency index, and the
complete four-sector proof graph.  It should finish quickly.

For the complete ordinary sector-level replay (Python 3.12, SymPy 1.14,
mpmath 1.3, PARI/GP 2.15.4, and SageMath 10.9):

    python3 -m pip install -r requirements.txt
    BEAL357_SAGE_PYTHON=/path/to/sage-python \
      python3 -B scripts/verify_dependency_closed_release_v3.py --run-sector-replays

The release already contains the combined clean-extraction log and ten
individual sector logs.  The builder produced them inside an empty-root
filesystem namespace in which the original workspace path did not exist.

## Claim-to-program map

All paths below are relative to the extracted release's `repository/`
directory.

### Main theorem and four-sector composition

The terminal proof graph and its seven authenticated dependencies are in:

    results/2026-09-10_complete_primitive_357_proof_v3/

Primary verifier:

    scripts/verify_complete_primitive_357_proof_v3.py

### Exhaustive descent-algebra routing

The exact routing to the four factor-degree sectors `[1,6]`, `[2,5]`,
`[3,4]`, and `[7]` is in:

    results/2026-09-09_signed_global_algebra_superselection_audit_v8/

Primary verifier:

    scripts/verify_signed_global_algebra_superselection_audit_v8.py

### Rational-factor sector `[1,6]`

The composition package is:

    results/2026-09-10_rational_factor_proposition_6_1_composition_v2/

Primary programs:

    scripts/verify_rational_factor_proposition_6_1_checkpoint_v2.py
    scripts/verify_rational_factor_prop_6_1_projector_v2.py
    scripts/verify_quadratic_field_lemma_6_4.gp

Its transitive packages contain the Mordell--Weil basis checks, sieve,
congruence and valuation exhaustion, Magma inputs, and authenticated rank and
Chabauty logs.

### Quadratic-factor sector `[2,5]`

The database-free router and terminal reconstruction are:

    results/2026-09-09_quadratic_factor_router_2_5_v1/
    results/2026-09-09_quadratic_factor_2_5_reconstruction_v1/

Primary programs:

    scripts/verify_quadratic_factor_router_2_5.py
    scripts/verify_quadratic_factor_2_5_reconstruction.py
    scripts/reconstruct_fake_selmer.m
    scripts/reconstruct_class41.m
    scripts/reconstruct_class42.m

The Magma logs authenticate the fake 2-Selmer computation and both terminal
Chabauty branches.

### Cubic--quartic sector `[3,4]`

The complete Section 7 composition package is:

    results/2026-09-10_section7_proposition_7_1_closure_v2_model_intrinsic/

Primary verifier:

    scripts/verify_section7_proposition_7_1_closure_v2.py

Its dependencies include the quartic-field router, Mordell--Weil basis and
sieve certificates, and the model-intrinsic bad-prime formal-group
calculation.

### Six pure irreducible septic fields

The sector composition package is:

    results/2026-09-10_irreducible_degree7_sector_closure_v1/

The exact Fano-resolvent and canonical-quartic programs are in:

    beal_357_spark_handover_2026-08-20/project/

Principal programs and data:

    p7_fano_resolvent_certificate.py
    p7_f42_cover_certificate.py
    p7_f42_modular_canonical.py
    p7_f42_canonical_reconstruct.py
    p7_f42_canonical_verify.py
    p7_f42_canonical_local.sage
    p7_f42_local_factor_certificate.py
    p7_f42_branch_jacobian.sage
    p7_f42_rank2_certificate.py
    p7_f42_canonical_exact.json.gz

These files verify the Fano planes and orbits, the plane quartic, inverse
maps, singularity resolution, five branch points, and the exact rational
parameter coefficients printed in Appendix A.  The sector dependencies also
contain the 2-descent, rank-four, five-saturation, sieve, and local-logarithm
certificates.

### Exceptional irreducible septic field

The Putz--PVT interface and the finite comparison package are:

    results/2026-09-10_pvt_putz_interface_audit_v2/
    results/2026-09-09_static_projector_seven_field_q29_compression_v1/

Primary programs:

    scripts/verify_pvt_putz_interface_v2.py
    scripts/verify_pvt_putz_interface_v2_package.py
    scripts/verify_seven_field_q29_spectral_compression_v1.py

The exact inputs record the variable and parameter maps, four possible
Hilbert levels, eight ray characters, four trace polynomials, six residual
polynomials, and the nonzero resultant comparison matrix.

### Hecke coverage through every preceding filter

The release-level verifiers

    scripts/verify_hilbert_hecke_filter_coverage.py
    scripts/verify_hilbert_hecke_ambient_coverage.py

first reconstruct all eighteen trace-polynomial interfaces from the upstream
6,253-polynomial data set. Seventeen historical filters match. The filter at
131 omits an allowed level-lowering trace, so the second verifier reruns all
four levels with that filter conservatively replaced by `T^49-T`. It then
decomposes the resulting filtered ambient modules completely, retains all 36
packets compatible with the necessary local trace at 2, and proves that every
resulting trace factor at 29 is already in the six-factor terminal resultant
comparison. This proves coverage through the filters and makes old/new
subtraction non-load-bearing. It does not call the filtered spaces full cusp
spaces or complete newspaces. The human-readable argument is
`HECKE_COVERAGE_AND_OLD_NEW_NOTE.md` in the arXiv source directory and
`HECKE_AMBIENT_COVERAGE.md` inside the extracted ancillary release.

## Meaning of the files

- `scripts/*.py`, `*.gp`, `*.sage`, `*.m`: verification or reconstruction
  programs;
- `inputs/*`: exact problem instances and ledgers;
- `certificates/*.json`: machine-readable conclusions and interface values;
- `logs/*`: completed output from an authenticated program/input pair;
- `summaries/*`: human-readable reports;
- `manifests/*SHA256SUMS.txt`: cryptographic bindings for packages.

The release includes checksum-pinned copies of the Putz thesis, the PVT preprint, and the earlier composition review in repository/references/.  General
theorems imported from Dahmen--Siksek, Putz, Pacetti--Villagra Torcomian,
Breuil--Diamond, Flynn, Bruin--Poonen--Stoll, Siksek, and Bruin--Stoll remain
bibliographic dependencies.  The bundled programs certify the
project-specific finite calculations; they do not purport to reprove those
general theorems.

## Software boundary

The default integrity verifier needs Python 3 only.  The complete ordinary
sector replay uses the pinned versions in `inputs/SOFTWARE_VERSIONS_V3.json`:

- PARI/GP for exact number-field arithmetic;
- SageMath for curve and finite-field computations;
- SymPy and mpmath for exact symbolic Python layers;
- Magma for selected descent, Mordell--Weil, modular-form, and Chabauty
  specialist recomputations beyond the ordinary replay.

For Magma-dependent layers, exact source, input, output, and authenticated
completed logs are included, so their interfaces can be checked even when a
licensed Magma installation is not available.


## V3 foundational replay

V3 adds the 100 evidence paths omitted from V2 and the independently checked
Section 7 Kummer repair. The complete generator map is
inputs/FOUNDATIONAL_REGENERATION_INDEX_V3.json; the file-by-file closure is
inputs/DEPENDENCY_CLOSURE_INDEX_V3.json. The V3 clean replay regenerates the
five-place rank/descent outputs and both global logarithm branches rather than
only authenticating their saved conclusions. The exact full command is:

    python3 -B scripts/verify_dependency_closed_release_v3.py \
      --run-sector-replays --run-foundational-replays

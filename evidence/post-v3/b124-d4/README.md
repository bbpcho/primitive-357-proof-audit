# B124 / D4 upstream reconstruction package

This is the missing upstream package for the `D4=P4-P1` column used by
`compute_p23_s4_full_log_matrix_v1.sage`.  It does not merely include the
saved first-log cache.  It includes the producer chain and every file that
the chain reads from outside its own directory.

## What is here

The mathematical chain is

```text
exact plane quartic
  -> B124 graded section-space/product lattices
  -> finite-field KM tensor and group-law checks
  -> tensor lift over Z/23^8 and Z/23^10
  -> two independent computations of the class 75(P4-P1)
  -> three-point formal-chart Newton decoding
  -> integration of (1,Y,Z)dY/F_Z
  -> D4 branchwise logarithm at the s = 4 place above 23
  -> four-column s = 4 global-log matrix (where D4 is reused)
```

Here `B124` means the degree-three base divisor `P1+P2+P4`.  The target
class is `D4=P4-P1`, whose reduction order is 75.

The important reconstruction files are:

- `repository/results/2026-08-31_p23_alternative_km_base_chart_screen_v1/scripts/build_p23_B124_graded_product_lattices_v1.sage`
- `repository/results/2026-08-31_p23_alternative_km_base_chart_screen_v1/scripts/build_p23_B124_padic_tensor_lift_v1.sage`
- `repository/results/2026-08-31_p23_alternative_km_base_chart_screen_v1/scripts/replay_p23_B124_padic_KM_scalar75_v1.sage`
- `repository/results/2026-08-31_p23_alternative_km_base_chart_screen_v1/scripts/decode_p23_B124_75D_formal_chart_v1.sage`
- `repository/results/2026-08-31_p23_alternative_km_base_chart_screen_v1/scripts/compute_p23_B124_first_branchwise_log_v1.sage`

The corresponding large or structured evidence files are included beside
them under `evidence/`:

- the exact graded lattice cache;
- the lifted multiplication tensors modulo `23^10` (with their `23^8`
  reductions);
- the two `75D` class computations;
- the decoded formal-chart points at both precisions; and
- the first D4 logarithm cache.

## The two previously external dependencies

The closure also carries:

1. `repository/beal_357_spark_handover_2026-08-20/project/p7_f42_canonical_exact.json.gz`,
   the exact plane-quartic model from which the B124 section spaces are
   constructed; and
2. `repository/results/2026-08-27_p23_branchwise_km_small_s4_probe_v1/scripts/replay_small_KM_group_law_and_75D.sage`,
   authenticated as a source-only provider of the `UnitKM` implementation
   and pivot helpers.  The B124 programs extract those definitions by AST;
   they do not execute that historical script's top level or depend on its
   old `/tmp` caches.

`UPSTREAM_DEPENDENCY_INDEX.json` records the precise role and SHA-256 of
every load-bearing node and the stage edges between them.

## Verify the package

From the extracted package root:

```bash
python3 scripts/verify_p23_B124_D4_upstream_package_v1.py
```

This checks the strict manifest, rejects symlinks and unmanifested files,
checks the dependency index and all named hashes, and checks the success
states of the JSON certificates.

With SageMath 10.9 available, also run:

```bash
BEAL357_SAGE_PYTHON=/path/to/sage-python \
  python3 scripts/replay_p23_B124_D4_upstream_v1.py
```

The replay works in a temporary clean copy.  It regenerates, in turn, the
lifted tensors, the p-adic 75D classes, the formal-chart points, and the D4
logarithm.  Each stage is compared to its sealed mathematical certificate;
the sealed handoff is then restored before the next stage.  This avoids
confusing nondeterministic elapsed times or Sage serialization bytes with
the mathematical payload.

The supplied logs split the completed clean replay at an authenticated
boundary: logs/CLEAN_TENSOR_REPLAY.log records the expensive tensor lift,
and logs/CLEAN_UPSTREAM_REPLAY_FROM_SCALAR.log records scalar 75D, formal-chart
decoding, and the D4 logarithm. Together they cover the formerly omitted
upstream segment.

To inspect the serialized objects without regenerating them:

```bash
BEAL357_SAGE_PYTHON=/path/to/sage-python \
  python3 scripts/replay_p23_B124_D4_upstream_v1.py --load-check-only
```

## Full reconstruction boundary

The package contains the original exact graded-lattice producer as well as
the sealed 39.9 MB result.  Rebuilding that first object from the canonical
quartic is deliberately not part of the short replay: exact function-field
Riemann--Roch and product-lattice construction can be long.  Its source,
checkpoint, final certificate, function-reduction audit, and cache are all
present, so it can be rerun separately under SageMath 10.9.  The short replay
starts from that authenticated graded-lattice boundary and reconstructs the
entire formerly omitted tensor/scalar/chart/log segment.

This package closes a provenance and reproducibility gap.  It does not add a
new rational-point or generalized-Fermat claim beyond the certificates it
contains.

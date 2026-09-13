# Rank reconstruction workplan

This is the concrete working queue for closing the only gate that currently
blocks theorem-level publication.

## Frozen starting points

The V3 foundational driver is tracked at
`release-tools/v3/run_foundational_replays_v3.py`.  It executes:

- the two five-place source-reconstruction workers;
- their semantic comparison;
- `certify_selmer_character_projector_rank4_v1.py`;
- the two split-23 global-log generators;
- the combined rank/annihilator and exceptional local gates.

The full payload for those paths is in the release asset
`PRIMITIVE_357_REPRODUCIBILITY_V3.tar.gz`.

Two dependencies identified after V3 are separate release assets:

- `2026-09-13_p5_literal_c_obstruction_dependency_closure_v1.zip`;
- `2026-09-13_p23_B124_D4_upstream_reconstruction_package_v1.zip`.

Their compact indexes, logs, and replay tools are under
`evidence/post-v3/`.

## Work packages

### R1 — Statement and dependency graph

Extract the exact rank, torsion, subgroup, and saturation claims from the
paper and every consuming verifier.  Produce a directed graph with no
unlabelled theorem edge.

Output: `R1_THEOREM_INTERFACE.json` and a readable report.

### R2 — Four-class lower bound

Rebuild the four divisor classes and an exact independence witness from the
canonical curve.  Check basis and base-point conventions independently.

Output: exact matrix, unit minor, source/input manifest, and second replay.

### R3 — Selmer upper bound

Reconstruct the dimension-four upper bound from the five-place local
conditions.  Incorporate the complete p=5 obstruction package and verify the
map from its carrier signs to the two quotient coordinates.

Output: full local-to-global dimension ledger, theorem hypotheses, and two
independent decisions.

### R4 — Torsion and saturation

Audit torsion and every prime that can divide the index of the displayed
subgroup.  State separately what the Section 7 mod-2 Kummer witness proves and
what comes from other computations.

Output: prime-by-prime saturation ledger and generation conclusion.

### R5 — Both split-23 logarithm branches

Rebuild every column from upstream class data.  The s=4 D4 column must traverse
the B124 tensor, scalar-75, formal-chart, and integration chain rather than
loading the saved D4 log as an unexplained premise.

Output: both 6-by-4 input blocks, precision ledger, rank witness, annihilator
basis, and high-precision replay.

### R6 — Downstream theorem use

Check the Mordell--Weil sieve, the five surviving residue pairs, the four unit
Siksek determinants, and the exceptional P1 calculation against exactly the
group statement proved in R1--R5.

Output: a consumption audit proving there is no hidden promotion from finite
index to equality.

### R7 — Composition and paper repair

Run everything from a clean extraction, obtain two independent decisions,
then update the manuscript and `audit/status.json`.

Output: either a proof-candidate tag or a permanent no-go report naming the
first failed implication.

## Order

Run R1 first.  R2 and R3 may then proceed independently.  R4 consumes both.
R5 can run in parallel with R2--R4 at the evidence level, but it becomes
load-bearing only after R4.  R6 consumes R4 and R5.  R7 is last.

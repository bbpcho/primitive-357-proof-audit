# Corrected-66 pre-dyadic and second-dyadic dependency closure

This package supplies the two upstream constructions requested during the
independent audit.

First, it derives the 18-dimensional array later copied as
`corrected_after_p7_basis_consumed_v1.txt`.  It starts with the corrected
displayed 66 squareclasses (28 ordinary units and 38 principal support-prime
generators, with the four p=29 generators replaced by the geometric HNF-22
packet), rebuilds every changed last-four column, and imposes the exact
pre-dyadic conditions in this order:

1. twelve split-good local conditions;
2. the corrected seven-row norm condition;
3. 57 admitted nonsplit-good local conditions;
4. the p=3 allowed subspace;
5. the p=5 allowed subspace;
6. the p=7 allowed subspace.

The cumulative constraint ranks are `43,43,44,46,47,48`; the corresponding
kernel dimensions are `23,23,22,20,19,18`.  The produced matrix is exactly
equal, entry for entry, to the 18-by-66 matrix consumed before the dyadic
cuts.  The two text files are not byte-identical: the downstream PARI/GP
producer reads the upstream file and writes the same matrix with GP's
whitespace serialization.  Both distinct hashes, the exact matrix comparison,
and the source-level read/write provenance are checked.

Second, it supplies the complete local inputs and both verifiers behind lines
112--171 of `P2_PLACE2_AUGMENTED_LOCAL_STOPPING_THEOREM.md`.  Production
constructs the full degree-28 fake-kernel relation `[1,1,-10]`; the
answer-independent replay uses the distinct relation `[1,0,2]`.  Both
evaluate the two degree-six target carriers and obtain the correction profile
`(0,1)`, proving a nonzero correction direction at the second dyadic place.

## What is included

Historical paths are preserved below `repository/`.  The package contains:

- the HNF-22 squareclass packet, its producer/verifier source, manifests,
  checkpoints, and exact support-principal witnesses;
- every one of the 222 files named by the corrected global-intersection
  certificate, plus the earlier inputs needed to rebuild those columns;
- the norm matrix, all split/nonsplit/support-place raw maps, every allowed
  local subspace, the intersection programs, frozen outputs, and independent
  audit;
- the corrected-66 exact-principal/square-witness audit used to identify the
  displayed generator space;
- the second-dyadic resolved-chart and augmented-correction programs, all
  five degree-42 contact inputs, the finite target-character reconstruction,
  the production checkpoint, and the independent precision-140 checkpoint.

`DEPENDENCY_INDEX.json` gives every packaged path, SHA-256 digest, size, and
role.  The top-level SHA-256 manifest is strict, sorted, and self-excluding.

## Verification

From the extracted package directory, the fast verifier performs an exact
tree audit, replays all historical manifests, independently reconstructs the
pre-dyadic intersection over F2, compares the two 18-row files, and checks the
second-dyadic relations and nonzero character:

```text
python3 -B scripts/verify_corrected66_predyadic_p2_place2_package_v1.py
```

For a clean arithmetic replay, with PARI/GP 2.15.4 available:

```text
python3 -B scripts/replay_corrected66_predyadic_p2_place2_v1.py \
  --log logs/CLEAN_CORRECTED66_PREDYADIC_P2_PLACE2_REPLAY.log
```

The replay copies only the package's `repository/` tree to a temporary
directory.  It rebuilds the corrected global columns, the norm certificate,
the 19- and 18-dimensional intersections, the production second-dyadic
checkpoint, and the distinct independent second-dyadic checkpoint.  The
original workspace is inaccessible to those computations.

## Claim boundary

The finite algebra is exact for the frozen displayed 66-generator space and
for the stated second-dyadic local inputs.  The BPS identifications and local
descent interpretation remain imported mathematics, exactly as labelled in
the historical theorem reports.  This package does not itself make a new
global Selmer, Mordell--Weil, rational-point, `(3,5,7)`, or Beal claim.

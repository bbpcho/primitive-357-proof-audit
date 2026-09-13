# Exact p=5 literal-c obstruction dependency closure

This release supplies the missing arithmetic behind the two nonzero
obstruction coordinates `(1,0)` and `(0,1)`.  It is a checkpoint-closed
replay package, not merely a copy of the two final JSON certificates.

The package starts from the exact target-42 root and contact data, carries
the frozen coherent-cocycle source and output closures, recomputes the three
physical p-adic carrier signs with two independent PARI/GP programs, and
checks their conversion to the two quotient coordinates used by the A.26
conditional rejection theorem.

## Contents

All historical paths are preserved below `repository/`.  In particular the
release contains:

* the target-42 relative root;
* the degree-42 contact cross matrix, CRT conics, and three contact lines;
* the exact tower and the local p=5 condition;
* the coherent target42/size56 cocycle producer closure and its sealed
  outputs;
* both p=5 arithmetic programs and their frozen output records;
* the target-character rank-two calculation and its two imported source
  modules, the partition-gauge package, and the A.26
  true-lift gate inputs;
* the prior independent declared-hash-closure auditor.

`DECLARED_DEPENDENCY_INDEX.json` records the dependency roles and exact
digests.  `P5_LITERAL_C_OBSTRUCTION_DEPENDENCY_CLOSURE_V1_SHA256SUMS.txt`
is strict and self-excluding.

## Verification

From the extracted package directory:

```text
python3 -B scripts/verify_p5_literal_c_obstruction_package_v1.py
```

This performs a byte-level tree and declared-closure audit without doing
new arithmetic.

For the decisive arithmetic replay, PARI/GP 2.15.4 is required:

```text
python3 -B scripts/replay_p5_literal_c_obstruction_v1.py --log logs/CLEAN_P5_OBSTRUCTION_REPLAY.log
```

The replay copies only the bundled `repository/` to a temporary directory,
runs the production p=5 calculation, the answer-isolated verifier, and the
independent finite target-character rank calculation.
The original workspace is not available to either computation.  Newly
generated records must equal the two supplied frozen PARI/GP objects exactly;
the verifier deliberately compares deserialized mathematical objects rather
than the incidental binary serialization bytes.

## Exact conclusion and boundary

The arithmetic carrier signs are `(-1,+1,-1)`.  With the certified
rank-two character relation, the coherent roots `[00]` and `[11]` give
respectively `(1,0,1)` and `(0,1,0)`, hence coordinates `(1,0)` and `(0,1)`
in the `(rq_1,rq_2)` basis.  Both are nonzero.

This is the exact local/checkpoint dependency closure for that obstruction.
Its interpretation as the A.26 rejection remains conditional on the
imported BPS exact sequence and the accepted same-literal-c source witness,
exactly as stated by the original theorem certificate.  The package makes
no broader Selmer, rational-point, `(3,5,7)`, or Beal claim.

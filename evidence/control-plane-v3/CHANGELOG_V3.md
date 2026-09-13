# Changelog: dependency-closed V2 to V3

1. Restored all 100 paths in the independent review's missing-evidence list.
   The files were present in the working repository but absent from V2.
2. Replaced sampled-sector closure claims by a complete 765-file repository
   index with SHA-256, byte size, role, and reverse reference information.
3. Added a foundational replay entrypoint that freshly runs both five-place
   workers, compares their exact semantics, replays the Selmer projector,
   reconstructs both split-23 global logarithm matrices, and recomputes the
   combined annihilator and exceptional local calculation.
4. Added the Section 7 finite-field Kummer certificate at
   (173,theta-22), its independent cross-check, logs, code, and explanatory
   text. This replaces the invalid abstract index inference.
5. Incorporated the independent review's corrections to attribution, local
   factor patterns, the explicit Fano/function-field bridge, fifth saturation,
   PVT theorem use, conductor bounds, residual-character reciprocity, Hecke
   transfer, terminology, and bibliography.
6. Corrected the Hecke sentence to include the sixth displayed factor T-5.
7. Corrected the release guide's file counts and redistribution statement.
8. Added the complete V2 independent-review bundle and checksum as provenance.
9. The first V3 foundational rehearsal exposed one missing Sage import in the
   historical s=19 full-log generator. V3 preserves that source and adds a
   separately hashed replay copy whose only change imports identity_matrix.

V2 remains unchanged. No historical evidence byte is edited in V3; restored
inputs are copied at their original repository-relative paths.

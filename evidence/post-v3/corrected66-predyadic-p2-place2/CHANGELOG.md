# Changelog

## V1 — 2026-09-13

Created in response to the independent audit's identification of two omitted
upstream dependency chains.

- Added the exact corrected-66 construction and all norm/local conditions
  producing the pre-dyadic 18-space.
- Added an exact 18-by-66 matrix-equality gate between the original producer
  output and `corrected_after_p7_basis_consumed_v1.txt`, while recording their
  distinct hashes and GP whitespace reserialization provenance.
- Added both second-dyadic fake-kernel cycles, all degree-42 carrier inputs,
  the production evaluation, and the distinct precision-140 verifier.
- Added a clean-extraction arithmetic replay and a fast independent finite
  replay.
- Preserved all historical artifacts unchanged; this is a new closure, not a
  repair in place.

## Packaging repairs found by clean replay

- Replaced an initial, incorrect byte-identity claim for the two 18-row text
  files with the stronger relevant statement: they parse to the exact same
  18-by-66 integer matrix.  Their distinct frozen hashes and the downstream
  GP read/write provenance are now explicit.
- Made the global-column replay compare every regenerated matrix and all 16
  components of the GP checkpoint semantically, then restore the frozen text
  serialization before replaying the historical hash certificate.  This
  handles GP's environment-sensitive whitespace/binary serialization without
  weakening the arithmetic comparison.
- Moved the regenerated second-dyadic checkpoint inside the clean extraction
  after its producer correctly rejected an output path outside the extracted
  repository.
- During diagnosis, one rebuild was mistakenly launched from the workspace
  root and temporarily reserialized 74 historical global-replay outputs.
  They were immediately restored from the pre-existing exact package snapshot.
  All 74 contents, including checkpoint and certificate, were then rehashed
  to their original manifest-bound identities before the final archive build.

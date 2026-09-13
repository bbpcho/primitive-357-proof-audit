# Packaging and replay changelog

This records release-engineering changes only. The historical mathematical
producers and evidence files under repository/ are unchanged.

1. The release collected the complete historical B124 directory, the exact
   canonical quartic, and the source-only UnitKM helper provider into one
   dependency-indexed package.
2. The portable launcher redirects the historical fixed workspace root into
   an isolated copy, so the original workspace is not used during replay.
3. The first clean tensor run exposed a wrapper-only marker spelling error:
   the producer correctly emitted P23_B124_PADIC_TENSOR_STATUS, while the
   new wrapper expected a TENSOR_LIFT variant. The wrapper was corrected.
4. That clean tensor run completed all four degrees and passed the invariant
   certificate comparison. The following scalar stage likewise completed,
   exposing the analogous wrapper expectation PADIC_KM_SCALAR75_STATUS
   versus its actual P23_B124_PADIC_KM_STATUS. The wrapper was corrected
   before the downstream replay. The formal-chart marker was checked
   directly against its producer and corrected at the same time.
5. Certificate comparison removes only runtime, path-root, and serialization
   metadata: wall_seconds, elapsed_seconds, and cache descriptors.
   Mathematical fields are compared exactly.
6. The start-stage option was added so a reviewer may resume at any
   authenticated boundary without repeating the approximately twenty-minute
   tensor lift.

No repair changed a mathematical producer, an input, or a sealed historical
certificate.

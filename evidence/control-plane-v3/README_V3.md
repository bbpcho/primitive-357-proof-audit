# Primitive (3,5,7) proof and reproducibility release V3

V3 responds directly to the independent V2 review. It retains V2 byte-for-byte
as its base, restores all 100 omitted transitive dependencies, adds an explicit
generator-to-input index, exposes the rank/descent and global-log generators as
a required clean replay, and supplies the independent finite-field Kummer
repair for the Section 7 two-saturation argument.

Fast integrity and Kummer checks:

    python3 -B scripts/verify_dependency_closed_release_v3.py

Full clean mathematical replay:

    python3 -B scripts/verify_dependency_closed_release_v3.py       --run-sector-replays --run-foundational-replays

The sealed build additionally runs that command inside an empty-root
bubblewrap namespace with the original workspace path absent. See
logs/CLEAN_EXTRACTION_COMPLETE_REPLAY_V3.log and
inputs/FOUNDATIONAL_REGENERATION_INDEX_V3.json.

The paper source incorporates the independent review's mathematical and
attribution corrections. The author field remains deliberately blank until
the submitting author supplies the desired name and affiliation.

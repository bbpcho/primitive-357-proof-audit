# Independent ledger assembly review

Reviewed 15 September 2026. This is a bounded review of the assembly logic and evidence joins, not another execution of the mathematical calculations.

I read `checks/assemble_ledger.py` and independently checked the assembled `PROOF_LEDGER.json`: 118 unique claim nodes, 70 named imports, an acyclic dependency graph, and consistent reconstruction of transitive open claims, transitive imports and closure statuses. The source-ledger input hashes and manuscript hashes agreed. Every recorded old/new manuscript replacement reproduced the separate corrected draft exactly.

The seven superseded open rank premises have explicit matching geometry, seven-adic or global-foundation supplements. Their former rows remain in the history. The terminal rank update is identified as a parent aggregation and retains its previous row; it does not replace its individual premises. The three corrected manuscript claims retain their source claim and status and point to the distinct draft changes. I found no hidden open-status overwrite or imported result converted into a project-specific proof.

Two citation/dependency metadata repairs found during this review are now applied:

- Dembélé–Voight Theorem 3.9 and §4 now links to the Hilbert modular forms article, rather than the quaternion book: <https://jvoight.github.io/articles/hmf-crm-bcn-053024.pdf>.
- PURE-14 now explicitly depends on `Siksek:Theorem2`, with the primary theorem at <https://msp.org/ant/2013/7-4/ant-v7-n4-p01-p.pdf>, p. 776. Its general theorem remains an import; the application is the checked claim.

The first-dyadic upper bound also now has direct provenance in RANK-FIRST-DYADIC. Its dependencies include RANK-02 and BPS Remark 11.6, and its evidence includes the source, result and log `checks/support/dyadic_decomposition_envelope.py`, `.json` and `.log`. The parent reran this unchanged exhaustive source; the result records all 95 subgroup classes and all five classes with the actual first-place orbit degrees `[4,6,6,12]`, each with fixed two-torsion dimension 1. Thus the local Kummer dimension is `3+1=4`. The previously replayed actual-source log records ranks `[1,3,6,7]`: diagonal rank 3, rank 6 after the global point differences, and rank 7 after the true local point. This supplies the matching lower bound `7−3=4` in the same actual-completion coordinates. I checked the newly cited records and ledger join without rerunning this calculation myself.

No further assembly defect was found. The closure label means a reviewed argument with explicit mathematical and software imports. It does not mean proof-assistant certification, an independent implementation of every imported algorithm, or an external human specialist review. The evidence index remains explicitly an index of cited files, not a transitive replay manifest.

# V5 aggregate count correction and downstream scope

The correct sum of the eight authenticated support-table cardinalities is

199728 + 3942 + 15426 + 17766 + 155 + 25 + 133 + 7 = **237182**.

`check_completed.py` independently counts the distinct seven-entry rows of every actual archived table, authenticates each table against its sealed ledger hash, and compares those counts with all eight successful V5 log lines. The incorrect number 236182 is a reporting aggregate, not the cardinality of a ninth mathematical object or a deduplicated union. The tables have their separate declared residue moduli and are compared individually.

The source-owned arithmetic checks in `results/2026-09-09_putz_hunter_local_tschirnhaus_support_v5/scripts/verify_putz_hunter_local_tschirnhaus_support_v5.py` use the eight `EXPECTED_COUNTS` values (lines 56–65), verify the imported sets (lines 505–524), enumerate the full finite domains, and compare each generated support for exact equality (lines 541–555). The erroneous aggregate appears only in the print statement at line 562. It is not used as an enumeration bound, truncation limit, sieve cutoff, normalization constant, or numerical estimate.

Within the V5 package the error is also present in the ledger's `totals.rows` (line 60), the decision certificate's `exact_results.total_imported_rows` (line 35), and the report TeX (abstract line 35 and total row line 162). The actual report PDF repeats it in its abstract and table. The original source, ledger, certificate, report and observed logs remain unchanged, with their tested identities preserved.

The old label was propagated downstream. In particular:

- `results/2026-09-09_static_projector_end_to_end_proof_candidate_v14/scripts/verify_static_projector_end_to_end_proof_candidate_v14.py`, `check_exact_foundations`: line 136 requires the graph's local-support statement to contain `236,182`; line 150 requires the V5 decision's stored aggregate to equal 236182. These are authenticated metadata consistency assertions. The actual finite support checks remain the eight set equalities in V5. V14's output summary at line 264 repeats the old label.
- `results/2026-09-09_static_projector_end_to_end_proof_candidate_v15/scripts/verify_static_projector_end_to_end_proof_candidate_v15.py`, line 179, prints the old aggregate inside its chain label. Its stored graph and decision descriptions also repeat it.
- `results/2026-09-10_irreducible_degree7_sector_closure_v1/scripts/verify_irreducible_degree7_sector_closure_v1.py`, line 166, requires the dependency ledger's chain string to contain the old aggregate. This is another metadata/interface equality, not a mathematical operation on the support rows.
- The V14 graph/decision, targeted Hunter V7 descriptions and irreducible dependency/report descriptions repeat the same reporting value. `TOTAL_LABEL_OCCURRENCES.json` gives the source lines, text and file hashes found in the frozen v3 `results` tree and the independently extracted V5 PDF occurrences.

Consequently, it would be inaccurate to say that *no verifier assertion depends on the old number*. Those interface assertions do depend on it. It is retained in the sealed input graph only to preserve the exact tested historical interfaces and their identities. The corrected standalone summary and this erratum supersede it as a reported mathematical count. No support table, characteristic-polynomial map, residue-domain enumeration or downstream exclusion bound depends on the erroneous aggregate; all eight freshly executed comparisons passed.

`SUPPLEMENTAL_V5_FINAL_RESULT.json` is the corrected publication summary. It explicitly separates `raw_reported_support_rows: 236182` from `independently_counted_support_rows: 237182`, and binds the original successful run, its verbatim log and the independent count review. The original supervisor's copied `conclusions.support_rows` field is also covered by this erratum. This additive correction neither relabels an unsuccessful run nor changes the declared main 13/65/16/5 replay coverage.

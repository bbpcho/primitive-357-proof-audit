# Fano parameter identification: review of report §§2 and 5

**The report's proposed shortcut is not a valid inference from the stated premises. The current manuscript does not rely on it.** No correction to the manuscript's exact-identification argument is called for by this point.

Matching ramification profiles over 0, 1, ∞ does not establish that two maps to P¹ differ by a Möbius transformation. The fact that an automorphism fixing those three points is the identity only removes a target-coordinate ambiguity **after** the maps have been shown to be related by such an automorphism. Equality of passports alone does not provide that relation. This objection does not require asserting that this particular passport has several realizations: any uniqueness/rigidity assertion would itself need proof.

Equivalently, two functions can have the same degree without generating the same rational subfield of the source curve's function field. If their rational subfields were already identified, then a change of generator would be Möbius, and the three distinct labelled fibre types could settle its normalization. That missing identification is exactly what the report says it did not check.

The report's computations at 23, 43, 67, 71 are useful independent consistency tests for the printed forms and their reductions. Without additional exact bounds or a specialization/lifting argument, the observed finite-characteristic fibre profiles do not establish the corresponding characteristic-zero identities or identify the function with the Fano parameter. This is not a claim that finite-prime methods cannot prove characteristic-zero statements: the project's separate Fano reconstruction uses CRT with a rigorous coefficient bound, which supplies the missing implication there.

## The actual manuscript and verifier

At current commit `b8d278de668861a30b72bdc947d7fdf84ab3d974`, manuscript §6.1.1, lines 853–868, explicitly uses the certificate's forward coordinates N₁,N₂,N₃ and two inverse maps. It states the identities

\[
 Q(N)=0,\qquad G_q(N)+qH_q(N)=0,\qquad G_t(N)+tH_t(N)=0,
\]

with both inverse denominators nonzero in the function field of R₊(q,t)=0. Recovering both q and t gives the function-field isomorphism with the smooth plane quartic. In particular the printed function −G_t/H_t is the same t appearing in the original resolvent, not merely a function with matching ramification. The smooth-projective extension handles common zeros in the chosen homogeneous presentation.

I inspected the actual private-baseline verifier, `p7_f42_canonical_verify.py`:

- Lines 5, 15–57 use exact `Fraction` pairs a+bs with s²=−7; these are characteristic-zero operations.
- Lines 147–159 construct the monic degree 15 R₊ from the Fano coefficient tables. The verifier's variable `A` is the normalized Fano coordinate q=M_F/225, as the imported Fano module explicitly documents.
- Lines 306–322 multiply and reduce in K[t][q]/(R₊). Lines 335–358 construct N_j from the exact differential vectors and check the zero remainder of Q(N).
- Lines 361–387 separately check both inverse identities. Line 383 requires each evaluated denominator to be nonzero, and line 385 requires the exact remainder to vanish. These are the relevant identification checks.
- Lines 410–446 check the five displayed branch-point substitutions. These supplement the inverse identities; they are not substituted for them.
- Lines 455–462, despite their “fresh-prime ranks” printed message, only inspect stored metadata. The adopted argument does **not** rely on that routine as a fresh rank computation: the exact inverse identities and independently verified smoothness provide the needed function-field conclusion. This limitation was already explicit in the prior logical audit.

The connection between the coefficient tables and the original Fano invariant is a separate computational premise. `p7_fano_resolvent_certificate.py`, lines 1–20 and 231–277, reconstructs the integer orbit coefficients and checks them against the normalized tables. The retained fresh run records 80 CRT primes, a 1330-bit modulus beyond the 1230-bit coefficient bound, and five additional validation primes. Those bounds, rather than matching a few fibre profiles, justify characteristic-zero recovery. The prior pure-sector audit also checks that the 15 Fano invariants do not collapse the quotient, and binds all printed quartic/parameter coefficients to the exact packet.

## Disposition

This is recorded as a correction to the **report's rationale**, not a newly discovered gap in the paper. Suggested wording:

> The finite-prime fibre calculations independently corroborate the printed parameter. They do not by themselves identify it with the Fano-resolvent parameter. That identification uses the paper's exact characteristic-zero forward and inverse function-field identities and their ancillary certificate; it remains an imported certificate result for a reader who has not checked that material.

No project calculation was rerun in this bounded source review. The original certificate/log and previously completed logical audit were inspected as evidence; their status strings alone were not treated as proofs.

## Source identities

Private source directory, relative to the sealed baseline:

`work/verified_release_2026_09_14/staging/PRIMITIVE_357_VERIFIED_RELEASE_2026-09-14_V1/evidence/v3/repository/beal_357_spark_handover_2026-08-20/project/`

| File | SHA-256 |
|---|---|
| Current `paper/manuscript.tex` | `70f66fe3605ecbde730e21fbee0308daaf0533fcd566d464274944066c3ef9cf` |
| `p7_f42_canonical_exact.json.gz` | `1252327a057029dd0ff0f6347f848be88794842afa742503a6c179f683087739` |
| `p7_f42_canonical_verify.py` | `c71f094867f544fa0e8c79ad6919cd0803328f9bd7e3c10c7c0efb8df3f1b028` |
| `p7_fano_resolvent_certificate.py` | `de3b8e28368510cdc18abc5dae9c3310b793b616ea8a15278f25c25ace6acaf7` |

Additional evidence: `work/mathematical_argument_audit_2026_09_15/reviews/pure_parameter.md`, lines 49–69; the sealed `verification/sectors/logs/independent_fano_resolvent_foundation.log`; and the canonical verifier's retained log alongside its source. This source review made no changes to mathematical inputs. Repository documentation changes are described in the accompanying response.

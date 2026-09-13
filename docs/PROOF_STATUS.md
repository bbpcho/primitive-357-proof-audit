# Proof status

Status date: 13 September 2026

## Executive status

The project has a strong manuscript and an unusually extensive computational
evidence base.  Packaging integrity, clean extraction, the four-sector routing,
the conservative Hecke ambient calculation, and several formerly missing
dependency closures have concrete replay evidence.

The repository nevertheless records the main theorem as **open at audit
level**.  The unresolved item is not a vague request for more computation: it
is a specific need to reconstruct and independently validate the
Mordell--Weil rank upper bound and its composition with the completed
saturation and logarithm calculations.

## Gate table

| Gate | State | Meaning |
|---|---|---|
| Manuscript builds cleanly | pass | The current TeX and V3 PDF are present; the sealed V3 log records a clean three-pass build. |
| Dependency-closed V3 integrity | pass | The 765-file V3 release has a strict manifest and clean-extraction replay. |
| Attribution and presentation repairs | pass in current draft | The current source includes the expanded provenance and Hecke discussion. |
| Hecke ambient coverage | pass at certificate boundary | The conservative filtered ambient argument avoids relying on an unsupported complete-newspace claim. |
| B124/D4 upstream provenance | pass at current evidence boundary | Tensor lift, 75D class, formal chart, and D4-log dependencies are supplied and replayed as a closed archive. |
| p=5 obstruction provenance | packaged | The target-42/contact/cocycle dependency closure and replay are supplied; independent audit is still required. |
| Mordell--Weil lower bound | evidence present | Four explicit classes and finite-field witnesses exist, but must be integrated into one clean rank audit. |
| Mordell--Weil upper bound and rank composition | **open audit gate** | Rebuild the Selmer/rank bound from primary inputs and prove that it combines with the known classes to give exactly the group statement consumed later. |
| Saturation calculations | pass at current evidence boundary | The independent Kummer/two-saturation and five-saturation checks are complete; their precise consequences still have to be used correctly in the rank composition. |
| Global logarithms and local gates | pass at current evidence boundary | Both split-23 branches, including the formerly cached D4 upstream chain, have been reconstructed and replayed. |
| Final theorem composition | blocked | It becomes eligible only after the rank chain and its downstream use are independently closed. |
| Public proof release | blocked | Publish only an audit snapshot until the mathematical gate above is closed. |

## What “packaged” does and does not mean

“Packaged” means that the dependency closure, programs, inputs, logs, and
hashes needed for a claimed replay have been gathered into one portable
object.  It is stronger than merely pointing to a file in the working tree.
It is weaker than an independent mathematical audit.  That distinction is
the principal design rule of this repository.

## Immediate workstream

The next work should be a single rank audit with a deliberately narrow output.
It should reuse, rather than redo, the completed saturation and logarithm
packages:

1. state the exact Mordell--Weil group, subgroup, and rank claim;
2. reconstruct the rank lower and upper bounds and their exact implication;
3. audit the p=5 closure at the point where it enters the upper bound;
4. verify that the later sieve, completed saturation, and completed local-log
   arguments consume precisely those
   outputs and no stronger unstated claim;
5. issue either a signed-off rank certificate or a precise no-go report.

Only after that should the main theorem wording and public release status be
changed.

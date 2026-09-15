# Replacement companion: replay guide and exact coverage

For `PRIMITIVE_357_REPLAY_COMPANION_2026-09-15_V2.zip`, release `replay-companion-2026-09-15.2`. The current paper and small arXiv source ZIP are separate release assets. This guide clarifies paths and the macOS compiler setup in the frozen companion instructions; it does not change any tested input.

All paths below are relative to the extracted companion root unless stated otherwise. Replace every uppercase path placeholder with an absolute path. `PYTHON` must name the actual Python executable. Keep the distribution, acquisition cache, logical inputs, private external inputs and replay output in disjoint directories. `LOGICAL`, `PRIVATE` and `OUTPUT` must not exist before use.

Use the recorded software versions: Python 3.12, SageMath 10.9, PARI/GP 2.15.4, SymPy 1.14, mpmath 1.3, python-flint 0.9, Poppler, a working C compiler, FLINT and GMP. The software installations are supplied separately.

## Authenticate and prepare inputs

```sh
PYTHON -B scripts/verify_companion.py
PYTHON -B scripts/acquire_external_inputs.py --lock inputs/EXTERNAL_INPUTS_LOCK.json --cache CACHE --record RECORDS/acquisition.json
PYTHON -B scripts/regenerate_hunter_sources.py --lock inputs/EXTERNAL_INPUTS_LOCK.json --recipes inputs/HUNTER_SOURCE_RECIPES.json --cache CACHE --record RECORDS/hunter.json
PYTHON -B scripts/regenerate_pvt_mod7.py --data CACHE/cc73ca915d3b25fe4def2b323b93bdc0fcdc46bbd560f16193af4dbdfae08ba5 --output CACHE/2833cdd1e290727028496b1339997ac3b401ab1d42dd51a9a970502a69837403 --record RECORDS/pvt.json
PYTHON -B scripts/verify_companion.py --cache CACHE --logical-root LOGICAL --private-root PRIVATE --report RECORDS/materialization.json
```

The first command checks distribution integrity, not arithmetic. Acquisition is an online preparation step for 62 pinned downloads; the generators produce 12 additional objects. Each object must match its exact size and SHA-256. `--offline` on the acquirer uses an existing checked cache; `--file ID=/absolute/path/to/file` accepts a separately obtained input without relaxing its identity check. Keep the cache and acquired/reconstructed third-party material private.

The PVT table is a verified reduction of the upstream numeric dataset, not a new production of that dataset. Hunter reconstruction restores exact source variants without executing them. The seven omitted historical native binaries were only hashed by the adopted suite; their original identities and limited provenance-check changes remain recorded. Seven earlier Magma executions and four negative controls remain separate records, not computations rerun here.

## Offline execution and macOS setup

The complete run must use a process-wide isolation boundary that blocks network access and earlier proof-workspace reads, permits only the new proof input roots and declared software dependencies, and confines writes to the fresh output and runtime scratch directories. The replay wrapper does not establish that operating-system boundary itself.

The preparation machine used the following macOS compiler environment. Adapt the SDK and software locations to the installed tools; `SDKROOT` is required when the compiler is invoked directly through this `PATH`:

```sh
export DEVELOPER_DIR=/Library/Developer/CommandLineTools
export SDKROOT=/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk
export PATH=/Library/Developer/CommandLineTools/usr/bin:/usr/bin:/bin:/sbin:/usr/sbin:/opt/homebrew/bin
export TMPDIR=/absolute/path/runtime-tmp
export CLANG_MODULE_CACHE_PATH="$TMPDIR/clang-cache"
export XDG_CACHE_HOME="$TMPDIR/xdg-cache"
export PYTHONDONTWRITEBYTECODE=1
export PYTHONOPTIMIZE=0
export OPENBLAS_NUM_THREADS=1
```

Create the runtime scratch directory before execution and include it in the isolation profile. The `/sbin` entry supplies `sha256sum` on this machine. Before the full run, check compilation/linking against the selected SDK, FLINT and GMP and check both permitted software reads and forbidden proof-workspace/network reads.

The actual driver and tested profile are recorded at:

- `records/completed-replay/isolation/launch_clean2.py`
- `records/completed-replay/isolation/CLEAN2_ISOLATED_DRIVER.json`
- `records/completed-replay/isolation/clean2_offline.sb`
- `records/completed-replay/isolation/CLEAN2_PROFILE_ALLOWLIST.json`
- `records/completed-replay/isolation/CLEAN2_ISOLATION_REVIEW.md`

Those files contain machine-specific absolute roots. They document the recorded run; adapt and recheck the paths/profile for another machine rather than executing the archived driver unchanged. A corresponding macOS invocation, after that adaptation, is:

```sh
/usr/bin/sandbox-exec -f PROFILE PYTHON -B scripts/replay_companion.py --logical-root LOGICAL --private-root PRIVATE --output-root OUTPUT --python PYTHON --sage-python SAGE_PYTHON --gp GP --pdftotext PDFTOTEXT --python-path PYTHON_SOFTWARE_DEPENDENCIES --flint-prefix FLINT_PREFIX
```

`PROFILE` is the adapted profile's absolute path. Other systems need an equivalent process-wide boundary. Both Python dependency and FLINT-prefix arguments are required. There is no partial-group or resume option. The earlier run's missing `stdio.h` diagnostics are retained under `records/completed-replay/earlier-incomplete-run/`; that attempt is not a successful full replay.

## Read the results

Require `PASS_FRESH_EXTERNALIZED_COMPLETE_REPLAY` in `OUTPUT/EXTERNALIZED_REPLAY_RESULT.json` and `PASS_INDEPENDENT_REPLAY_ENVELOPE` in `OUTPUT/INDEPENDENT_ENVELOPE.json`. The recorded coverage is 13 sector/interface records, 65 prior jobs and 16 rank-local checks, with the last group joined to five freshly generated inputs. The wrapper authenticates logical and private inputs before and after execution and independently checks the result joins. Read `OUTPUT/INTEGRATED_REPLAY.log` and `OUTPUT/suite/REPLAY_RESULT.json` with the stage logs; a historical PASS or a zero exit code with arithmetic diagnostics is insufficient.

The irreducible-sector record explicitly reports `DEEP_REPLAY=0` and invokes the V15 composition verifier **without `--full`**. The counts above identify the declared jobs; they do not mean that every optional producer referenced by a composition certificate was executed. The main run includes its specified component replays, small spectral contradiction, Fano reconstruction and independent Hecke foundations. It does not run irreducible `--deep`, V15 `--full`, or targeted Hunter V7 `--full`.

Five direct default-mode checks of the adapted archive readers were also run separately under the same unchanged CLEAN2 offline profile, against the same immutable logical and private inputs, with new scratch directories. They have their own actual commands, environment, input identities, exit codes and logs; they are **not additional records inside the main 13/65/16/5 contract**.

| Direct supplemental verifier | Observed time | Actual scope |
|---|---:|---|
| Hunter repair V2 | 6.761 s | Restored-source/endpoint checks and fresh predecessor PARI filtering of 52,582 saved rows to 279 matches and 19 field classes. |
| Hunter repair V3 | 7.910 s | Initial-state and regression checks, its own fresh V1 predecessor filter, corrected 52,561-row support and the field-count delta. |
| Finite-state V4 | 0.822 s | Root-count formulas, archived worker/support relationships, congruence/CRT arithmetic and restored-source invariants. |
| Tschirnhaus V5 | 16.170 s | Fresh generation and exact comparison of all eight local support tables: **237,182 rows**, with zero missing or extra rows. |
| Local-algebra V6 | 21.341 s | Fresh classification of 1,182 representatives, with identical results at precisions 35 and 45. |

**V5 count erratum:** its source, ledger and raw log print `total_imported_rows=236182`; the uncorrected supplemental supervisor also copied that number. The eight individually checked table counts actually sum to **237,182**. The raw records remain verbatim. This is an aggregate reporting error; all eight exact generated-set comparisons passed. Some downstream metadata assertions also retain the old label for historical interface compatibility; no enumeration or exclusion bound uses it. See the corrected final summary and completed-record review below for the independent count from the authenticated input tables.

The supplements do not rerun the historical Hunter native searches or V7's optional 173,175-state high-precision bound emitter. The original large search/UBSan counts remain authenticated historical evidence where that is what a verifier consumes. V5's finite support reconstruction and V6's classification are separate obligations; neither summary alone replaces the mathematical local-covering argument.

The sealed records are listed below. All paths in this list are relative to the extracted companion root.

- Main sector review: `records/completed-replay/sector-review/SECTOR_REVIEW.md`.
- V2/V3/V4/V6 scope and execution review: `records/completed-replay/supplemental/adapted-readers/SUPPLEMENTAL_REPLAY_REVIEW.md`, with its artifact index: `records/completed-replay/supplemental/adapted-readers/SUPPLEMENTAL_ARTIFACT_INDEX.json`.
- V4/V6 completed result: `records/completed-replay/supplemental/adapted-readers/supplemental_clean2/attempt2/SUPPLEMENTAL_RESULTS.json` and V2/V3 completed result: `records/completed-replay/supplemental/adapted-readers/supplemental_clean2/attempt3/SUPPLEMENTAL_RESULTS.json`.
- V5 scope, compiler correction and count erratum: `records/completed-replay/supplemental/v5/README.md`, corrected final result: `records/completed-replay/supplemental/v5/SUPPLEMENTAL_V5_FINAL_RESULT.json`, verbatim successful-run record: `records/completed-replay/supplemental/v5/attempt2/SUPPLEMENTAL_V5_RESULT.json`, and independent completed-record review: `records/completed-replay/supplemental/v5/COMPLETED_RECORD_REVIEW.json`.

Cited mathematical results and software algorithms remain premises. Successful replay is not proof-assistant formalization or independent human peer review.

## Repeat the five supplemental default checks

Run the main wrapper first so that its recorded portability and strict-GP adapters exist. Reuse those exact adapters, with the repository root pointing to `LOGICAL`, and keep the mathematical sources unchanged. These instructions invoke each default entry point directly; adding `--full` to a composition wrapper is a different workflow with additional runtime requirements.

Recheck the existing logical and private input bytes before and after the supplements. From the companion root, this block validates them without rematerializing or overwriting them:

```sh
PYTHON -B - LOGICAL PRIVATE <<'PYINPUT'
import sys
from pathlib import Path
sys.path.insert(0, str(Path('scripts').resolve()))
from companion_common import verify_distribution, check_expanded, check_private
_, logical, external, private = verify_distribution(Path.cwd())
check_expanded(Path(sys.argv[1]), logical)
check_private(Path(sys.argv[2]), external, private)
print('Logical and private input identities verified')
PYINPUT
```

Keep the macOS environment above. Replace the uppercase placeholders with absolute paths, including in variable assignments. The adapted profile must permit reading the already-generated adapter sources under `OUTPUT` and writing the new supplemental scratch directory. It must continue denying network access and earlier proof-workspace reads.

```sh
set -e
REPOSITORY=LOGICAL/evidence/v3/repository
PORTABLE=OUTPUT/suite/sectors/v3/scripts/portable_python.py
export BEAL357_REPOSITORY_ROOT="$REPOSITORY"
export BEAL357_SAGE_PYTHON=SAGE_PYTHON
export BEAL357_MINIMUM_CHILD_TIMEOUT=1800
export BEAL357_PDFTOTEXT=PDFTOTEXT
export PRIMITIVE357_GP_ADAPTER=OUTPUT/suite/sectors/bin/gp
export RANK_AUDIT_REAL_GP=GP
export PRIMITIVE357_EXTERNAL_INPUTS=PRIVATE
export PYTHONPATH=PYTHON_SOFTWARE_DEPENDENCIES
export PYTHONINTMAXSTRDIGITS=0
SUPPLEMENT="$TMPDIR/supplemental-default-checks"
mkdir "$SUPPLEMENT"

run_leaf() (
    leaf_name=$1
    shift
    leaf_dir="$SUPPLEMENT/$leaf_name"
    mkdir "$leaf_dir"
    export TMPDIR="$leaf_dir"
    export DOT_SAGE="$leaf_dir/sage-cache"
    export XDG_CACHE_HOME="$leaf_dir/xdg-cache"
    export CLANG_MODULE_CACHE_PATH="$leaf_dir/clang-cache"
    if [ "$leaf_name" = v5 ]; then
        mkdir "$leaf_dir/bin"
        ln -s /Library/Developer/CommandLineTools/usr/bin/clang++ "$leaf_dir/bin/g++"
        export PATH="$leaf_dir/bin:$PATH"
    fi
    cd "$leaf_dir"
    set +e
    /usr/bin/sandbox-exec -f PROFILE "$@" > replay.log 2>&1
    leaf_rc=$?
    printf '%s\n' "$leaf_rc" > exit-code.txt
    exit "$leaf_rc"
)

run_leaf v2 PYTHON -I -B "$PORTABLE" -B "$REPOSITORY/results/2026-09-09_putz_hunter_closed_interval_completeness_repair_v2/scripts/verify_putz_hunter_closed_interval_completeness_repair_v2.py"
run_leaf v3 PYTHON -I -B "$PORTABLE" -B "$REPOSITORY/results/2026-09-09_putz_hunter_initial_configuration_completeness_repair_v3/scripts/verify_putz_hunter_initial_configuration_completeness_repair_v3.py"
run_leaf v4 PYTHON -I -B "$REPOSITORY/results/2026-09-09_putz_hunter_finite_state_projector_invariant_v4/scripts/verify_putz_hunter_finite_state_projector_invariant_v4.py"
run_leaf v5 PYTHON -B "$REPOSITORY/results/2026-09-09_putz_hunter_local_tschirnhaus_support_v5/scripts/verify_putz_hunter_local_tschirnhaus_support_v5.py"
run_leaf v6 SAGE_PYTHON -I -B "$REPOSITORY/results/2026-09-09_putz_hunter_local_algebra_covering_v6/scripts/verify_putz_hunter_local_algebra_covering_v6.py"
```

The scratch directory must be new; the `mkdir` checks intentionally fail on reuse. Each job retains its full output and actual exit code in its own directory. Require zero exit codes and the source's exact completion result: V2's JSON `status` is `PASS_HUNTER_CLOSED_INTERVAL_AND_DIRECTED_BOUND_COMPLETENESS_REPAIR_V2`; the remaining exact lines are `PASS_PUTZ_HUNTER_STATIC_STATE_SPACE_COMPLETENESS_REPAIR_V3`, `PASS_PUTZ_HUNTER_FINITE_STATE_PROJECTOR_INVARIANT_V4`, `PASS_PUTZ_HUNTER_LOCAL_TSCHIRNHAUS_SUPPORT_V5`, and `PASS_PUTZ_HUNTER_LOCAL_ALGEBRA_COVERING_V6`. Check the numerical outputs and V5 erratum as described above, and repeat the input-identity check afterward. Retain the actual commands, environment/profile, input identities and timestamps if recording a new run.

The V5 `g++` alias selects the native Command Line Tools `clang++` directly. On this machine the dispatch wrapper emitted xcrun cache errors despite a successful compiler exit, which correctly failed the source's empty-diagnostics check. The fresh alias preserved the source's `-std=c++17 -O3 -DNDEBUG` flags and required no warning suppression or wider sandbox. The unsuccessful attempt and diagnostic probes are retained with the V5 records. On another platform, select a working native C++ compiler and recheck the boundary; do not disable the verifier's compiler-output assertions.

## Clarified paths in the frozen acquisition guide

The root `EXTERNAL_INPUTS_GUIDE.md` predates final placement of four referenced records. Its bare names refer to these actual paths:

| Name in frozen guide | Actual path from companion root |
|---|---|
| `THIRD_PARTY_ATTRIBUTION.md` | `THIRD_PARTY_NOTICES.md` |
| `RETAINED_LICENSED_MATERIAL.json` | `inputs/RETAINED_LICENSED_MATERIAL.json` |
| `FRESH_ACQUISITION_SUMMARY.json` | `records/release-preparation/FRESH_ACQUISITION_SUMMARY.json` |
| `NEGATIVE_CONTROLS.json` | `records/release-preparation/NEGATIVE_CONTROLS.json` |

The root README's macOS compiler note should be read with the explicit `SDKROOT` setup above. Both frozen files are preserved byte for byte to maintain the tested distribution identity; this appended guide supplies the clarification.

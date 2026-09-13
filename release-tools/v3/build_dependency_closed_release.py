#!/usr/bin/env python3
"""Build the V2 dependency-closed research release and ancillary archive."""

from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import os
from pathlib import Path
import platform
import re
import shutil
import subprocess
import sys
import tarfile
import tempfile
import time


PACKAGE = Path(__file__).resolve().parents[1]
WORKSPACE = PACKAGE.parents[1]
BASE = WORKSPACE / "results/2026-09-11_primitive_357_paper_release_v1"
OUTPUT = PACKAGE / "dependency_closed_release_v2"
RELEASE_NAME = "2026-09-13_primitive_357_dependency_closed_release_v2"
RELEASE = OUTPUT / RELEASE_NAME
REPOSITORY = RELEASE / "repository"
MANIFEST = RELEASE / "manifests/PRIMITIVE_357_DEPENDENCY_CLOSED_RELEASE_V2_SHA256SUMS.txt"
ARCHIVE = PACKAGE / "anc/PRIMITIVE_357_REPRODUCIBILITY_V2.tar.gz"
SAGE_ENV = Path("/tmp/beal357-p23-sage-runtime-v1/env")

EXTERNAL_SOURCES = {
    "composition_review_v2": (
        Path("/home/pcho/Downloads/AUDIT_COMPOSITION_V2.md"),
        "references/AUDIT_COMPOSITION_V2.md",
        "74b865c967efc3cd9a06ef48109f92c3d106f56a7e95b11fd20a5a37b54a7394",
    ),
    "putz_thesis": (
        Path("/home/pcho/Downloads/Thesis_CasperPutz.pdf"),
        "references/Thesis_CasperPutz.pdf",
        "5652812adac99a7d5c8b429a83072cbf5b1ccae35552645a837093dd8ade2c7c",
    ),
    "pacetti_villagra_torcomian_preprint": (
        Path("/tmp/2512.17845.pdf"),
        "references/Pacetti_Villagra_Torcomian_2512.17845v1.pdf",
        "d5983c0949129942c3510d9c3a8de1fbf8998e4b0e5b5d822ddf94a795048004",
    ),
}

FULL_PACKAGES = {
    "section7_quartic_router": "results/2026-09-09_quartic_factor_router_3_4_v1",
    "section7_terminal_engine": "results/2026-09-09_section7_terminal_engine_reconstruction_v1",
    "section7_mordell_weil_basis": "results/2026-09-10_section7_mordell_weil_basis_lemma_7_3_v1",
    "section7_mordell_weil_sieve": "results/2026-09-10_section7_mw_sieve_lemma_7_4_v1",
    "section7_model_intrinsic_formal_group": "results/2026-09-10_section7_formal_group_lemma_7_5_v2_model_intrinsic",
    "rational_parameter_residue_sieve": "results/2026-09-08_p23_rational_t_diagonal_residue_inventory_v1",
    "rational_parameter_exceptional_diagonal": "results/2026-09-08_p23_exceptional_t_diagonal_test_v1",
    "rational_parameter_rank4_checkpoint": "results/2026-09-06_p23_ros_rank4_checkpoint_v1",
    "rational_parameter_strict_c25_independent_audit": "results/2026-08-30_p7_p109_corrected_c25_strict_independent_audit_v1",
    "rational_parameter_p109_c25_discriminator": "results/2026-08-30_p109_corrected_c25_discriminator_v1",
    "odd_exceptional_cm_interference": "results/2026-09-08_odd_exceptional_splitting_cm_interference_v2",
    "odd_exceptional_cm_crosscheck": "results/2026-09-08_odd_exceptional_splitting_cm_adversarial_crosscheck_v2",
}

SELECTED_FILES = {
    "rational_parameter_source_bridge": [
        "beal_357_spark_handover_2026-08-20/project/beal_357_progress.tex",
    ],
    "hilbert_hecke_upstream_data_parser": [
        "beal_357_spark_handover_2026-08-20/project/verify_p7_data_mod7.py",
    ],
    "rational_parameter_s4_log_inputs": [
        "results/2026-08-31_p23_alternative_km_base_chart_screen_v1/scripts/compute_p23_s4_full_log_matrix_v1.sage",
        "results/2026-08-31_p23_alternative_km_base_chart_screen_v1/certificates/p23_s4_full_log_matrix_v1.json",
        "results/2026-08-31_p23_alternative_km_base_chart_screen_v1/evidence/p23_s4_full_log_matrix_v1.sobj",
    ],
    "rational_parameter_s19_log_and_lift_inputs": [
        "results/2026-08-31_p23_s19_alternative_km_base_chart_screen_v1/scripts/compute_p23_s19_full_log_matrix_v1.sage",
        "results/2026-08-31_p23_s19_alternative_km_base_chart_screen_v1/certificates/p23_s19_full_log_matrix_v1.json",
        "results/2026-08-31_p23_s19_alternative_km_base_chart_screen_v1/evidence/p23_s19_full_log_matrix_v1.sobj",
        "results/2026-08-31_p23_s19_alternative_km_base_chart_screen_v1/scripts/certify_p23_ros_log_rank_and_siksek_v1.sage",
        "results/2026-08-31_p23_s19_alternative_km_base_chart_screen_v1/certificates/p23_ros_log_rank_and_siksek_v1.json",
        "results/2026-08-31_p23_s19_alternative_km_base_chart_screen_v1/scripts/analyze_p23_P1_second_order_gate_v1.sage",
        "results/2026-08-31_p23_s19_alternative_km_base_chart_screen_v1/certificates/p23_P1_second_order_gate_v1.json",
        "results/2026-08-31_p23_s19_alternative_km_base_chart_screen_v1/scripts/lift_p23_P1_exceptional_root_and_coefficients_v1.sage",
        "results/2026-08-31_p23_s19_alternative_km_base_chart_screen_v1/certificates/p23_P1_exceptional_root_coefficients_v1.json",
    ],
}

MANIFEST_CLOSURES = {
    "original_project_manifest_closure": (
        "beal_357_spark_handover_2026-08-20/project/SHA256SUMS_357.txt"
    ),
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def write_text(path: Path, value: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(value, encoding="utf-8", newline="\n")


def copy_file(relative: str) -> None:
    source = WORKSPACE / relative
    target = REPOSITORY / relative
    if not source.is_file() or source.is_symlink():
        raise AssertionError(("missing/unsafe dependency", relative))
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        if sha256(target) != sha256(source):
            raise AssertionError(("dependency conflicts with base release", relative))
        return
    shutil.copy2(source, target)


def copy_package(relative: str) -> None:
    source_root = WORKSPACE / relative
    if not source_root.is_dir() or source_root.is_symlink():
        raise AssertionError(("missing/unsafe package", relative))
    for source in sorted(source_root.rglob("*")):
        if not source.is_file() or source.is_symlink():
            continue
        if "__pycache__" in source.parts or source.suffix in {".pyc", ".pyo"}:
            continue
        copy_file(source.relative_to(WORKSPACE).as_posix())


def copy_external_sources() -> None:
    for label, (source, relative, expected) in EXTERNAL_SOURCES.items():
        if not source.is_file() or source.is_symlink() or sha256(source) != expected:
            raise AssertionError(("missing/mismatched external source", label, source))
        target = REPOSITORY / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)


def manifest_closure_members(relative: str) -> list[str]:
    manifest = WORKSPACE / relative
    if not manifest.is_file() or manifest.is_symlink():
        raise AssertionError(("missing/unsafe closure manifest", relative))
    members = [relative]
    seen: set[str] = set()
    for line in manifest.read_text(encoding="utf-8").splitlines():
        match = re.fullmatch(r"([0-9a-f]{64})  ([^\x00\r\n]+)", line)
        if not match:
            raise AssertionError(("malformed closure-manifest row", relative, line))
        digest, member = match.groups()
        candidate = Path(member)
        if candidate.is_absolute() or ".." in candidate.parts or member in seen:
            raise AssertionError(("unsafe/duplicate closure member", relative, member))
        seen.add(member)
        source = (manifest.parent / candidate).resolve()
        source.relative_to(WORKSPACE.resolve())
        if not source.is_file() or source.is_symlink() or sha256(source) != digest:
            raise AssertionError(("closure member mismatch", relative, member))
        members.append(source.relative_to(WORKSPACE).as_posix())
    return sorted(set(members))


def command_output(command: list[str], timeout: int = 60) -> str | None:
    try:
        completed = subprocess.run(
            command,
            check=False,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=timeout,
            env={
                "PATH": "/usr/bin:/bin",
                "HOME": "/tmp",
                "DOT_SAGE": "/tmp/primitive357-version-dot-sage",
                "LANG": "C.UTF-8",
                "LC_ALL": "C.UTF-8",
            },
        )
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return None
    if completed.returncode:
        return None
    return completed.stdout.strip()


def software_versions() -> dict:
    sage_python = SAGE_ENV / "bin/python"
    return {
        "schema": "primitive_357_dependency_closed_software_versions_v2",
        "build_host": {
            "platform": platform.platform(),
            "machine": platform.machine(),
            "python": sys.version.splitlines()[0],
        },
        "available_at_build": {
            "pari_gp": command_output(["/usr/bin/gp", "--version-short"]),
            "pdflatex": command_output(["/usr/bin/pdflatex", "--version"]),
            "sage": command_output(
                [str(sage_python), "-c", "import sage.env; print(sage.env.SAGE_VERSION)"]
            ) if sage_python.is_file() else None,
            "sympy_mpmath": command_output([
                str(WORKSPACE / "results/2026-08-20_descent_support/.venv/bin/python"),
                "-c",
                "import sympy,mpmath; print(sympy.__version__,mpmath.__version__)",
            ]),
            "c_compiler": command_output(["/usr/bin/cc", "--version"]),
            "magma": command_output(["magma", "-v"]),
        },
        "specialist_log_identity": {
            "magma": "V2.29-10, as named by the authenticated Magma input/output packages",
            "note": "Magma is proprietary and was not installed during this release build.",
        },
        "upstream_trace_data_generation": {
            "source": "third_party/GFE-5p3/Outputs/DataTimes.txt",
            "pari_gp": "2.17.2",
            "reported_cpu_time": "15h 44min 18.655s",
            "reported_wall_time": "1h 4min 49.297s",
            "replay_note": (
                "The release rechecks all 6253 generated polynomials against "
                "the bundled output; it does not repeat this one-hour upstream generation."
            ),
        },
    }


def build_dependency_index(base_paths: set[str]) -> dict:
    groups = []
    for label, relative in FULL_PACKAGES.items():
        prefix = relative + "/"
        members = sorted(
            path.relative_to(REPOSITORY).as_posix()
            for path in (REPOSITORY / relative).rglob("*")
            if path.is_file()
        )
        groups.append({"id": label, "kind": "complete_package", "root": relative, "files": members})
    for label, members in SELECTED_FILES.items():
        groups.append({"id": label, "kind": "selected_authenticated_inputs", "files": members})
    for label, relative in MANIFEST_CLOSURES.items():
        groups.append({
            "id": label,
            "kind": "strict_manifest_closure",
            "manifest": relative,
            "files": manifest_closure_members(relative),
        })
    groups.append({
        "id": "putz_pvt_primary_and_review_sources",
        "kind": "exact_external_sources_relocated_in_memory",
        "files": [relative for _, relative, _ in EXTERNAL_SOURCES.values()],
    })
    actual = sorted(
        path.relative_to(REPOSITORY).as_posix()
        for path in REPOSITORY.rglob("*")
        if path.is_file()
    )
    added = [
        {"path": relative, "sha256": sha256(REPOSITORY / relative)}
        for relative in actual
        if relative not in base_paths
    ]
    return {
        "schema": "primitive_357_dependency_closure_index_v2",
        "base_release": "2026-09-11_primitive_357_paper_release_v1",
        "base_repository_file_count": len(base_paths),
        "repair_scope": (
            "Adds every file required by the ordinary sector-level replay suite, "
            "including the complete Section 7 packages and the rational-parameter "
            "sieve, rank, local-root, and lift interfaces."
        ),
        "groups": groups,
        "added_files": added,
        "added_file_count": len(added),
        "repository_file_count": len(actual),
        "third_party_source_snapshot": {
            "root": "third_party/GFE-5p3",
            "upstream_commit": "e88f914c577ab6cf9a45e5cdd82c1993477fb423",
            "origin": "third_party/GFE-5p3/UPSTREAM_ORIGIN.json",
            "manifest": "third_party/GFE-5p3/UPSTREAM_SHA256SUMS.txt",
            "file_count_including_manifest": sum(
                1 for path in (RELEASE / "third_party/GFE-5p3").rglob("*")
                if path.is_file()
            ),
        },
        "clean_extraction_policy": {
            "original_workspace": "/home/pcho/Documents/Codex/beal_357",
            "access": "filesystem path absent inside a bubblewrap mount namespace",
            "evidence_bytes_modified": False,
            "path_relocation": "historical machine-local literals replaced only in memory",
        },
    }


def base_repository_paths() -> set[str]:
    return {
        path.relative_to(BASE / "repository").as_posix()
        for path in (BASE / "repository").rglob("*")
        if path.is_file()
    }


def write_docs() -> None:
    readme = """# Primitive (3,5,7) dependency-closed research release V2

This release repairs the incomplete transitive dependency collection in V1.
It contains the paper, the exact evidence tree, every ordinary sector-replay
dependency, an explicit dependency index, software-version metadata, complete
clean-extraction replay output, and a portable verifier.

Run the dependency and composition checks:

    python3 -B scripts/verify_dependency_closed_release.py

Install the pinned Python dependencies before sector replay:

    python3 -m pip install -r requirements.txt

Rerun every ordinary sector-level verifier:

    python3 -B scripts/verify_dependency_closed_release.py --run-sector-replays

The portable launcher leaves every authenticated evidence file byte-for-byte
unchanged. It relocates historical absolute path literals only in memory.
The sealed release test is run inside a filesystem namespace in which the
original workspace path does not exist. Ordinary sector replay requires
Python 3.12, SymPy 1.14, mpmath 1.3, PARI/GP 2.15.4, and SageMath 10.9.
Magma is needed only for separately identified specialist recomputations.

The Hecke terminal step now verifies the complete upstream local-trace data
and every preceding filter. One archived filter at 131 omitted an allowed
trace; the replay makes that filter vacuous and rebuilds all four filtered
ambient modules. This conservative computation makes old/new subtraction
diagnostic rather than load-bearing; see HECKE_AMBIENT_COVERAGE.md.
"""
    changelog = """# Changelog: V1 to dependency-closed V2

1. Added all five omitted Section 7 dependencies: the quartic router,
   terminal engine, Mordell--Weil basis, Mordell--Weil sieve, and
   model-intrinsic formal-group package.
2. Added the rational-parameter residue-sieve certificate and programs, the
   rank-four/P1 checkpoint, exceptional diagonal test, both split-23 log
   interfaces, and the exceptional-root lift inputs.
3. Added an explicit file-by-file dependency index instead of relying on a
   regular expression for literal manifest names. The V1 collector missed
   paths assembled from Python constants.
4. Added a portable launcher. Several authenticated historical replay scripts
   contained the original machine path. The launcher checks their original
   bytes, substitutes the extracted repository root only in memory, and
   can delegate Sage sources to the configured SageMath interpreter.
5. A failed nested Section 7 replay showed that a child process discarded the
   relocation variable. The launcher now discovers the bundled repository
   beside itself, so nested verifiers remain relocatable without editing any
   authenticated evidence bytes.
6. A second failed nested replay showed that a Sage source was being sent to
   ordinary CPython. The launcher now detects Sage imports and delegates the
   same in-memory-relocated source to the pinned Sage 10.9 interpreter.
7. A third failed nested replay showed that a historical child verifier
   intentionally discarded `PYTHONPATH`, so its fresh portable-Python child
   could not import SymPy. The launcher now rediscovers the read-only
   `/dependencies` mount and propagates it to later nested children without
   changing any authenticated evidence source.
8. The first dependency-mount repair still replaced the discovered path when
   it installed the historical script directory at `sys.path[0]`. The next
   clean replay exposed this immediately. The launcher now inserts the script
   directory while preserving the dependency entry; the precise nested-child
   case is tested before the full replay is repeated.
9. The next clean replay reached the irreducible-sector projector and exposed
   an omitted original project manifest. The release now includes the strict
   157-row `SHA256SUMS_357.txt` closure plus the manifest itself, rather than
   selecting only the project files named in later certificates.
10. The focused projector replay then exposed a multiprocessing portability
    defect: functions compiled in a detached dictionary could not be pickled
    as `__main__` workers. The launcher now compiles into the registered
    `__main__` module dictionary, preserving historical fork-worker lookup.
11. The next focused irreducible replay exposed one more transitive omission:
    the rational-parameter stress audit binds the strict independent C25
    package. That complete six-file package is now included and indexed.
12. The following focused replay exposed its producer-side dependency, the
    seven-file p=109 corrected C25 discriminator package. It too is now
    included in full and indexed explicitly.
13. The seven-field compression then reached two odd-packet/CM interface
    manifests absent from V1. Both the five-file interface package and its
    four-file Sage crosscheck are now included in full and indexed.
14. The first full run with all mathematical sectors passing exposed one
    release-verifier dependency not present in the 157-row project manifest:
    `verify_p7_data_mod7.py`. It is now an explicit indexed input to the Hecke
    filter audit.
15. A focused Hecke rebuild then showed that this Debian host's `/usr/bin/cc`
    is a symlink through `/etc/alternatives`, which the empty-root namespace
    had not mounted. The isolated harness now read-only mounts that system
    alternatives directory; no evidence or mathematical source is changed.
16. Added the complete upstream `GFE-5p3` snapshot at commit
   `e88f914c577ab6cf9a45e5cdd82c1993477fb423`, including the original
   6,253-polynomial `Data.txt`, generation code, output, version log, origin
   record, and strict manifest.
17. Audited every preceding Hecke trace filter. Seventeen reproduce exactly;
   the archived filter at 131 omitted the allowed level-lowering trace 1.
   The new replay makes that condition vacuous (`T^49-T`) and rebuilds the
   four conservatively filtered ambient modules. All 36 T_2-compatible packet
   occurrences have T_29 factors already present in the terminal six-factor
   resultant calculation. Old/new subtraction is no longer load-bearing.
18. Added software-version metadata and complete per-sector and combined logs
   from an extracted archive mounted in an isolated filesystem where the
   original workspace path is absent.
19. The decisive clean extraction exposed a machine-speed assumption in the
    authenticated Section 7 orchestrator: its PARI router child exceeded the
    historical 300-second limit. The portable launcher now permits that one
    sector to raise child limits to 1,800 seconds (never lower them), while
    executing the same authenticated command and leaving all historical bytes
    unchanged. The effective limit is printed in the complete replay log.
20. The final Putz--PVT interface replay exposed three unbundled exact source
    objects: the review memo, the complete Putz thesis, and the cited PVT
    preprint. All three are now checksum-pinned in `repository/references/`;
    the portable launcher redirects the historical absolute paths to those
    extracted copies in memory. This completes the sector's source interface
    with the original Downloads directory and `/tmp` inaccessible.
21. The Putz package wrapper starts its primary verifier with a literal
    `/usr/bin/python3` command. The portable launcher now redirects any such
    repository-local Python child back through the same in-memory relocation
    layer. The command target and authenticated source bytes are unchanged;
    this only prevents a nested child from escaping the clean path mapping.

No historical mathematical certificate, input, program, or authenticated log
was edited. The conservative 131 repair is generated in a temporary directory
and its exact two-token source transformation is checked before compilation.
The paper and release add the corrected Hecke-coverage argument and verifiers;
all historical evidence remains byte-identical.
"""
    write_text(RELEASE / "README.md", readme)
    write_text(RELEASE / "CHANGELOG.md", changelog)
    write_text(RELEASE / "requirements.txt", "sympy==1.14.0\nmpmath==1.3.0\n")


def build_sector_index() -> dict:
    specifications = [
        ("signed-global-algebra", "results/2026-09-09_signed_global_algebra_superselection_audit_v8/scripts/verify_signed_global_algebra_superselection_audit_v8.py", "repository", ["base evidence tree"]),
        ("rational-factor-sector", "results/2026-09-10_rational_factor_proposition_6_1_composition_v2/scripts/verify_rational_factor_proposition_6_1_checkpoint_v2.py", "repository", ["base evidence tree"]),
        ("quadratic-factor-router", "results/2026-09-09_quadratic_factor_router_2_5_v1/scripts/verify_quadratic_factor_router_2_5.py", "repository", ["base evidence tree"]),
        ("quadratic-factor-terminal", "results/2026-09-09_quadratic_factor_2_5_reconstruction_v1/scripts/verify_quadratic_factor_2_5_reconstruction.py", "repository", ["base evidence tree"]),
        ("cubic-quartic-section7-sector", "results/2026-09-10_section7_proposition_7_1_closure_v2_model_intrinsic/scripts/verify_section7_proposition_7_1_closure_v2.py", "repository", [key for key in FULL_PACKAGES if key.startswith("section7_")]),
        ("rational-parameter-sieve-and-lifts", "results/2026-09-08_mixed_rational_t_signature_357_closure_v1/scripts/verify_mixed_rational_t_signature_357_closure_v1.py", "repository", [key for key in FULL_PACKAGES if key.startswith("rational_parameter_")] + list(SELECTED_FILES)),
        ("irreducible-septic-sector", "results/2026-09-10_irreducible_degree7_sector_closure_v1/scripts/verify_irreducible_degree7_sector_closure_v1.py", "repository", ["base evidence tree", "rational-parameter closure"]),
        ("hilbert-hecke-filter-coverage", "scripts/verify_hilbert_hecke_filter_coverage.py", "release", ["complete upstream GFE-5p3 snapshot", "6253 trace polynomials", "archived FLINT filter source"]),
        ("hilbert-hecke-ambient-coverage", "scripts/verify_hilbert_hecke_ambient_coverage.py", "release", ["filter-coverage audit", "four freshly rebuilt conservative filtered ambient modules", "prime-2 local trace certificate"]),
        ("putz-pvt-interface", "results/2026-09-10_pvt_putz_interface_audit_v2/scripts/verify_pvt_putz_interface_v2_package.py", "repository", ["base evidence tree"]),
    ]
    rows = []
    for label, relative, base, dependencies in specifications:
        root = RELEASE if base == "release" else REPOSITORY
        rows.append({
            "id": label,
            "base": base,
            "source": relative,
            "sha256": sha256(root / relative),
            "dependencies": dependencies,
        })
    return {
        "schema": "primitive_357_sector_replay_index_v2",
        "original_workspace_must_be_absent": True,
        "ordinary_runtime": {
            "python": "3.12",
            "sympy": "1.14.0",
            "mpmath": "1.3.0",
            "pari_gp": "2.15.4",
            "sage": "10.9",
        },
        "replays": rows,
    }


def write_root_manifest() -> None:
    files = sorted(
        path for path in RELEASE.rglob("*")
        if path.is_file() and path != MANIFEST
    )
    rows = [f"{sha256(path)}  {path.relative_to(RELEASE).as_posix()}" for path in files]
    write_text(MANIFEST, "\n".join(rows) + "\n")


def deterministic_tar(source: Path, target: Path) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("wb") as raw:
        with gzip.GzipFile(filename="", mode="wb", fileobj=raw, mtime=0) as zipped:
            with tarfile.open(fileobj=zipped, mode="w", format=tarfile.PAX_FORMAT) as archive:
                for path in sorted(source.rglob("*"), key=lambda item: item.as_posix()):
                    relative = Path(source.name) / path.relative_to(source)
                    info = archive.gettarinfo(str(path), arcname=relative.as_posix())
                    info.uid = 0
                    info.gid = 0
                    info.uname = ""
                    info.gname = ""
                    info.mtime = 0
                    if path.is_file():
                        with path.open("rb") as handle:
                            archive.addfile(info, handle)
                    else:
                        archive.addfile(info)


def clean_extraction_replay() -> str:
    with tempfile.TemporaryDirectory(prefix="primitive357-dependency-closed-") as temporary:
        temporary_root = Path(temporary)
        candidate_archive = temporary_root / "candidate.tar.gz"
        deterministic_tar(RELEASE, candidate_archive)
        with tarfile.open(candidate_archive, "r:gz") as archive:
            archive.extractall(temporary_root, filter="data")
        clean = temporary_root / RELEASE_NAME
        dependency_site = temporary_root / "site-packages"
        dependency_site.mkdir()
        source_site = (
            WORKSPACE
            / "results/2026-08-20_descent_support/.venv/lib/python3.12/site-packages"
        )
        copied_dependencies: list[str] = []
        for pattern in ("sympy", "sympy-*.dist-info", "mpmath", "mpmath-*.dist-info"):
            for source in source_site.glob(pattern):
                target = dependency_site / source.name
                if source.is_dir():
                    shutil.copytree(source, target)
                    copied_dependencies.append(source.name)
        if not {"sympy", "mpmath"}.issubset(copied_dependencies):
            raise AssertionError(("missing clean-test Python dependencies", copied_dependencies))
        if not SAGE_ENV.is_dir():
            raise AssertionError("Sage 10.9 replay environment is unavailable")
        started = time.monotonic()
        command = [
            "/usr/bin/bwrap", "--die-with-parent", "--unshare-all", "--new-session",
            "--clearenv", "--tmpfs", "/", "--proc", "/proc", "--dev", "/dev",
            "--ro-bind", "/usr", "/usr", "--symlink", "usr/bin", "/bin",
            "--symlink", "usr/lib", "/lib", "--symlink", "usr/lib64", "/lib64",
            "--ro-bind", "/etc/alternatives", "/etc/alternatives",
            "--ro-bind", str(clean), "/release",
            "--ro-bind", str(dependency_site), "/dependencies",
            "--dir", "/tmp/beal357-p23-sage-runtime-v1",
            "--ro-bind", str(SAGE_ENV), "/tmp/beal357-p23-sage-runtime-v1/env",
            "--setenv", "PATH", "/usr/bin:/bin",
            "--setenv", "HOME", "/nonexistent",
            "--setenv", "LANG", "C.UTF-8", "--setenv", "LC_ALL", "C.UTF-8",
            "--setenv", "PYTHONDONTWRITEBYTECODE", "1",
            "--setenv", "PYTHONINTMAXSTRDIGITS", "0",
            "--setenv", "PYTHONPATH", "/dependencies",
            "--setenv", "BEAL357_SAGE_PYTHON", "/tmp/beal357-p23-sage-runtime-v1/env/bin/python",
            "--setenv", "BEAL357_FLINT_PREFIX", "/tmp/beal357-p23-sage-runtime-v1/env",
            "--chdir", "/release",
            "/usr/bin/python3", "-B", "/release/scripts/verify_dependency_closed_release.py",
            "--run-sector-replays", "--require-original-workspace-absent",
        ]
        completed = subprocess.run(
            command,
            cwd=temporary_root,
            check=False,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=24000,
            env={
                "PATH": "/usr/bin:/bin",
                "HOME": "/tmp",
                "LANG": "C.UTF-8",
                "LC_ALL": "C.UTF-8",
                "PYTHONDONTWRITEBYTECODE": "1",
                "PYTHONINTMAXSTRDIGITS": "0",
            },
        )
        elapsed = time.monotonic() - started
        output = (
            "CLEAN_EXTRACTION_SOURCE=DETERMINISTIC_PRESEAL_TAR_ARCHIVE\n"
            "ISOLATION=BUBBLEWRAP_UNSHARE_ALL_EMPTY_ROOT\n"
            "RELEASE_MOUNT=/release_READ_ONLY\n"
            "ORIGINAL_WORKSPACE_ACCESS=IMPOSSIBLE_PATH_ABSENT\n"
            "PYTHON_DEPENDENCIES_READ_ONLY=" + ",".join(copied_dependencies) + "\n"
            f"EXIT={completed.returncode}\nWALL_SECONDS={elapsed:.6f}\n"
            + completed.stdout
        )
        if completed.returncode:
            raise RuntimeError(output[-30000:])
        return output


def write_replay_logs(output: str) -> None:
    write_text(RELEASE / "logs/CLEAN_EXTRACTION_SECTOR_REPLAY_V2.log", output)
    matches = list(re.finditer(
        r"^===== BEGIN ([a-z0-9-]+) =====\n(.*?)^===== END \1 =====$",
        output,
        re.MULTILINE | re.DOTALL,
    ))
    if len(matches) != 10:
        raise AssertionError(("sector log split count", len(matches)))
    for number, match in enumerate(matches, 1):
        label, body = match.groups()
        write_text(
            RELEASE / f"logs/sectors/{number:02d}_{label}.log",
            f"SECTOR={label}\n{body}",
        )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-sector-replays", action="store_true")
    args = parser.parse_args()
    if OUTPUT.exists():
        shutil.rmtree(OUTPUT)
    RELEASE.mkdir(parents=True)
    shutil.copytree(BASE / "repository", REPOSITORY)
    base_paths = base_repository_paths()
    for relative in FULL_PACKAGES.values():
        copy_package(relative)
    for members in SELECTED_FILES.values():
        for relative in members:
            copy_file(relative)
    for relative in MANIFEST_CLOSURES.values():
        for member in manifest_closure_members(relative):
            copy_file(member)
    copy_external_sources()
    shutil.copytree(PACKAGE / "third_party", RELEASE / "third_party")

    (RELEASE / "paper").mkdir()
    shutil.copy2(
        PACKAGE / "summaries/THE_PRIMITIVE_GENERALIZED_FERMAT_EQUATION_357_FROM_FRONTIER_TO_PROOF.tex",
        RELEASE / "paper/THE_PRIMITIVE_GENERALIZED_FERMAT_EQUATION_357_FROM_FRONTIER_TO_PROOF.tex",
    )
    shutil.copy2(
        PACKAGE / "summaries/THE_PRIMITIVE_GENERALIZED_FERMAT_EQUATION_357_FROM_FRONTIER_TO_PROOF.pdf",
        RELEASE / "paper/THE_PRIMITIVE_GENERALIZED_FERMAT_EQUATION_357_FROM_FRONTIER_TO_PROOF.pdf",
    )
    shutil.copy2(PACKAGE / "PROGRAMS_AND_CERTIFICATES.md", RELEASE / "PROGRAMS_AND_CERTIFICATES.md")
    shutil.copy2(PACKAGE / "HECKE_COVERAGE_AND_OLD_NEW_NOTE.md", RELEASE / "HECKE_AMBIENT_COVERAGE.md")
    (RELEASE / "scripts").mkdir()
    for name in (
        "portable_python.py",
        "verify_dependency_closed_release.py",
        "verify_hilbert_hecke_filter_coverage.py",
        "verify_hilbert_hecke_ambient_coverage.py",
        "build_dependency_closed_release.py",
    ):
        shutil.copy2(PACKAGE / f"scripts/{name}", RELEASE / f"scripts/{name}")
        (RELEASE / f"scripts/{name}").chmod(0o755)
    (RELEASE / "inputs").mkdir()
    shutil.copy2(BASE / "inputs/EVIDENCE_MANIFEST_INDEX.json", RELEASE / "inputs/BASE_EVIDENCE_MANIFEST_INDEX_V1.json")
    write_text(
        RELEASE / "inputs/DEPENDENCY_CLOSURE_INDEX_V2.json",
        json.dumps(build_dependency_index(base_paths), indent=2, sort_keys=True) + "\n",
    )
    write_text(
        RELEASE / "inputs/SOFTWARE_VERSIONS_V2.json",
        json.dumps(software_versions(), indent=2, sort_keys=True) + "\n",
    )
    write_docs()
    write_text(
        RELEASE / "inputs/SECTOR_REPLAY_INDEX_V2.json",
        json.dumps(build_sector_index(), indent=2, sort_keys=True) + "\n",
    )
    write_root_manifest()

    if args.run_sector_replays:
        output = clean_extraction_replay()
        write_replay_logs(output)
        write_root_manifest()

    deterministic_tar(RELEASE, ARCHIVE)
    write_text(
        PACKAGE / "anc/PRIMITIVE_357_REPRODUCIBILITY_V2.tar.gz.sha256",
        f"{sha256(ARCHIVE)}  {ARCHIVE.name}\n",
    )
    print(
        "PRIMITIVE_357_DEPENDENCY_CLOSED_BUILD=PASS "
        f"REPOSITORY_FILES={sum(1 for path in REPOSITORY.rglob('*') if path.is_file())} "
        f"ARCHIVE_SHA256={sha256(ARCHIVE)} SECTOR_LOG={int(args.run_sector_replays)}"
    )


if __name__ == "__main__":
    main()

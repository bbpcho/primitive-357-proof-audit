#!/usr/bin/env python3
"""Build the V3 primitive (3,5,7) proof/reproducibility release."""

from __future__ import annotations

import argparse
import gzip
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tarfile
import tempfile
import time
import zipfile


PACKAGE = Path(__file__).resolve().parents[1]
WORKSPACE = PACKAGE.parents[1]
V2_PACKAGE = WORKSPACE / "results/2026-09-11_primitive_357_provenance_paper_v1"
V2_RELEASE = V2_PACKAGE / (
    "dependency_closed_release_v2/"
    "2026-09-13_primitive_357_dependency_closed_release_v2")
OUTPUT = PACKAGE / "dependency_closed_release_v3"
RELEASE_NAME = "2026-09-13_primitive_357_dependency_closed_release_v3"
RELEASE = OUTPUT / RELEASE_NAME
REPOSITORY = RELEASE / "repository"
ROOT_MANIFEST = RELEASE / (
    "manifests/PRIMITIVE_357_DEPENDENCY_CLOSED_RELEASE_V3_SHA256SUMS.txt")
ARCHIVE = PACKAGE / "anc/PRIMITIVE_357_REPRODUCIBILITY_V3.tar.gz"
MISSING = PACKAGE / "review/v2_missing_evidence.txt"
AUDIT_BUNDLE = PACKAGE / "review/v2_audit_bundle.zip"
SAGE_ENV = Path("/tmp/beal357-p23-sage-runtime-v1/env")
PAPER_NAME = "THE_PRIMITIVE_GENERALIZED_FERMAT_EQUATION_357_FROM_FRONTIER_TO_PROOF"
FOUNDATIONAL_DIRECT_FILES = [
    "results/2026-08-21_descent_galois/checkpoints/local_condition_3.bin",
    "results/2026-08-21_descent_galois/checkpoints/local_condition_5.bin",
    "results/2026-08-21_descent_galois/checkpoints/local_condition_7_v2.bin",
    "results/2026-08-25_dyadic_stopping/checkpoints/p2_place1_direct_fake_rank4_v1.bin",
    "results/2026-08-25_global_assembly/checkpoints/p2_place1_direct_log_restriction_v1.bin",
    "results/2026-08-25_global_assembly/checkpoints/p2_place2_direct_log_restriction_v1.bin",
    "results/2026-08-25_source_class_bridge_resume/checkpoints/p7_orbit42_56_exact_tau_norms_v4_resume1.bin",
    "results/2026-08-26_literal_c_five_place_source_preimage_v2r2_source_implementation/inputs/literal_c_five_place_geometry_v2r2.gpdata",
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def write_text(path: Path, value: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(value, encoding="utf-8", newline="\n")


def safe_relative(value: str) -> Path:
    path = Path(value)
    if path.is_absolute() or not path.parts or ".." in path.parts:
        raise AssertionError(("unsafe relative path", value))
    return path


def copy_workspace_file(relative: str) -> None:
    source = WORKSPACE / safe_relative(relative)
    target = REPOSITORY / safe_relative(relative)
    if not source.is_file() or source.is_symlink():
        raise AssertionError(("missing or unsafe V3 dependency", relative))
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        if sha256(target) != sha256(source):
            raise AssertionError(("V3 dependency conflicts with V2", relative))
        return
    shutil.copy2(source, target)


def audit_references() -> dict[str, list[str]]:
    member = (
        "V2_INDEPENDENT_REVIEW/work/v2_audit/"
        "complete_review_closure_result.json")
    with zipfile.ZipFile(AUDIT_BUNDLE) as archive:
        payload = json.loads(archive.read(member))
    references: dict[str, set[str]] = {}
    for problem in payload["problems"]:
        if problem.get("kind") != "missing":
            continue
        references.setdefault(problem["path"], set()).add(problem["source"])
    return {path: sorted(sources) for path, sources in references.items()}


def role_for(path: str) -> str:
    suffix = Path(path).suffix
    if suffix in {".py", ".gp", ".sage", ".m"}:
        return "program"
    if suffix in {".bin", ".sobj", ".gpdata"}:
        return "serialized_exact_input"
    if suffix == ".log":
        return "execution_log"
    if suffix in {".json", ".txt"}:
        return "certificate_or_exact_text"
    return "documentation"


def copy_repaired_section7_package() -> list[str]:
    source = PACKAGE / "review/v2_basis_repair"
    target = REPOSITORY / "results/2026-09-13_section7_basis_kummer_repair_v1"
    target.mkdir(parents=True, exist_ok=True)
    copied = []
    for item in sorted(source.iterdir()):
        if not item.is_file() or item.is_symlink():
            continue
        shutil.copy2(item, target / item.name)
        copied.append((target / item.name).relative_to(REPOSITORY).as_posix())
    if len(copied) != 7:
        raise AssertionError(("unexpected Section 7 repair file count", copied))
    return copied


def create_generator_repairs() -> list[str]:
    relative = (
        "results/2026-08-31_p23_s19_alternative_km_base_chart_screen_v1/"
        "scripts/compute_p23_s19_full_log_matrix_v1.sage")
    source = REPOSITORY / relative
    expected = "91abe1af072868c55a7c2ec3b0d1d8a8622eed9dfe726a3b3aac1b7050d4e951"
    if sha256(source) != expected:
        raise AssertionError(("unexpected historical s19 generator", sha256(source)))
    old = "dumps, load, matrix, vector)"
    new = "dumps, identity_matrix, load, matrix, vector)"
    text = source.read_text(encoding="utf-8")
    if text.count(old) != 1:
        raise AssertionError("s19 import repair occurrence is not unique")
    target_relative = (
        "results/2026-09-13_v3_generator_repairs/"
        "compute_p23_s19_full_log_matrix_v1_import_repair.sage")
    target = REPOSITORY / target_relative
    write_text(target, text.replace(old, new))
    return [target_relative]


def repository_rows() -> list[dict[str, object]]:
    return [
        {
            "path": path.relative_to(REPOSITORY).as_posix(),
            "sha256": sha256(path),
            "bytes": path.stat().st_size,
        }
        for path in sorted(REPOSITORY.rglob("*"))
        if path.is_file()
    ]


def build_indexes(base_count: int, section7_paths: list[str],
                  generator_repairs: list[str]) -> None:
    references = audit_references()
    missing_paths = [line for line in MISSING.read_text(encoding="utf-8").splitlines()
                     if line]
    if len(missing_paths) != 100 or len(set(missing_paths)) != 100:
        raise AssertionError("review missing-evidence inventory is not exactly 100 paths")
    restored = []
    for relative in missing_paths:
        path = REPOSITORY / safe_relative(relative)
        restored.append({
            "path": relative,
            "sha256": sha256(path),
            "bytes": path.stat().st_size,
            "role": role_for(relative),
            "referenced_by": references.get(relative, []),
        })
    all_rows = repository_rows()
    index = {
        "schema": "primitive_357_dependency_closure_index_v3",
        "base_release": "2026-09-13_primitive_357_dependency_closed_release_v2",
        "base_repository_file_count": base_count,
        "review_bundle_sha256": sha256(AUDIT_BUNDLE),
        "review_finding": (
            "V2 ordinary sector replay omitted 100 transitive rank/descent and "
            "global-log dependencies; V3 restores every listed live path."
        ),
        "restored_missing_evidence": restored,
        "restored_missing_evidence_count": len(restored),
        "direct_generator_dependencies_beyond_review_minimum": [
            {
                "path": relative,
                "sha256": sha256(REPOSITORY / relative),
                "bytes": (REPOSITORY / relative).stat().st_size,
                "role": role_for(relative),
            }
            for relative in FOUNDATIONAL_DIRECT_FILES
        ],
        "section7_kummer_repair": [
            {
                "path": path,
                "sha256": sha256(REPOSITORY / path),
                "bytes": (REPOSITORY / path).stat().st_size,
            }
            for path in section7_paths
        ],
        "failure_prompted_generator_repairs": [
            {
                "path": path,
                "sha256": sha256(REPOSITORY / path),
                "bytes": (REPOSITORY / path).stat().st_size,
                "scope": "one missing Sage identity_matrix import; no arithmetic change",
            }
            for path in generator_repairs
        ],
        "repository_files": all_rows,
        "repository_file_count": len(all_rows),
        "exact_set_policy": True,
    }
    write_text(
        RELEASE / "inputs/DEPENDENCY_CLOSURE_INDEX_V3.json",
        json.dumps(index, indent=2, sort_keys=True) + "\n",
    )
    regeneration = {
        "schema": "primitive_357_foundational_regeneration_index_v3",
        "scope": [
            "fresh producer and answer-isolated five-place source reconstruction",
            "fresh semantic comparison of both five-place outputs",
            "Selmer character-projector and Mordell-Weil rank-four deduction",
            "fresh s=4 and s=19 global abelian logarithm matrices at p=23",
            "fresh combined rank-four annihilator and five local gates",
            "fresh exceptional P1 second-order and lifted-root calculations",
            "independent Section 7 finite-field Kummer 2-saturation witness",
        ],
        "entrypoint": "scripts/run_foundational_replays_v3.py",
        "clean_command": (
            "python3 -B scripts/verify_dependency_closed_release_v3.py "
            "--run-sector-replays --run-foundational-replays "
            "--require-original-workspace-absent"
        ),
        "output_comparison": {
            "GP_text_and_semantics": "exact",
            "Sage_serialized_caches": (
                "fresh identity recorded; Sage compression is not treated as canonical"
            ),
            "Sage_JSON": (
                "all invariant mathematical fields exact after deleting measured "
                "wall_seconds and the incidental compressed-cache identity"
            ),
            "combined_rank_and_local_certificates": "exact",
        },
        "software": {
            "python": "3.12",
            "pari_gp": "2.15.4",
            "sage": "10.9",
            "sympy": "1.14.0",
            "mpmath": "1.3.0",
        },
    }
    write_text(
        RELEASE / "inputs/FOUNDATIONAL_REGENERATION_INDEX_V3.json",
        json.dumps(regeneration, indent=2, sort_keys=True) + "\n",
    )


def copy_release_scripts() -> None:
    scripts = {
        "portable_python.py": PACKAGE / "scripts/portable_python.py",
        "verify_dependency_closed_release_v3.py": (
            PACKAGE / "scripts/verify_dependency_closed_release_v3.py"),
        "run_foundational_replays_v3.py": (
            PACKAGE / "scripts/run_foundational_replays_v3.py"),
        "verify_hilbert_hecke_filter_coverage.py": (
            PACKAGE / "scripts/verify_hilbert_hecke_filter_coverage.py"),
        "verify_hilbert_hecke_ambient_coverage.py": (
            PACKAGE / "scripts/verify_hilbert_hecke_ambient_coverage.py"),
        "build_dependency_closed_release_v3.py": Path(__file__),
    }
    for name, source in scripts.items():
        target = RELEASE / "scripts" / name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
        target.chmod(0o755)


def copy_review_material() -> None:
    target = RELEASE / "review"
    target.mkdir(parents=True, exist_ok=True)
    for name in (
        "v2_audit_bundle.zip",
        "v2_audit_bundle.zip.sha256",
        "v2_review.md",
        "v2_missing_evidence.txt",
        "v2_proposed_corrections.patch",
        "v2_release_docs_corrections.patch",
    ):
        shutil.copy2(PACKAGE / "review" / name, target / name)


def write_docs() -> None:
    readme = """# Primitive (3,5,7) proof and reproducibility release V3

V3 responds directly to the independent V2 review. It retains V2 byte-for-byte
as its base, restores all 100 omitted transitive dependencies, adds an explicit
generator-to-input index, exposes the rank/descent and global-log generators as
a required clean replay, and supplies the independent finite-field Kummer
repair for the Section 7 two-saturation argument.

Fast integrity and Kummer checks:

    python3 -B scripts/verify_dependency_closed_release_v3.py

Full clean mathematical replay:

    python3 -B scripts/verify_dependency_closed_release_v3.py \
      --run-sector-replays --run-foundational-replays

The sealed build additionally runs that command inside an empty-root
bubblewrap namespace with the original workspace path absent. See
logs/CLEAN_EXTRACTION_COMPLETE_REPLAY_V3.log and
inputs/FOUNDATIONAL_REGENERATION_INDEX_V3.json.

The paper source incorporates the independent review's mathematical and
attribution corrections. The author field remains deliberately blank until
the submitting author supplies the desired name and affiliation.
"""
    changelog = """# Changelog: dependency-closed V2 to V3

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
"""
    write_text(RELEASE / "README.md", readme)
    write_text(RELEASE / "CHANGELOG.md", changelog)

    guide = (V2_PACKAGE / "PROGRAMS_AND_CERTIFICATES.md").read_text(
        encoding="utf-8")
    guide = guide.replace("646 evidence files", "765 evidence files")
    guide = guide.replace("649 evidence files", "765 evidence files")
    guide = guide.replace("exact 646-file repository closure",
                          "exact 765-file repository closure")
    guide = guide.replace("exact 649-file repository closure",
                          "exact 765-file repository closure")
    guide = guide.replace("133 Python programs", "138 Python programs")
    guide = guide.replace("21 PARI/GP programs", "39 PARI/GP programs")
    guide = guide.replace("17 Sage programs", "25 Sage programs")
    guide = guide.replace("17 SageMath programs", "25 SageMath programs")
    guide = guide.replace("191 mathematical program sources",
                          "222 mathematical program sources")
    guide = guide.replace(
        "Five additional Python programs build, relocate, audit the Hecke filters and\n"
        "ambient modules, and verify the release itself.",
        "Seven release-level Python programs build and relocate the release, audit the\n"
        "Hecke filters and ambient modules, run the foundational reconstruction, and\n"
        "verify the release itself.",
    )
    guide = guide.replace(
        "PRIMITIVE_357_REPRODUCIBILITY_V2.tar.gz",
        "PRIMITIVE_357_REPRODUCIBILITY_V3.tar.gz",
    )
    guide = guide.replace(
        "2026-09-13_primitive_357_dependency_closed_release_v2",
        "2026-09-13_primitive_357_dependency_closed_release_v3",
    )
    guide = guide.replace(
        "scripts/verify_dependency_closed_release.py",
        "scripts/verify_dependency_closed_release_v3.py",
    )
    guide = guide.replace(
        "inputs/SOFTWARE_VERSIONS_V2.json",
        "inputs/SOFTWARE_VERSIONS_V3.json",
    )
    guide = guide.replace(
        "The release deliberately does not redistribute published papers.",
        "The release includes checksum-pinned copies of the Putz thesis, the "
        "PVT preprint, and the earlier composition review in "
        "repository/references/.")
    guide += """

## V3 foundational replay

V3 adds the 100 evidence paths omitted from V2 and the independently checked
Section 7 Kummer repair. The complete generator map is
inputs/FOUNDATIONAL_REGENERATION_INDEX_V3.json; the file-by-file closure is
inputs/DEPENDENCY_CLOSURE_INDEX_V3.json. The V3 clean replay regenerates the
five-place rank/descent outputs and both global logarithm branches rather than
only authenticating their saved conclusions. The exact full command is:

    python3 -B scripts/verify_dependency_closed_release_v3.py \\
      --run-sector-replays --run-foundational-replays
"""
    write_text(RELEASE / "PROGRAMS_AND_CERTIFICATES.md", guide)


def write_sector_index() -> None:
    source = json.loads(
        (V2_RELEASE / "inputs/SECTOR_REPLAY_INDEX_V2.json").read_text())
    source["schema"] = "primitive_357_sector_replay_index_v3"
    write_text(
        RELEASE / "inputs/SECTOR_REPLAY_INDEX_V3.json",
        json.dumps(source, indent=2, sort_keys=True) + "\n",
    )
    versions = json.loads(
        (V2_RELEASE / "inputs/SOFTWARE_VERSIONS_V2.json").read_text())
    versions["schema"] = "primitive_357_dependency_closed_software_versions_v3"
    versions["v3_foundational_replay"] = {
        "python": "3.12",
        "pari_gp": "2.15.4",
        "sage": "10.9",
        "sympy": "1.14.0",
        "mpmath": "1.3.0",
        "independent_review_bundle": sha256(AUDIT_BUNDLE),
    }
    write_text(
        RELEASE / "inputs/SOFTWARE_VERSIONS_V3.json",
        json.dumps(versions, indent=2, sort_keys=True) + "\n",
    )


def compile_paper() -> None:
    paper = RELEASE / "paper" / f"{PAPER_NAME}.tex"
    environment = {
        "PATH": "/usr/bin:/bin",
        "HOME": "/tmp",
        "LANG": "C.UTF-8",
        "LC_ALL": "C.UTF-8",
    }
    outputs = []
    for _ in range(3):
        completed = subprocess.run(
            ["/usr/bin/pdflatex", "-interaction=nonstopmode",
             "-halt-on-error", paper.name],
            cwd=paper.parent,
            env=environment,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=300,
            check=False,
        )
        outputs.append(completed.stdout)
        if completed.returncode:
            raise RuntimeError(completed.stdout[-12000:])
    write_text(RELEASE / "logs/PAPER_COMPILE_V3.log", "\n".join(outputs))


def write_root_manifest() -> None:
    files = sorted(path for path in RELEASE.rglob("*")
                   if path.is_file() and path != ROOT_MANIFEST)
    rows = [
        f"{sha256(path)}  {path.relative_to(RELEASE).as_posix()}"
        for path in files
    ]
    write_text(ROOT_MANIFEST, "\n".join(rows) + "\n")


def deterministic_tar(source: Path, target: Path) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("wb") as raw:
        with gzip.GzipFile(filename="", mode="wb", fileobj=raw, mtime=0) as zipped:
            with tarfile.open(fileobj=zipped, mode="w",
                              format=tarfile.PAX_FORMAT) as archive:
                for path in sorted(source.rglob("*"),
                                   key=lambda item: item.as_posix()):
                    relative = Path(source.name) / path.relative_to(source)
                    info = archive.gettarinfo(str(path), arcname=relative.as_posix())
                    info.uid = info.gid = 0
                    info.uname = info.gname = ""
                    info.mtime = 0
                    if path.is_file():
                        with path.open("rb") as handle:
                            archive.addfile(info, handle)
                    else:
                        archive.addfile(info)


def clean_extraction_replay() -> str:
    with tempfile.TemporaryDirectory(prefix="primitive357-v3-clean-") as temporary:
        temporary_root = Path(temporary)
        candidate = temporary_root / "candidate.tar.gz"
        deterministic_tar(RELEASE, candidate)
        with tarfile.open(candidate, "r:gz") as archive:
            archive.extractall(temporary_root, filter="data")
        clean = temporary_root / RELEASE_NAME
        dependency_site = temporary_root / "site-packages"
        dependency_site.mkdir()
        source_site = (
            WORKSPACE /
            "results/2026-08-20_descent_support/.venv/lib/python3.12/site-packages")
        for pattern in ("sympy", "sympy-*.dist-info", "mpmath", "mpmath-*.dist-info"):
            for source in source_site.glob(pattern):
                if source.is_dir():
                    shutil.copytree(source, dependency_site / source.name)
        if not SAGE_ENV.is_dir():
            raise AssertionError("Sage 10.9 replay environment is unavailable")
        command = [
            "/usr/bin/bwrap", "--die-with-parent", "--unshare-all", "--new-session",
            "--clearenv", "--tmpfs", "/", "--proc", "/proc", "--dev", "/dev",
            "--tmpfs", "/tmp", "--ro-bind", "/usr", "/usr",
            "--symlink", "usr/bin", "/bin", "--symlink", "usr/lib", "/lib",
            "--symlink", "usr/lib64", "/lib64",
            "--ro-bind", "/etc/alternatives", "/etc/alternatives",
            "--bind", str(clean), "/release",
            "--ro-bind", str(dependency_site), "/dependencies",
            "--dir", "/tmp/beal357-p23-sage-runtime-v1",
            "--ro-bind", str(SAGE_ENV), "/tmp/beal357-p23-sage-runtime-v1/env",
            "--setenv", "PATH", "/usr/bin:/bin",
            "--setenv", "HOME", "/tmp",
            "--setenv", "LANG", "C.UTF-8", "--setenv", "LC_ALL", "C.UTF-8",
            "--setenv", "PYTHONDONTWRITEBYTECODE", "1",
            "--setenv", "PYTHONINTMAXSTRDIGITS", "0",
            "--setenv", "PYTHONPATH", "/dependencies",
            "--setenv", "BEAL357_SAGE_PYTHON",
            "/tmp/beal357-p23-sage-runtime-v1/env/bin/python",
            "--setenv", "BEAL357_FLINT_PREFIX",
            "/tmp/beal357-p23-sage-runtime-v1/env",
            "--chdir", "/release",
            "/usr/bin/python3", "-B",
            "/release/scripts/verify_dependency_closed_release_v3.py",
            "--run-sector-replays", "--run-foundational-replays",
            "--require-original-workspace-absent",
        ]
        started = time.monotonic()
        completed = subprocess.run(
            command,
            cwd=temporary_root,
            env={
                "PATH": "/usr/bin:/bin",
                "HOME": "/tmp",
                "LANG": "C.UTF-8",
                "LC_ALL": "C.UTF-8",
                "PYTHONDONTWRITEBYTECODE": "1",
                "PYTHONINTMAXSTRDIGITS": "0",
            },
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=30000,
            check=False,
        )
        output = (
            "CLEAN_EXTRACTION=EMPTY_ROOT_WRITABLE_EPHEMERAL_RELEASE\n"
            "ORIGINAL_WORKSPACE=ABSENT\n"
            f"EXIT={completed.returncode}\n"
            f"WALL_SECONDS={time.monotonic()-started:.6f}\n"
            + completed.stdout
        )
        if completed.returncode:
            raise RuntimeError(output[-40000:])
        return output


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-clean-replays", action="store_true")
    args = parser.parse_args()
    if OUTPUT.exists():
        shutil.rmtree(OUTPUT)
    shutil.copytree(V2_RELEASE, RELEASE)
    base_count = sum(1 for path in REPOSITORY.rglob("*") if path.is_file())
    if base_count != 649:
        raise AssertionError(("unexpected V2 repository file count", base_count))

    missing_paths = [line for line in MISSING.read_text(encoding="utf-8").splitlines()
                     if line]
    for relative in missing_paths:
        copy_workspace_file(relative)
    for relative in FOUNDATIONAL_DIRECT_FILES:
        copy_workspace_file(relative)
    section7_paths = copy_repaired_section7_package()
    generator_repairs = create_generator_repairs()

    copy_release_scripts()
    copy_review_material()
    shutil.copy2(
        PACKAGE / "summaries" / f"{PAPER_NAME}.tex",
        RELEASE / "paper" / f"{PAPER_NAME}.tex",
    )
    write_sector_index()
    build_indexes(base_count, section7_paths, generator_repairs)
    write_docs()
    compile_paper()
    write_root_manifest()

    if args.run_clean_replays:
        output = clean_extraction_replay()
        write_text(RELEASE / "logs/CLEAN_EXTRACTION_COMPLETE_REPLAY_V3.log", output)
        write_root_manifest()

    deterministic_tar(RELEASE, ARCHIVE)
    write_text(
        PACKAGE / "anc/PRIMITIVE_357_REPRODUCIBILITY_V3.tar.gz.sha256",
        f"{sha256(ARCHIVE)}  {ARCHIVE.name}\n",
    )
    print(
        "PRIMITIVE_357_DEPENDENCY_CLOSED_BUILD_V3=PASS "
        f"REPOSITORY_FILES={sum(1 for path in REPOSITORY.rglob('*') if path.is_file())} "
        f"ARCHIVE_SHA256={sha256(ARCHIVE)} "
        f"CLEAN_REPLAY={int(args.run_clean_replays)}"
    )


if __name__ == "__main__":
    main()

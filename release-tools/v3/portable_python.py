#!/usr/bin/env python3
"""Execute an authenticated repository Python file with a relocatable root.

The evidence files themselves are not modified.  This launcher replaces only
the two historical machine-local path literals while compiling the source in
memory.  It also rejects any Python file access to the original workspace.
"""

from __future__ import annotations

import os
from pathlib import Path
import importlib.util
import subprocess
import sys


ORIGINAL_ROOT = "/home/pcho/Documents/Codex/beal_357"
ORIGINAL_SAGE = "/tmp/beal357-p23-sage-runtime-v1/env/bin/python"
EXTERNAL_RELOCATIONS = {
    "/home/pcho/Downloads/AUDIT_COMPOSITION_V2.md": "references/AUDIT_COMPOSITION_V2.md",
    "/home/pcho/Downloads/Thesis_CasperPutz.pdf": "references/Thesis_CasperPutz.pdf",
    "/tmp/2512.17845.pdf": "references/Pacetti_Villagra_Torcomian_2512.17845v1.pdf",
}


def install_bundled_python_dependencies() -> None:
    """Rediscover the clean release's read-only Python dependency mount."""
    configured = os.environ.get("BEAL357_DEPENDENCY_SITE")
    candidates = [Path(configured)] if configured else []
    candidates.append(Path("/dependencies"))
    for candidate in candidates:
        if not candidate.is_dir():
            continue
        rendered = str(candidate.resolve())
        if rendered not in sys.path:
            sys.path.insert(0, rendered)
        inherited = [
            item for item in os.environ.get("PYTHONPATH", "").split(os.pathsep) if item
        ]
        if rendered not in inherited:
            os.environ["PYTHONPATH"] = os.pathsep.join([rendered, *inherited])
        return


def repository_root() -> Path:
    configured = os.environ.get("BEAL357_REPOSITORY_ROOT")
    if configured:
        return Path(configured).resolve()
    here = Path(__file__).resolve()
    bundled = here.parents[1] / "repository"
    if bundled.is_dir():
        return bundled.resolve()
    if here.parent.name == ".portable":
        return here.parents[1]
    raise SystemExit("BEAL357_REPOSITORY_ROOT is not set")


def deny_original_workspace(event: str, arguments: tuple[object, ...]) -> None:
    if event != "open" or not arguments:
        return
    candidate = arguments[0]
    if isinstance(candidate, (str, bytes, os.PathLike)):
        rendered = os.fsdecode(candidate)
        if rendered == ORIGINAL_ROOT or rendered.startswith(ORIGINAL_ROOT + "/"):
            configured = os.environ.get("BEAL357_REPOSITORY_ROOT")
            if configured:
                allowed = str(Path(configured).resolve())
                if rendered == allowed or rendered.startswith(allowed + "/"):
                    return
            raise PermissionError("portable replay denied original-workspace access")


def main() -> None:
    install_bundled_python_dependencies()
    arguments = sys.argv[1:]
    while arguments and arguments[0] in {"-B", "-u", "-I"}:
        arguments.pop(0)
    if not arguments:
        raise SystemExit("usage: portable_python.py [-B] SCRIPT [ARGS ...]")
    root = repository_root()
    script = Path(arguments.pop(0)).resolve()
    script.relative_to(root)
    if (
        not script.is_file()
        or script.is_symlink()
        or script.suffix not in {".py", ".sage"}
    ):
        raise SystemExit(f"unsafe or missing Python source: {script}")

    source = script.read_text(encoding="utf-8")
    needs_sage = bool(
        script.suffix == ".sage"
        or "from sage." in source
        or "import sage." in source
        or "import sage\n" in source
    )
    sage_available = importlib.util.find_spec("sage") is not None
    if needs_sage and not sage_available:
        sage_python = Path(
            os.environ.get("BEAL357_SAGE_PYTHON", ORIGINAL_SAGE)
        ).resolve()
        if not sage_python.is_file() or sage_python == Path(__file__).resolve():
            raise SystemExit(
                "this replay needs SageMath; set BEAL357_SAGE_PYTHON to its Python executable"
            )
        completed = subprocess.run(
            [str(sage_python), "-B", str(Path(__file__).resolve()), "-B", str(script), *arguments],
            env=dict(os.environ),
            check=False,
        )
        raise SystemExit(completed.returncode)
    patched = source.replace(ORIGINAL_ROOT, str(root))
    patched = patched.replace(ORIGINAL_SAGE, str(Path(__file__).resolve()))
    for original, relative in EXTERNAL_RELOCATIONS.items():
        patched = patched.replace(original, str(root / relative))
    checked = patched.replace(str(root), "")
    if (
        ORIGINAL_ROOT in checked
        or ORIGINAL_SAGE in patched
        or any(original in patched for original in EXTERNAL_RELOCATIONS)
    ):
        raise AssertionError("historical path literal survived relocation")

    # Keep explicit historical /usr/bin/python3 children inside the same
    # in-memory relocation layer.  This is needed when a package verifier
    # starts a second authenticated Python program by absolute interpreter
    # path rather than by sys.executable.
    portable = str(Path(__file__).resolve())
    minimum_child_timeout = int(os.environ.get("BEAL357_MINIMUM_CHILD_TIMEOUT", "0"))
    original_run = subprocess.run

    def run_with_portability(*args, **kwargs):
        positional = list(args)
        command = kwargs.get("args", positional[0] if positional else None)
        if isinstance(command, (list, tuple)) and len(command) >= 3:
            rendered = list(command)
            if Path(str(rendered[0])).name in {"python", "python3"}:
                try:
                    child = Path(str(rendered[2])).resolve()
                    child.relative_to(root)
                except (OSError, ValueError):
                    pass
                else:
                    if rendered[1] == "-B" and child.suffix == ".py":
                        rendered[0] = portable
                        command = rendered
                        if "args" in kwargs:
                            kwargs["args"] = command
                        else:
                            positional[0] = command
        timeout = kwargs.get("timeout")
        if (
            minimum_child_timeout
            and timeout is not None
            and timeout < minimum_child_timeout
        ):
            kwargs["timeout"] = minimum_child_timeout
        return original_run(*positional, **kwargs)

    subprocess.run = run_with_portability

    sys.addaudithook(deny_original_workspace)
    sys.argv = [str(script), *arguments]
    script_directory = str(script.parent)
    if script_directory in sys.path:
        sys.path.remove(script_directory)
    sys.path.insert(0, script_directory)
    sys.executable = str(Path(__file__).resolve())
    os.environ["BEAL357_REPOSITORY_ROOT"] = str(root)
    # Use the real __main__ module dictionary, not an unregistered surrogate.
    # Historical multiprocessing verifiers pickle worker functions by their
    # __main__ name and therefore require those definitions to be discoverable
    # through sys.modules in forked children.
    namespace = sys.modules["__main__"].__dict__
    namespace.update({
        "__name__": "__main__",
        "__file__": str(script),
        "__package__": None,
        "__cached__": None,
    })
    exec(compile(patched, str(script), "exec"), namespace)


if __name__ == "__main__":
    main()

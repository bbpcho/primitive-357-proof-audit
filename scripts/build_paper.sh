#!/usr/bin/env bash
set -euo pipefail
repo_root="$(cd "$(dirname "$0")/.." && pwd)"
build_dir="$repo_root/build/paper"
mkdir -p "$build_dir"
cp "$repo_root/paper/manuscript.tex" "$repo_root/paper/rank-proof.tex" "$build_dir/"
cd "$build_dir"
for pass in 1 2 3; do
  pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error manuscript.tex
done
python3 - <<'PYLOG'
from pathlib import Path
import re
log=Path("manuscript.log").read_text(errors="replace")
issues=re.findall(r".*(?:undefined references|Citation .* undefined|Reference .* undefined|LaTeX Error|Overfull).*",log)
if issues:
    raise SystemExit("PAPER_BUILD=FAIL: " + "\n".join(issues))
PYLOG
echo "PAPER_BUILD=PASS $build_dir/manuscript.pdf"

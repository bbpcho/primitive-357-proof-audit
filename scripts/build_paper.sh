#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "$0")/.." && pwd)"
build_dir="$repo_root/build/paper"
mkdir -p "$build_dir"
cp "$repo_root/paper/manuscript.tex" "$build_dir/manuscript.tex"
cd "$build_dir"
pdflatex -interaction=nonstopmode -halt-on-error manuscript.tex
pdflatex -interaction=nonstopmode -halt-on-error manuscript.tex
pdflatex -interaction=nonstopmode -halt-on-error manuscript.tex
echo "PAPER_BUILD=PASS $build_dir/manuscript.pdf"

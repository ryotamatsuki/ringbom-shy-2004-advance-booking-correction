#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"
mkdir -p manuscript/build
latexmk -pdf -halt-on-error -interaction=nonstopmode \
  -outdir=manuscript/build manuscript/main.tex

if grep -E 'undefined references|undefined citations|Citation .* undefined|Reference .* undefined' manuscript/build/main.log; then
  echo "Unresolved citation or reference in manuscript build" >&2
  exit 1
fi

mkdir -p output/pdf
cp manuscript/build/main.pdf output/pdf/anonymous-manuscript.pdf

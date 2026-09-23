#!/usr/bin/env bash
set -euo pipefail

pdf="output/pdf/anonymous-manuscript.pdf"
tex="manuscript/main.tex"
test -s "$pdf"
info="$(pdfinfo "$pdf")"
printf '%s\n' "$info"

grep -q '^Title:.*A Correction to the Two-Type Refund Result in Ringbom and Shy (2004)' <<<"$info"
grep -q '^Author:.*Anonymous' <<<"$info"
pages="$(awk '/^Pages:/ {print $2}' <<<"$info")"
test "$pages" -ge 1
test "$pages" -le 7

# Public Economics Bulletin initial-submission requirements checked from source/PDF.
grep -Fq '\documentclass[12pt]{article}' "$tex"
grep -Fq '\usepackage[margin=1in]{geometry}' "$tex"

first_page="$(mktemp)"
trap 'rm -f "$first_page"' EXIT
pdftotext -f 1 -l 1 -layout "$pdf" "$first_page"
if grep -Fq 'A Correction to the Two-Type Refund Result' "$first_page"; then
  echo "Visible title found in initial-submission PDF" >&2
  exit 1
fi
if grep -Eq '^[[:space:]]*Abstract[[:space:]]*$' "$first_page"; then
  echo "Visible abstract heading found in initial-submission PDF" >&2
  exit 1
fi
if ! grep -Eq '^[[:space:]]*1[[:space:]]+Introduction[[:space:]]*$' "$first_page"; then
  echo "First page does not begin with numbered Introduction as required" >&2
  cat "$first_page" >&2
  exit 1
fi

font_table="$(pdffonts "$pdf")"
printf '%s\n' "$font_table"
if awk 'NR>2 && NF && $5 != "yes" { bad=1 } END { exit bad }' <<<"$font_table"; then
  :
else
  echo "At least one PDF font is not embedded" >&2
  exit 1
fi

#!/usr/bin/env bash
set -euo pipefail

pdf="output/pdf/anonymous-manuscript.pdf"
test -s "$pdf"
info="$(pdfinfo "$pdf")"
printf '%s\n' "$info"
grep -q '^Title:.*A Correction to the Two-Type Refund Result in Ringbom and Shy (2004)' <<<"$info"
grep -q '^Author:.*Anonymous' <<<"$info"
pages="$(awk '/^Pages:/ {print $2}' <<<"$info")"
test "$pages" -ge 1

font_table="$(pdffonts "$pdf")"
printf '%s\n' "$font_table"
if awk 'NR>2 && NF && $5 != "yes" { bad=1 } END { exit bad }' <<<"$font_table"; then
  :
else
  echo "At least one PDF font is not embedded" >&2
  exit 1
fi

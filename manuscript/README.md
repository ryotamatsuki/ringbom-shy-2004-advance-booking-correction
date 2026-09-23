# Manuscript build

`main.tex` is the anonymous manuscript source. It contains no author names, affiliations, acknowledgments, or identifying metadata. The target journal format will be applied only after the Stage 11 referee audit and Stage 12 candidate-universe decision.

Build from a clean checkout with:

```bash
bash scripts/build_manuscript.sh
```

The build creates an intermediate at `manuscript/build/main.pdf` and the clean anonymous submission PDF at `output/pdf/anonymous-manuscript.pdf`. The build log is checked for unresolved citations and references. Stage 14 records page count, embedded fonts, and PDF metadata in the QA ledger.

# Stage 9 — Repository and reproducibility setup

## Gate record

- Input commit: `fa3b516e7e48528515a08e60a69ea1974efcebed` (Stage 8 theory freeze).
- Output commit: to be recorded in `docs/STAGE_COMMIT_LEDGER.md` after CI evidence is available.
- Branch: `research/stage-00-evidence-freeze`.
- **Local verdict: PASS; remote clean-checkout CI pending.** Stage 9 closes after the pushed Python and manuscript jobs succeed.

## Repository changes

- Updated the root README, project status, claim boundary, and evidence map to the frozen correction result.
- Added deterministic `scripts/run_checks.sh` covering the symbolic derivation, exact headline example, independent correspondence enumerator, outside-option counterexample, uniform boundary and table audits, portability audit, compilation, and proof-placeholder scan.
- Added manuscript build and PDF QA scripts. The LaTeX source is under `manuscript/`; the clean anonymous PDF is generated at `output/pdf/anonymous-manuscript.pdf`.
- Added `.github/workflows/reproducibility.yml` for fresh Python and LaTeX builds. Existing pinned Lean CI remains in `.github/workflows/formal-verification.yml`.
- Kept `requirements.txt` as the exact Python dependency record (`sympy==1.14.0`); Lean/mathlib versions are pinned in `formal/lean-toolchain` and `formal/lake-manifest.json`.
- The build omits generated LaTeX auxiliaries and Python caches. The publisher's copyrighted source PDF remains excluded.

## Evidence run

- `bash scripts/run_checks.sh`: PASS. This includes 800 seeded exact-rational random correspondence cases, 21 directed edge regressions, the Eq. (6) counterexample, Corollary 1 outside option, both Table 1 private-rate discrepancies, all other checked table values, rate/cash normalization, and non-normalized positive masses.
- `bash scripts/build_manuscript.sh`: PASS; no unresolved citations or references. Output is 5 pages.
- `bash scripts/check_pdf.sh`: PASS; PDF title and anonymous author metadata match the source, every listed font is embedded, page count is 5, and no encryption/forms/JavaScript are present.
- Visual render at 110 dpi: all five pages reviewed; no clipping, broken math, overlap, or orphaned section header remains.
- A fresh local Lean invocation was unavailable because `lake` is not installed in this execution image. The pinned GitHub Actions run for the unchanged formal files, run 9 on commit `6562740410460f48418baabff5b44912346db35e`, built `RingbomShy` and passed placeholder and axiom checks. The existing formal certificate documents that run.

## Portability and source limits

The README gives clean-checkout Python, Lean, and manuscript commands. The LaTeX PDF is source-reproducible but not promised byte-identical across TeX Live versions. `sources/source_manifest.md` records the publisher VOR, URL, page map, metadata, access date, and copyright handling. Its byte-level source-PDF SHA-256 remains visibly `UNRESOLVED`: the publisher bytes were not available through the read-only retrieval channel, and no digest is invented.

## Next-stage contract

Stage 10 will freeze the section-by-section manuscript against the frozen theorem ledger. Stage 11 must attack every material claim in the compiled draft before any journal selection. No submission or Stage 15 action is authorized.

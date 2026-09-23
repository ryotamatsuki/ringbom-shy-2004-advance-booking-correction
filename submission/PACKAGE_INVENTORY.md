# Stage-14 Submission Package Inventory

## Manuscript

- `manuscript/main.tex` — journal-integrated anonymous initial-submission source.
- CI-built anonymous manuscript PDF — 5 pages; QA SHA-256 `6dd03d476a6c110dcc86c0fdb38a853fb683a6a84a528bc158d27ec44527c401`.
- `submission/SUBMISSION_METADATA.md` — title, abstract, keywords, JEL, and portal metadata placeholders.
- Separate title page: **not included**, because Economics Bulletin generates it from metadata.
- Separate appendix: **not required for the mathematical correction**.
- `submission/REPRODUCIBILITY_SUPPLEMENT.md` — optional referee-facing supplement manifest.

## Verification

- `derivations/two_type_global_correspondence.md`
- `derivations/uniform_rederivation.md`
- `derivations/source_transcription.md`
- `code/symbolic_checks.py`
- `code/independent_correspondence.py`
- `code/stage11_hostile_referee.py`
- exact counterexample / table-audit result files under `results/`
- `docs/THEOREM_CERTIFICATES_STAGE04.md`
- `formal/AdvanceBookingCorrection.lean`
- `formal/FORMAL_VERIFICATION_CERTIFICATE.md`
- pinned Lean / mathlib toolchain files under `formal/`
- CI workflows under `.github/workflows/`

## Research records

- `sources/source_manifest.md`
- `PROVENANCE.md`
- `CLAIM_BOUNDARY.md`
- `EVIDENCE_MAP.md`
- Stage reports `docs/STAGE_00_EVIDENCE_FREEZE.md` through `docs/STAGE_14_SUBMISSION_QA.md`
- novelty/prior-disclosure ledgers under `results/`
- `docs/STAGE_07_IMPACT_MAP.md`
- `docs/STAGE_07_5A_PORTABILITY_CERTIFICATE.md`
- certification-regression records under `docs/CERTIFICATION_REGRESSION_*.md`
- hostile-referee report `docs/STAGE_11_HOSTILE_REFEREE.md`

## Submission-facing records

- `submission/JOURNAL_CANDIDATE_UNIVERSE.md`
- `submission/JOURNAL_FIT_MATRIX.md`
- `submission/JOURNAL_REQUIREMENTS_LEDGER.md`
- `submission/COVER_LETTER_DRAFT.md`
- `submission/DECLARATIONS_DRAFT.md`
- `submission/SUBMISSION_CHECKLIST.md`
- `submission/AUTHENTICATED_PORTAL_PREFLIGHT.md`
- this inventory.

## Deliberately absent

- Publisher VOR PDF: not committed for copyright/provenance reasons.
- Binding author declarations: not executed.
- Authenticated-portal screenshots/receipt: not available before author login.
- Submission confirmation / manuscript number: none, because no submission has been made.
- Stage 15 freeze/tag: not created.

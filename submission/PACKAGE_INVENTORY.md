# Stage-14 Submission Package Inventory

## Manuscript

- `manuscript/main.tex` — journal-integrated anonymous initial-submission source.
- Canonical submission PDF — generated from `manuscript/main.tex` by GitHub Actions and distributed only as a commit-specific workflow artifact (`submission-pdf-<commit SHA>`), together with its SHA-256 file. Generated PDFs are deliberately not tracked in Git, preventing a stale binary from diverging from the audited source.
- `submission/SUBMISSION_METADATA.md` — title, abstract, keywords, JEL, and portal metadata placeholders.
- Separate title page: **not included**, because Economics Bulletin generates it from metadata.
- Separate appendix: **not required for the mathematical correction**.
- `submission/REPRODUCIBILITY_SUPPLEMENT.md` — optional referee-facing supplement manifest.

## Verification

- `derivations/two_type_global_correspondence.md`
- `derivations/uniform_rederivation.md`
- `derivations/source_transcription.md`
- `code/symbolic_derivation.py`
- `code/independent_correspondence.py`
- `code/stage11_hostile_referee.py`
- exact counterexample / table-audit result files under `results/`
- `docs/THEOREM_CERTIFICATES_STAGE04.md`
- `formal/RingbomShy.lean`
- `formal/RingbomShy/Refund.lean`
- `formal/RingbomShy/AxiomAudit.lean`
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

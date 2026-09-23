# Stage-14 Submission Package Inventory

## Manuscript

- `manuscript/main.tex` — remediated, journal-integrated anonymous initial-submission source.
- Canonical submission PDF — generated from `manuscript/main.tex` by GitHub Actions and distributed only as a commit-specific workflow artifact. Generated PDFs are deliberately not tracked in Git.
- Current certified source commit: `10c831d97569281c91a2a7686fb405c2ca83865a`.
- Current workflow run: `35819784957` — SUCCESS.
- Current artifact: `submission-pdf-10c831d97569281c91a2a7686fb405c2ca83865a`, artifact ID `10732269176`.
- Current PDF SHA-256: `5a78a8db1a57e72997dea1227a30557f29fa9301bab1987bf8481af53fe7ffe2`.
- PDF: 5 pages; no visible title page/abstract; first visible heading `1 Introduction`; all fonts embedded; all five pages visually inspected.
- `submission/SUBMISSION_METADATA.md` — title, abstract, keywords, JEL, and portal metadata placeholders.
- Separate title page: **not included**, because Economics Bulletin generates it from metadata.
- Separate appendix: **not required for the mathematical correction**.
- `submission/REPRODUCIBILITY_SUPPLEMENT.md` — optional referee-facing supplement manifest.

## Verification

- `derivations/two_type_global_correspondence.md`
- `derivations/uniform_rederivation.md`
- `derivations/source_transcription.md`
- `code/symbolic_derivation.py`
- `code/counterexample_exact.py`
- `code/corollary_counterexample.py`
- `code/independent_correspondence.py`
- `code/stage11_hostile_referee.py`
- `code/uniform_boundary_audit.py`
- `code/uniform_table_audit_exact.py`
- `code/portability_audit_exact.py`
- exact counterexample / table-audit result files under `results/`
- `docs/THEOREM_CERTIFICATES_STAGE04.md`
- `formal/RingbomShy.lean`
- `formal/RingbomShy/Refund.lean`
- `formal/RingbomShy/AxiomAudit.lean`
- `formal/FORMAL_VERIFICATION_CERTIFICATE.md`
- pinned Lean / mathlib toolchain files under `formal/`
- CI workflow under `.github/workflows/reproducibility.yml`
- standard checker entry point `scripts/run_checks.sh`, which now includes the Stage-11 hostile-referee checker.

## Astra remediation record

- `docs/STAGE_14A_ASTRA_REMEDIATION.md` — one-to-one closure map for M01 and C01–C12.
- stale `output/pdf/anonymous-manuscript.pdf`: **removed from Git**.
- `.gitignore`: generated submission PDF/checksum ignored.
- `scripts/check_pdf.sh`: fails if a generated submission PDF is tracked.
- CI: generates a SHA-256 companion file and uses a commit-specific artifact name.

## Research records

- `sources/source_manifest.md`
- `PROVENANCE.md`
- `CLAIM_BOUNDARY.md`
- `EVIDENCE_MAP.md`
- Stage reports through `docs/STAGE_14_SUBMISSION_QA.md`
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

- Repository-tracked submission PDF: deliberately absent; the canonical copy is the commit-specific CI artifact.
- Publisher VOR PDF: not committed for copyright/provenance reasons.
- Binding author declarations: not executed.
- Authenticated-portal screenshots/receipt: not available before author login.
- Submission confirmation / manuscript number: none, because no submission has been made.
- Stage 15 freeze/tag: not created.

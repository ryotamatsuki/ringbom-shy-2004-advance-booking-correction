# Project Status

## Target

Staffan Ringbom and Oz Shy (2004), “Advance Booking, Cancellations, and Partial Refunds,” *Economics Bulletin* 13(1), 1–7.

## Current stage

**Stage 14 — CONDITIONAL PASS — AUTHENTICATED PORTAL PREFLIGHT REQUIRED.**

The independent Astra pre-submission audit has been fully remediated. No fatal mathematical defect was found. The publication-facing manuscript, reproducibility entry points, canonical PDF policy, and unauthenticated submission QA are re-certified. Stage 15 has not been entered and no submission has been made.

## Gate state

- Source/VOR identity and source-page map: PASS; byte-level VOR SHA-256 remains explicitly unresolved because the publisher byte stream was unavailable. No hash is fabricated.
- Corrected two-type endpoint theorem and exact strict-reversal counterexample: PASS.
- Complete feasible refund correspondence, boundaries, weak ties, no-reservation plateau, equality branch, and negative-profit cases: PASS.
- Original Corollary 1 qualification: PASS WITH QUALIFICATION; the high-price direction now has an analytic counterfamily valid arbitrarily close to `p=β`, and the other comparative-static directions are explicitly conditioned on feasibility and global profitability rather than promoted into new theorems.
- Uniform section: PASS on `β>p>c≥s≥0`; private upper-bound/globality and planner-cutoff feasibility are explicit; the former claim that `p>c` is pointwise necessary for strictness has been removed.
- Table 1: two private-refund entries corrected; all other audited Table 1 values reproduce.
- Table 2: all audited welfare-loss entries reproduce.
- Novelty / prior-disclosure: PASS WITH QUALIFICATION; no public correction/equivalent result located in the bounded search; no absolute-priority claim.
- Formal verification: PASS for the frozen proof-critical subset in `formal/FORMAL_VERIFICATION_CERTIFICATE.md`; full correspondence and uniform welfare calculus remain analytic with independent exact checks.
- Stage 8 theory freeze: PASS, commit `fa3b516e7e48528515a08e60a69ea1974efcebed`.
- Stage 9 reproducibility: PASS.
- Stage 10 manuscript construction: PASS.
- Stage 11 hostile-referee audit: PASS; the Stage-11 checker is now included in the standard `scripts/run_checks.sh` path.
- Stage 12 journal positioning: PASS; primary = *Economics Bulletin* / Comment; stretch = *Review of Industrial Organization*; realistic fallback = *Economics and Business Letters*.
- Stage 13 journal integration: PASS after the Astra-targeted prose/proof-architecture remediation recorded in `docs/STAGE_14A_ASTRA_REMEDIATION.md`.
- Stage 14 automated/public QA: PASS after remediation.
- Canonical QA source commit: `10c831d97569281c91a2a7686fb405c2ca83865a`.
- GitHub Actions run: `35819784957` — SUCCESS for both exact-checks and manuscript jobs.
- Canonical artifact: `submission-pdf-10c831d97569281c91a2a7686fb405c2ca83865a`, artifact ID `10732269176`.
- Final submission PDF: 5 pages; exact artifact visually reviewed page-by-page; all fonts embedded; SHA-256 `5a78a8db1a57e72997dea1227a30557f29fa9301bab1987bf8481af53fe7ffe2`.
- Stale tracked PDF: REMOVED. Generated submission PDFs are ignored by Git; CI artifacts are commit-specific and include a checksum file; PDF preflight fails if a generated PDF is tracked.
- Remaining blocker: authenticated portal fields plus author confirmation of factual/legal declarations.
- Actual submission / Stage 15: PROHIBITED / NOT PERFORMED.

## Current artifacts

See:
- `docs/STAGE_08_THEORY_FREEZE.md`
- `docs/STAGE_11_HOSTILE_REFEREE.md`
- `docs/STAGE_12_JOURNAL_POSITIONING.md`
- `docs/STAGE_13_FULL_PAPER_INTEGRATION.md`
- `docs/STAGE_14A_ASTRA_REMEDIATION.md`
- `docs/STAGE_14_SUBMISSION_QA.md`
- `submission/JOURNAL_REQUIREMENTS_LEDGER.md`
- `submission/PACKAGE_INVENTORY.md`
- `submission/SUBMISSION_CHECKLIST.md`

## Branch discipline

All work remains on `research/stage-00-evidence-freeze`. `main` has not been modified or merged. Stage 15 has not been entered. Any later substantive mathematical change must reopen the earliest affected stage.

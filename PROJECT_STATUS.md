# Project Status

## Target

Staffan Ringbom and Oz Shy (2004), “Advance Booking, Cancellations, and Partial Refunds,” *Economics Bulletin* 13(1), 1–7.

## Current stage

**Stage 9 — Reproducibility setup; local gates pass and clean-checkout CI is pending.** Stage 8 theory is frozen. The anonymous LaTeX draft is built and in visual review.

## Gate state

- Source/VOR identity and source-page map: PASS; PDF byte hash remains explicitly unresolved because publisher bytes were not available through the read-only retrieval path.
- Independent two-type endpoint derivation and exact counterexample: PASS.
- Complete feasible correspondence, boundaries, no-reservation option, and equality branch: PASS analytically; independent rational enumerator passes.
- Uniform section: PASS on `β>p>c≥s≥0`; two private Table 1 entries corrected; Table 2 and remaining checked entries reproduce.
- Novelty review: PASS WITH QUALIFICATION; no public correction/equivalent result found in the bounded search; no absolute priority claim.
- Formal verification: PASS for the theorem subset recorded in `formal/FORMAL_VERIFICATION_CERTIFICATE.md`; full correspondence and uniform welfare calculus remain analytic with independent exact checks.
- Stage 8 theory freeze: PASS, commit `fa3b516e7e48528515a08e60a69ea1974efcebed`.
- LaTeX manuscript: source and five-page clean build succeed; visual PDF QA and local font/metadata checks pass; Stage 11 audit and journal formatting remain.
- Stage 11 hostile-referee audit, Stage 12 journal universe, Stage 13 integration, Stage 14 requirements/preflight: NOT STARTED.
- Submission and Stage 15: PROHIBITED / NOT PERFORMED.

## Current artifacts

See `docs/STAGE_08_THEORY_FREEZE.md` for the theorem set and frozen scope; `docs/STAGE_07_IMPACT_MAP.md` for downstream effects; and `docs/STAGE_07_5A_PORTABILITY_CERTIFICATE.md` for quantifiers, tie convention, portability, and formal-verification limits.

## Branch discipline

All new work remains on `research/stage-00-evidence-freeze`. `main` has not been modified. Stage reports record input/output commit SHAs and tests. A later mathematical change must reopen the earliest affected stage.

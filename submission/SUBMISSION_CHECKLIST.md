# Economics Bulletin Comment — Submission Checklist

**Date:** 2026-09-23  
**Do not submit from this checklist. Stage 15 is prohibited.**

- [x] Frozen central theorem set unchanged after Stage 8.
- [x] Independent Astra pre-submission audit completed; no fatal mathematical defect found.
- [x] Astra M01 and C01–C12 remediated and mapped in `docs/STAGE_14A_ASTRA_REMEDIATION.md`.
- [x] Seller/consumer attribution of `q_L` corrected.
- [x] Advance-payment, cancellation, cost, and salvage accounting made explicit.
- [x] Original Corollary 1 distinguished from the new global profitability criterion.
- [x] High-price claim tested with an analytic family that persists as `p ↑ β`, plus directed exact regressions.
- [x] Global correspondence proof explicitly covers zero/negative profits and the interval after the last threshold.
- [x] No independent shutdown option has been added; only an available no-reservation plateau is used.
- [x] Uniform private upper-bound/globality and planner cutoff feasibility/globality made explicit.
- [x] Pointwise claim that strict inequality “needs `p>c`” removed; boundary regression added.
- [x] Source notation `r_1,r_2` mapped to `r_H,r_L`; `n>0` and correspondence/tie wording clarified.
- [x] Reproducibility paths point only to existing files.
- [x] Stage-11 hostile-referee checker is included in `scripts/run_checks.sh`.
- [x] Stale repository-tracked PDF removed.
- [x] Generated PDF/checksum ignored by Git and guarded by `scripts/check_pdf.sh`.
- [x] CI artifact is commit-specific and includes a SHA-256 file.
- [x] Fresh canonical QA source commit is `10c831d97569281c91a2a7686fb405c2ca83865a`.
- [x] Fresh GitHub Actions run `35819784957` completed SUCCESS.
- [x] Exact/symbolic/independent checks, including Stage 11, pass.
- [x] Manuscript build and automated PDF preflight pass.
- [x] PDF SHA-256 is `5a78a8db1a57e72997dea1227a30557f29fa9301bab1987bf8481af53fe7ffe2` and matches the CI checksum file.
- [x] PDF contains no visible title page and no abstract.
- [x] First visible heading is `1 Introduction`.
- [x] PDF length is 5 pages, below the 7-page public limit.
- [x] Manuscript is 12pt with one-inch margins and numbered sections.
- [x] All references and internal cross-references resolve.
- [x] All PDF fonts are embedded.
- [x] Exact generated PDF visually inspected page-by-page; no clipping, overlap, broken glyphs, malformed equations, or unreadable references.
- [x] Formal-verification certificate remains current within its explicitly limited scope.
- [x] Title, abstract, keywords, and JEL metadata draft prepared.
- [x] Cover letter draft prepared.
- [x] Data/code statement prepared.
- [x] AI/tool-use disclosure draft prepared without claiming journal approval.
- [x] Reproducibility supplement manifest repaired and prepared.
- [x] VOR is not redistributed in the repository.
- [x] Main branch remains untouched.
- [ ] **AUTHOR / PORTAL:** confirm author name, scholarly affiliation (if any), email, and any ORCID field.
- [ ] **AUTHOR / PORTAL:** confirm funding statement.
- [ ] **AUTHOR / PORTAL:** confirm competing-interests statement.
- [ ] **AUTHOR / PORTAL:** confirm acknowledgments, if any.
- [ ] **AUTHOR / PORTAL:** confirm prior-publication, preprint, and simultaneous-submission status.
- [ ] **AUTHOR / PORTAL:** confirm originality / institution-approval representations.
- [ ] **AUTHOR / PORTAL:** confirm the proposed AI/tool-use disclosure against the current authenticated prompt/policy.
- [ ] **PORTAL:** verify that the article-type control still shows `Comment`.
- [ ] **PORTAL:** verify abstract/keyword/JEL field limits and any required declarations.
- [ ] **PORTAL:** confirm the system-generated metadata/title-page preview.
- [ ] **PORTAL:** upload only for reversible preflight if desired; **do not press final Submit**.

## Stop condition

All Astra-remediable mathematical, manuscript, reproducibility, and PDF-identity findings are closed. Until the unchecked authenticated/author items are closed, the workflow status is:

**Stage 14 — CONDITIONAL PASS — AUTHENTICATED PORTAL PREFLIGHT REQUIRED.**

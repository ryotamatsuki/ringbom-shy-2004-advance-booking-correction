# Stage 14 — Submission QA

## Gate record

- Canonical workflow: research-paper-workflow v2.4, commit `63f11a50a13d9328213498a5a6576d00b9bceef7`.
- Independent pre-submission audit: Astra hostile-referee audit, remediated in `docs/STAGE_14A_ASTRA_REMEDIATION.md`.
- Canonical remediated source/PDF-QA commit: `10c831d97569281c91a2a7686fb405c2ca83865a`.
- Primary target: *Economics Bulletin*, article type **Comment**.
- Live public-compliance recheck date: 2026-09-23.
- Branch: `research/stage-00-evidence-freeze`.
- **Canonical verdict: CONDITIONAL GO.**
- **Stop state: Stage 14 — CONDITIONAL PASS — AUTHENTICATED PORTAL PREFLIGHT REQUIRED.**
- Stage 15: **NOT ENTERED**.
- Actual submission: **NOT PERFORMED**.
- Main branch: **NOT MODIFIED**.

## Astra remediation closure

The audit identified no fatal mathematical defect. Its single major package defect and all listed moderate/minor findings were addressed without expanding the model or changing the central corrected theorem.

Closed items include:

- stale repository-tracked PDF eliminated and canonical artifact policy enforced;
- seller/consumer attribution of `q_L` corrected;
- advance-payment, cancellation, cost, and salvage accounting made explicit;
- original Corollary 1 separated from the new global profitability criterion;
- the former single high-price point replaced by an analytic counterfamily persisting as `p ↑ β`;
- private upper-bound/globality and planner-cutoff feasibility made explicit;
- the false pointwise-necessity reading of `p>c` removed;
- negative-profit and final-interval cases made explicit in the global proof;
- “no-booking option” language replaced by an available no-reservation plateau, so no shutdown strategy is added;
- broken reproducibility paths repaired;
- Stage-11 hostile-referee checker added to the normal validation path;
- source notation `r_1,r_2` mapped explicitly to `r_H,r_L`;
- `n>0`, tie/correspondence wording, and the positive-mass to boundary-domain transition clarified.

The detailed one-to-one resolution map is in `docs/STAGE_14A_ASTRA_REMEDIATION.md`.

## Mathematical / reproducibility QA

No remediation changed the corrected missing-factor theorem, strict decision-reversal counterexample, or Table-1 correction values. A fresh reproducibility run was executed after the stale tracked PDF was removed and the PDF guard was active:

- workflow run: `35819784957`;
- source commit: `10c831d97569281c91a2a7686fb405c2ca83865a`;
- exact-checks job: **SUCCESS**;
- manuscript job: **SUCCESS**;
- the normal exact-check path now includes `code/stage11_hostile_referee.py`;
- the high-price Corollary counterfamily has directed exact regressions approaching `β`;
- `(β,p,c,s)=(1,1/2,1/2,1/4)` is regression-tested with `r̄=0` and `r*=1/2`, preventing a return to the erroneous pointwise claim that `p>c` is necessary for strictness.

The frozen Lean certificate remains scoped to the listed proof-critical subset. No claim is made that Lean formalizes the entire piecewise correspondence or uniform welfare calculus.

## Canonical PDF identity

The canonical submission PDF is no longer a Git-tracked binary. It is the commit-specific CI artifact generated from the audited source.

- Workflow run: `35819784957`.
- Artifact name: `submission-pdf-10c831d97569281c91a2a7686fb405c2ca83865a`.
- Artifact ID: `10732269176`.
- PDF file: `anonymous-manuscript.pdf`.
- PDF SHA-256: `5a78a8db1a57e72997dea1227a30557f29fa9301bab1987bf8481af53fe7ffe2`.
- The SHA-256 recomputed from the downloaded PDF exactly matches the checksum file produced in CI.
- The workflow-artifact ZIP digest is separate and must not be confused with the PDF digest.

The formerly tracked stale PDF and the earlier QA PDF SHA-256 `6dd03d476a6c110dcc86c0fdb38a853fb683a6a84a528bc158d27ec44527c401` are historical only and are **not submission-authoritative**.

## Exact PDF QA

The exact CI artifact above was downloaded, rendered, and independently inspected.

- Pages: **5**.
- Page size: US Letter, 612 x 792 pt.
- PDF version: 1.5.
- Encrypted: no.
- Visible title page: none.
- Visible abstract: none.
- First page: begins with **1 Introduction**.
- PDF metadata title: *A Correction to the Two-Type Refund Result in Ringbom and Shy (2004)*.
- PDF metadata author: Anonymous.
- Fonts: every font reported by `pdffonts` is embedded.
- Visual review: all five pages rendered at 180 dpi and inspected.
- No clipping, overlap, broken glyphs, malformed fractions, missing equation elements, or unreadable references were observed.
- QED boxes render normally.

Page-by-page:
1. Introduction and revised model/accounting explanation render cleanly; no visible title/abstract.
2. source-notation mapping, corrected Proposition 1, proof, and exact reversal counterexample render cleanly.
3. complete global correspondence and sign-independent domination proof render cleanly.
4. Corollary 1 qualification, analytic near-`β` high-price counterfamily, and uniform private-globality argument render cleanly.
5. planner feasibility/globality, welfare comparison, calibrated `p>c` statement, conclusion, and reference render cleanly.

The page 4-to-5 continuation is ordinary body flow and does not create an orphan, overlap, or readability problem.

## Journal compliance QA

The public journal requirements rechecked on 2026-09-23 remain the basis for the initial-submission package: Comment is an available peer-reviewed type; the initial manuscript is PDF; the public page limit is at most 7 printed pages excluding specified back matter; English, 12pt-compatible font, single spacing, one-inch margins, and Arabic-numbered sections are used. The initial uploaded PDF contains no visible title page or abstract and begins with Section 1.

The live initial-submission page and older linked guidance are not fully aligned on heading size. The manuscript follows the current live initial-submission presentation; the authenticated portal remains the final authority if it exposes a conflicting instruction.

No separate current public journal-wide generative-AI policy was located during the public Stage-14 check. The exact authenticated AI/declaration wording therefore remains unguessed and is reserved for portal preflight.

## Citation / source QA

- Every manuscript citation resolves.
- The sole manuscript reference is the target Ringbom–Shy article and is verified against the publisher record/VOR.
- No literature citation was inserted merely to inflate positioning.
- The VOR is not redistributed.
- VOR byte-level SHA-256 remains explicitly UNRESOLVED because raw publisher bytes were unavailable through the retrieval path; no digest is fabricated. This is not a blocker to identifying the source article or printed equations.

## Reproducibility path QA

The referee-facing entry points now resolve to real repository files:

- `code/symbolic_derivation.py`;
- `code/independent_correspondence.py`;
- `code/stage11_hostile_referee.py`;
- `formal/RingbomShy.lean`;
- `formal/RingbomShy/Refund.lean`;
- `formal/RingbomShy/AxiomAudit.lean`;
- `formal/FORMAL_VERIFICATION_CERTIFICATE.md`.

The nonexistent paths `code/symbolic_checks.py`, `formal/AdvanceBookingCorrection.lean`, and `formal/README.md` have been removed from the submission-facing inventory/supplement.

## Submission-facing QA

Ready:
- remediated manuscript source;
- canonical commit-specific anonymous initial-submission PDF;
- exact PDF checksum;
- abstract / keyword / JEL metadata;
- optional cover-letter draft;
- code/data statement;
- proposed AI/tool-use disclosure;
- reproducibility supplement manifest;
- candidate-universe and journal-fit records;
- current requirements ledger;
- package inventory;
- submission checklist.

Intentionally awaiting author/authenticated portal:
- identity, email, scholarly affiliation, ORCID if requested;
- funding and competing-interest facts;
- acknowledgments;
- preprint / prior-publication / simultaneous-submission facts;
- institution-approval/originality representations;
- exact current AI/declaration prompt wording;
- authenticated field limits and system-generated preview;
- confirmation that the authenticated article-type control still offers **Comment**.

## Why this is not a full PASS

The material mathematical, reproducibility, source/PDF-identity, and public-format issues identified by the Astra audit are closed. Full Stage-14 PASS remains fail-closed because authenticated portal controls and author factual/legal declarations cannot be inferred or accepted automatically.

Therefore the defensible stop state is:

**Stage 14 — CONDITIONAL PASS — AUTHENTICATED PORTAL PREFLIGHT REQUIRED.**

No Stage-15 freeze/tag and no submission action are performed.

## Next-stage contract

There is no authorized Stage-15 contract. The next human action is the reversible authenticated portal preflight in `submission/AUTHENTICATED_PORTAL_PREFLIGHT.md`: confirm the factual/legal fields and system-generated metadata preview, and stop before final Submit/send-to-editor.

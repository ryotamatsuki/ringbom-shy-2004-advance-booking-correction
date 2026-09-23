# Stage 14 — Submission QA

## Gate record

- Canonical workflow: research-paper-workflow v2.4, commit `63f11a50a13d9328213498a5a6576d00b9bceef7`.
- Input commit: `3b5f42f39fc268c7c0a73197f988083961462298` (Stage 13 integration closure).
- Output/closure commit: `2f1c472a6946ea58a8553d9b5471246cee66d2cc` (Stage 14 package and conditional-pass closure).
- Files added/updated at closure: `docs/STAGE_14_SUBMISSION_QA.md`, `submission/JOURNAL_REQUIREMENTS_LEDGER.md`, `submission/SUBMISSION_CHECKLIST.md`, `submission/PACKAGE_INVENTORY.md`, `submission/REPRODUCIBILITY_SUPPLEMENT.md`, `submission/AUTHENTICATED_PORTAL_PREFLIGHT.md`, and `PROJECT_STATUS.md`.
- Primary target: *Economics Bulletin*, article type **Comment**.
- Live compliance recheck: 2026-09-23.
- Branch: `research/stage-00-evidence-freeze`.
- **Canonical verdict: CONDITIONAL GO.**
- **Stop state: Stage 14 — CONDITIONAL PASS — AUTHENTICATED PORTAL PREFLIGHT REQUIRED.**
- Stage 15: **NOT ENTERED**.
- Actual submission: **NOT PERFORMED**.
- Main branch: **NOT MODIFIED**.

## Mathematical / reproducibility QA

No manuscript change after Stage 8 altered the frozen theory. Stage 11 independently re-attacked the paper and found no fatal/major mathematical defect or certification regression. The exact counterexample, complete source-model refund correspondence, uniform-section qualifications, two Table-1 corrections, theorem certificates, and formal-verification scope remain mutually consistent.

A final reproducibility workflow run (`35814240584`, source commit `256cf5d0ae39c260b11e78f5e140a64064801546`) completed successfully:
- exact/symbolic test job: PASS;
- manuscript job: PASS;
- submission PDF retained as CI artifact for inspection;
- all automated PDF preflight checks: PASS.

The workflow source and manuscript are unchanged after that build; subsequent Stage-13/14 commits are documentation/submission-record changes only.

## Exact PDF QA

The exact CI-generated PDF was downloaded from the workflow artifact and independently inspected.

- Pages: **5**.
- Page size: US Letter, 612 x 792 pt.
- PDF version: 1.5.
- Encrypted: no.
- Visible title page: none.
- Visible abstract: none.
- First page: begins with **1 Introduction**.
- Fonts: all fonts reported by `pdffonts` are embedded.
- QA PDF SHA-256: `6dd03d476a6c110dcc86c0fdb38a853fb683a6a84a528bc158d27ec44527c401`.
- Visual review: all five pages rendered at 180 dpi and inspected. No clipped text, overlaps, broken glyphs, malformed fractions, missing equation elements, bad page breaks, or unreadable references were observed.
- Proof-end squares render as normal QED boxes rather than missing-glyph artifacts.

Page-by-page:
1. Sections 1–2 begin cleanly; first visible line is the numbered Introduction; equations (1)–(6) fit within margins.
2. Corrected Proposition 1, proof, exact counterexample, and start of Section 4 render cleanly.
3. Complete correspondence, proof, Corollary 1, and no-booking example render cleanly.
4. Uniform-model formulas and welfare expression render cleanly.
5. Conclusion and single verified reference render cleanly; no orphaned substantive text.

## Journal compliance QA

The live public submission page again confirms: Comment is an available peer-reviewed type; initial manuscript is PDF; <=7 pages excluding specified back matter; English; 12pt compatible font; single spacing; one-inch margins; Arabic-numbered sections. The current linked author guide states that the uploaded PDF should not contain a title page and should begin with Section 1 because title/abstract/author metadata are generated from the submission interface.

A current 2026 *Economics Bulletin* paper demonstrates explicit Funding, Competing interests, Data availability, and Use of AI tools statements. However, a separate current public journal-wide AI policy and the exact authenticated declaration fields were not located. These are therefore not guessed.

The older linked author guide also states that submission carries originality / not-under-consideration / institution-approval representations. Because these are factual/legal representations, they are deliberately left for author confirmation.

Full details are in `submission/JOURNAL_REQUIREMENTS_LEDGER.md`.

## Citation / source QA

- Every citation in the manuscript resolves.
- The sole manuscript reference is the target Ringbom–Shy article and is verified against the publisher record/VOR.
- No unverified literature citation was inserted merely to strengthen positioning.
- The VOR itself is not redistributed.
- VOR byte-level SHA-256 remains explicitly UNRESOLVED; a fresh direct byte download attempt failed, so no digest is fabricated. This is provenance incompleteness, not ambiguity about the source article or printed equation, and is not treated as a submission blocker.

## Submission-facing QA

Ready:
- manuscript source;
- clean anonymous initial-submission PDF;
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
- identity, email, affiliation, ORCID if requested;
- funding and competing-interest facts;
- acknowledgments;
- preprint / prior-publication / simultaneous-submission facts;
- institution-approval/originality representations;
- exact current AI/declaration prompt wording;
- authenticated field limits and system-generated preview.

## Why this is not a full PASS

The canonical workflow requires full PASS to fail closed on material `UNVERIFIED` items. The public journal requirements are sufficiently verified, but the authenticated portal is JavaScript/session dependent and the workflow is not authorized to invent or accept author declarations. Therefore the only defensible stop state is:

**Stage 14 — CONDITIONAL PASS — AUTHENTICATED PORTAL PREFLIGHT REQUIRED.**

This is the requested stopping boundary. No Stage-15 freeze/tag and no submission action are performed.

## Next-stage contract

There is no authorized Stage-15 contract. The next human action is to perform the reversible authenticated portal preflight described in `submission/AUTHENTICATED_PORTAL_PREFLIGHT.md`, confirm the factual/legal author fields, and stop before final submission.

# Stage 13 — Full-Paper Integration for Economics Bulletin

## Gate record

- Canonical workflow: research-paper-workflow v2.4, commit `63f11a50a13d9328213498a5a6576d00b9bceef7`.
- Input commit: `5d519f05ee05d09e923f48b43692668d9bbef502` (Stage 12 primary-journal decision).
- Output/closure commit: `3b5f42f39fc268c7c0a73197f988083961462298` (Stage 13 integration report; substantive manuscript preflight had already passed at `fdb98047fc60fea82553095521b66c1c011c4a27`).
- Primary journal / route: *Economics Bulletin* / **Comment**, subject to authenticated portal confirmation.
- Branch: `research/stage-00-evidence-freeze`.
- **Verdict: PASS TO STAGE 14.**
- No theorem, quantifier, tie convention, novelty boundary, or welfare conclusion changed.

## Journal-specific integration

The current public *Economics Bulletin* submission instructions were re-read on 2026-09-23. The manuscript was altered only in presentation:

1. Base manuscript size changed to 12pt.
2. One-inch margins and single-spacing architecture preserved.
3. Numbered Arabic section structure preserved.
4. Section/subsection headings use centered bold 14pt, following the current live initial-submission page.
5. The visible title page, author line, abstract, keywords, and JEL lines were removed from the uploaded manuscript PDF. The public instructions state that the submission metadata generates the title page and that the submitted PDF should begin with Section 1.
6. The artificial page break before the two-type model was removed.
7. Title, abstract, keywords, and JEL are preserved in `submission/SUBMISSION_METADATA.md` for portal entry.
8. The manuscript remains anonymous at the PDF metadata level (`Author: Anonymous`).

The live author-facing page states 14pt centered bold section headings, while an older linked author-guidelines PDF describes 12pt headings. For initial submission the current live page is treated as the more specific/current instruction; the conflict is recorded for authenticated preflight rather than silently ignored.

## Submission-facing drafts

- `submission/SUBMISSION_METADATA.md`: title, abstract, keywords, JEL, and author-confirm fields.
- `submission/COVER_LETTER_DRAFT.md`: optional source-journal Comment cover letter.
- `submission/DECLARATIONS_DRAFT.md`: non-binding drafts for code availability, AI/tool-use disclosure, funding, interests, preprint/originality, and acknowledgments.

No author identity, affiliation, e-mail, funding, competing-interest status, preprint status, originality warranty, or legally binding declaration has been invented.

## Build and regression evidence

- Reproducibility/manuscript workflow run `35813984894` on commit `fdb98047fc60fea82553095521b66c1c011c4a27`: **SUCCESS**.
- Exact/symbolic checks: PASS.
- Manuscript build: PASS.
- PDF checks enforce:
  - 12pt source;
  - one-inch geometry;
  - 1–7 pages;
  - no visible title or Abstract heading on page 1;
  - numbered `1 Introduction` on page 1;
  - embedded fonts;
  - anonymous PDF author metadata.
- Built PDF after journal integration: **5 pages**, US-letter page size, all PDF checks passed.
- Stage-11 theory and formal-verification artifacts were unchanged, so the formal certificate is not stale.

## Stage-14 contract

Stage 14 must:
- recheck current public requirements and record any public/authenticated split;
- inspect the exact built PDF page by page;
- verify package inventory and manuscript/code/formal consistency;
- keep all factual/legal author declarations unconfirmed until the author reviews them;
- stop at conditional PASS if authenticated portal-only fields cannot be verified without an irreversible submission action.

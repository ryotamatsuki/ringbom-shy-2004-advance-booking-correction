# Stage 10 — Section-by-section paper construction

## Gate record

- Input commit: `b2af21b7bdede1ab9d92c0987042371fe4edf836` (Stage 9 reproduction gate closed).
- Output commit: to be recorded in `docs/STAGE_COMMIT_LEDGER.md`.
- Working title: **A Correction to the Two-Type Refund Result in Ringbom and Shy (2004)**.
- Paper type: short correction/comment, anonymous 5-page manuscript.
- **Verdict: PASS TO STAGE 11.**

## Manuscript map

1. Introduction: identifies Eq. (6)'s missing factor, exact consequence, global-choice qualification, and separate uniform/table survival result.
2. Two-type model: transcribes primitive utility, refund thresholds, unit seller profit, threshold payoff, and threshold ordering.
3. Correct endpoint comparison: states and proves the exact necessary-and-sufficient endpoint ranking and reports the strict rational regression point.
4. Global refund choice: gives the full weak-tie threshold candidate correspondence and proof from primitive utility and fixed-set monotonicity; corrects the reading of Corollary 1 and records the no-booking regression.
5. Uniform section: states the active domain, direct profit derivative, private-refund formula, two Table 1 corrections with exact gains, planner cutoff, welfare loss, and strict-domain qualification.
6. Conclusion and a verified reference to the publisher Version of Record.

## Consistency and reproducibility checks

- The endpoint theorem in the PDF matches `docs/THEOREM_CERTIFICATES_STAGE04.md` TC-01.
- The global-correspondence quantifiers and tie convention match the analytic case split in `derivations/two_type_global_correspondence.md` and TC-02. The paper does not describe the endpoint inequality as a global optimum condition.
- The Corollary 1 outside option matches TC-03 and `code/corollary_counterexample.py`.
- The uniform formulas and two numerical corrections match `derivations/uniform_rederivation.md`, TC-04/TC-06, and `code/uniform_table_audit_exact.py`.
- The only bibliography item is the VOR, verified in `sources/source_manifest.md`; no DOI is assigned because none was identified in the source/publisher record.
- `bash scripts/build_manuscript.sh` and `bash scripts/check_pdf.sh` pass. The PDF has 5 pages, anonymous author metadata, embedded fonts, and no unresolved references. Visual review of all pages found no layout defects.
- Current PDF SHA-256: `1fc055d8af448bd16799dcc331169c67dd2c2e304ae27faccbab54a5106bbab6` (updated after removing an unused TeX package dependency; the rendered five-page layout was rechecked).

## Submission-facing limits

The PDF is journal-neutral pending Stage 11 and Stage 12. No author, affiliation, corresponding-author identity, funding/competing-interest declaration, or acknowledgment is invented. The separate title page and journal-specific declarations will be completed only to the extent supported by confirmed author information and official requirements. No legal declaration or journal submission has been made.

## Next-stage contract

Stage 11 treats the current compiled paper as the attack target. Any mathematical defect requires reopening the earliest affected upstream stage. Journal positioning begins only after Stage 11 passes.

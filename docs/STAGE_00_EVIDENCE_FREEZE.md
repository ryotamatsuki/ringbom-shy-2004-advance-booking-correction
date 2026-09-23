# Stage 0 — Idea / Evidence Intake and Freeze

## Question

What is the correct profit-maximizing refund choice in the published two-type model, once the printed Proposition 1 comparison and the feasible refund domain are checked from primitives?

## Phenomenon, explanation, and mechanism

- Phenomenon: the 2004 article reports a closed-form high-refund versus low-refund screening condition.
- Candidate explanation for a discrepancy: the substitution from equation (5) to equation (6) may omit a denominator; feasibility of the threshold rates may also be suppressed.
- Modeled margin: a seller chooses one refund rate in `[0,1]`; types differ in exogenous show-up probability and reserve iff expected utility is weakly nonnegative.
- Welfare object: the continuum/uniform section is a separate model result and is not presumed to depend on the two-type comparison.

## Falsifiable research question

Does the VOR's equation (6) correctly compare the two feasible endpoint profits in the two-type model, and what is the complete global argmax correspondence under the stated refund strategy set and an explicit participation tie rule?

## Frozen evidence

- Production repository branch and starting head: `research/stage-00-evidence-freeze` at `b1c6f118ee4a76489ca10789a89e8b1e86be738f`.
- Stage 0 output commit: `f936faa5865da528a300213f2c5c086415c795d0` (`stage00: freeze workflow mapping and evidence intake`).
- Canonical workflow: v2.4 at `63f11a50a13d9328213498a5a6576d00b9bceef7`; scaffold crosswalk: `docs/WORKFLOW_V2_4_MAPPING.md`.
- Master audit and code were fetched from the user's named branch and read as provenance only; the working copy never assumes their theorem is true.
- Publisher VOR accessed 2026-09-23; 8 PDF pages; equation/proposition/table inventory recorded in `sources/source_manifest.md` and `derivations/source_transcription.md`.
- Exact counterexample parameters are retained as a regression target in `code/counterexample_exact.py`.

## Preliminary discrepancy signal (not yet a frozen theorem)

For the supplied rational point, the source's printed comparison is positive while the direct endpoint-profit difference is negative. Stage 1 must re-derive this in independent symbolic and primitive-payoff paths before the result can be used in a manuscript.

## Literature families assigned to Stage 2

Exact erratum/corrigendum/comment/reply searches; the 2003 Ringbom–Shy predecessor; the 2005/2008 refund-collusion papers; advance-purchase and sequential-screening models; partial-refund revenue management; exact correction-note precedent at *Economics Bulletin*; and all forward citations discoverable from RePEc/CitEc and author records.

## Decisions and limitations

- The initial candidate is a correction of a published proposition, not a claim that the whole paper is invalid.
- No full-paper expansion is authorized absent an independent economic reason.
- The binary SHA-256 of the VOR PDF remains unverified because only browser-extracted PDF text was accessible in the source retrieval surface. No PDF digest is invented; the source URI and access date are frozen.
- Author identity and affiliation remain unresolved; no name or institutional affiliation is inserted into a submission file.

## Verdict

**GO** to Stage 1 source and mathematical audit. The source and research question are specific and falsifiable; the exact counterexample and first-principles checks are the Stage 1 burden of proof. This GO is not a theorem certification.

## Next-stage contract

Stage 1 must reconstruct the two-type and uniform models from the publisher source; complete source-to-equation mapping; independently compute the exact regression point through four distinct evidence paths; and record domain/tie limitations. No corrected proposition may be frozen before those checks.

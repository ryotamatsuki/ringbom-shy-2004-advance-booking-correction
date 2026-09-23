# Stage 3 — Candidate paper architecture

## Input and verdict

- Input commit: `66f30a1b861b825ea5904611c4c9f19fdf63f058` (Stage 2 output).
- Stage 2 result: the exact correction was not located in the public literature search; the generic global-candidate argument will not be claimed as a new general theorem.
- **Architecture decision: choose B, correction plus complete two-type correspondence.** This is a provisional architecture, not a theory freeze.

## Compared architectures

| Architecture | Proposed content | Contribution / reviewer value | Assessment |
|---|---|---|---|
| A. Minimal correction note | Derive the missing factor in equation (6), give the exact rational counterexample, and stop | Smallest possible correction; directly documents the published algebraic error | Too narrow for the research question because it leaves endpoint feasibility, the zero-profit alternative, and equality branches unanswered |
| B. Correction plus complete two-type correspondence | Correct endpoint comparison; characterize the global argmax over `r∈[0,1]` including thresholds outside the strategy set, weak ties, no-booking plateaus, and `β≤p`; map the downstream impact and state what survives | Resolves the algebraic error and the economic choice correspondence in the source's own model; provides conditions needed to interpret Proposition 1 and Corollary 1 | **Selected.** Model-specific, complete, and no new mechanism is added |
| C. Correction plus economic extension | Add a new model with endogenous price, finite capacity, competition, or another refund institution | Could produce new economics only if motivated independently | Rejected. None is needed to establish the correction; it would change primitives and dilute the reassessment. No “publication rescue” extension is authorized |

## Selected paper scope

Working title: **A Correction to the Two-Type Refund Result in Ringbom and Shy (2004)**.

The core note will contain:

1. the VOR's two-type primitives and tie convention;
2. an exact derivation of the corrected endpoint comparison and the rational counterexample;
3. the complete global refund correspondence, including no-booking and equality branches;
4. a corrected reading of Corollary 1 that compares the both-type candidate with both the high-only candidate and the outside option;
5. an impact statement distinguishing the two-type error from the uniform-distribution welfare section.

The uniform model will not be expanded into a new contribution. The note will say that the separate uniform results survive on `β>p>c≥s≥0`, independently of equation (6); the full clean-room derivation and exact domain audit remain in the reproducibility supplement. Any stronger survival claim must be supported by the Stage 7 certificate.

## Novelty and theorem wording boundary

- Claim a correction to the VOR's published Proposition 1 / equation (6), not a general refund-screening theorem.
- Call the corrected inequality an endpoint comparison. It is globally decisive only after feasibility and the zero-profit no-booking option are evaluated.
- The finite-candidate/plateau correspondence is a complete result for this model's refund strategy, not an originality claim about all piecewise-linear screening problems.
- Describe the Corollary 1 implications as qualified; do not say the entire article is invalid.
- Preserve the prior-version uncertainty in the novelty ledger; do not assert absolute priority.

## Next-stage contract

Stage 4 must derive the selected architecture from primitive payoffs and state the parameter domain for each theorem. Stage 4A must independently attack the full correspondence, not merely the factor in equation (6). Stage 6 will retest novelty against the final theorem statements.

## Stage 3 scope re-review after Stage 4A table audit

Stage 4A identified two additional incorrect numeric entries in the source's uniform Table 1. The architecture decision is **reaffirmed as B**, with a short, self-contained note correcting those two cells in the source-survival discussion. This finding arose from the required independent verification of the original table; it does not add a new mechanism or general theory. The manuscript remains a model-specific correction plus complete two-type correspondence. It will report that the uniform formulas and welfare conclusions survive on the audited domain, while identifying the two erroneous Table 1 entries and confirming Table 2. Architecture C remains rejected.


# Stage 8 — Canonical theory freeze

## Freeze record

- Canonical workflow: v2.4, `research-paper-workflow` commit `63f11a50a13d9328213498a5a6576d00b9bceef7`, rechecked 2026-09-23.
- Input commit: `a1e61d3721f339da71fcce6f8e08b43d1b5e6b5e` (Stage 7.5A).
- Branch: `research/stage-00-evidence-freeze`.
- Theory freeze: this commit is the immutable research baseline for downstream writing. No tag is necessary; all later manuscript work must preserve the theorem set and scope below.
- **Verdict: PASS — THEORY FROZEN.**

## Frozen theorem set

1. Under the published two-type primitives and feasible endpoint rates, the exact endpoint-profit difference contains the term `α_H(σ_H−σ_L)(β−p)/(1−σ_L)`. The printed Eq. (6) omits `1/(1−σ_L)`.
2. The source's exact rational parameter point has feasible thresholds `5/27` and `25/39`. Under the paper's weak participation convention, the printed rule selects the both-type endpoint, while primitive profits are `53/125` at the high-type-only endpoint and `509/1300` at the both-type endpoint; the gap is `−211/6500`.
3. The complete global correspondence is the finite threshold candidate set plus the initial no-reservation plateau where it ties at zero, under the stated parameter domain, strategy set `[0,1]`, nonnegative normalized type masses, and weak participation. Negative, zero, unit, merged, absent-type, and no-booking branches are included in the analytic proof.
4. The source's Corollary 1 requires correction: endpoint comparison alone is insufficient; feasibility and comparison with the zero-profit outside option are required. The exact high-price example disproves the unqualified both-types-served reading.
5. The uniform results in Eqs. (7)–(19) and Propositions 2–4 survive on `β>p>c≥s≥0`, with their stated boundary qualification. Two private-refund entries in Table 1 are numerically incorrect: `0.250` is `8/13`, and `0.357` is `2/3`. All remaining checked Table 1 and Table 2 values reproduce at displayed precision.

## Scope and claim boundary

- Paper type: short correction/comment, not an expanded full theory paper.
- Working title: **A Correction to the Two-Type Refund Result in Ringbom and Shy (2004)**.
- Tie convention: consumers reserve when indifferent (`EU_i≥0`), consistent with the source's weak acceptance condition. Boundary attainment is not claimed to be invariant to alternative tie-breaking.
- No novelty claim is made for generic candidate enumeration, no absolute priority claim is made, and no result is generalized beyond the source's model.
- No claim that the complete original article is invalid; the uniform welfare results are distinct from the two-type error.

## Gates carried into the freeze

- Stage 4A: PASS; independent exact-rational primitive-payoff enumerator plus analytic proof. Formalization has bounded scope.
- Stage 6: PASS with qualification; bounded novelty search found no public correction or equivalent theorem, but predecessor version lineage remains unresolved and no “first ever” claim is made.
- Stage 7: PASS with domain qualifications; impact map records each result as corrected, surviving, or unaffected.
- Stage 7.5: short correction selected.
- Stage 7.5A: PASS — MODEL-SPECIFIC; rate/cash normalization and arbitrary-mass portability checks pass; tie convention is explicit.
- Formal verification: PASS for the formalized theorem subset; full correspondence and uniform welfare calculus remain analytic and independently checked.

## Source and reproducibility anchors

- VOR manifest and equation/page transcription: `sources/source_manifest.md`, `derivations/source_transcription.md`.
- Clean-room derivation: `derivations/two_type_global_correspondence.md`, `derivations/uniform_rederivation.md`.
- Headline exact checks: `code/counterexample_exact.py`, `code/independent_correspondence.py`, `code/uniform_table_audit_exact.py`, `code/portability_audit_exact.py`.
- Formal certificate: `formal/FORMAL_VERIFICATION_CERTIFICATE.md`.
- The source PDF is not redistributed; provenance identifies the publisher PDF URL, access date, and digest.

## Stage 8 output contract

All later work may improve exposition, reproduction, and submission formatting. A change to a theorem, domain, tie convention, novelty boundary, or economic interpretation invalidates this freeze and requires rollback to the earliest affected stage. Stage 15, submission, and main-branch merge remain prohibited.

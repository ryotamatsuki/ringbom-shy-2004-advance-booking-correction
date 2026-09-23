# Formal Verification Certificate — Stage 4A

## Verdict

**PASS within the formalized scope.** GitHub Actions run [35807953310](https://github.com/ryotamatsuki/ringbom-shy-2004-advance-booking-correction/actions/runs/35807953310) completed successfully on commit `7a02dc974be8ca1716d97af4184d34f144c185f8` of `research/stage-00-evidence-freeze`.

## Reproduction environment

- Lean: `leanprover/lean4:v4.34.0` (pinned in `formal/lean-toolchain`).
- mathlib: v4.34.0, locked in `formal/lake-manifest.json` at `5ed2965256430c3649e86755f9576b54eca72435`.
- Build target: `RingbomShy`, explicitly selected in `formal/lakefile.lean` and CI.
- CI result: `RingbomShy.Refund`, `RingbomShy.AxiomAudit`, and the `RingbomShy` library built successfully; the source placeholder check passed; the axiom script rebuilt the library and checked `#print axioms` output.

## Theorems checked

- `endpoint_gap_identity`
- `endpoint_weak_choice_iff`
- `endpoint_equality_iff`
- `printed_gap_factor_omission`
- `feasible_endpoint_weak_choice_iff`
- `corrected_gap_exact_regression`
- `exact_regression_feasible`
- `weighted_unit_profit_nonincreasing`
- `fixed_set_profit_nonincreasing`

The axiom audit reports only Lean's standard foundations `propext`, `Classical.choice`, and `Quot.sound` for each theorem. It found no `sorryAx`, `admitAx`, project-declared axioms, or missing theorem reports.

## Scope limit

Lean certifies the listed rational identities, endpoint comparison/equality, exact counterexample, threshold feasibility, and fixed-set monotonicity. It does not encode the entire parameterized piecewise argmax correspondence, its initial no-booking plateau/tie branches, or the uniform-distribution welfare calculus. Those remain in the human-readable derivations and have separate exact-rational adversarial checks. This certificate must not be cited as formal verification of those unformalized results.

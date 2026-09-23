# Formal Verification Certificate — Stage 4A

## Verdict

**PASS within the formalized scope.** GitHub Actions workflow run #9, [run 35809641499](https://github.com/ryotamatsuki/ringbom-shy-2004-advance-booking-correction/actions/runs/35809641499), completed successfully on commit `6562740410460f48418baabff5b44912346db35e` of `research/stage-00-evidence-freeze`.

## Reproduction environment

- Lean: `leanprover/lean4:v4.34.0` (pinned in `formal/lean-toolchain`).
- mathlib: v4.34.0, locked in `formal/lake-manifest.json` at `5ed2965256430c3649e86755f9576b54eca72435`.
- Build target: `RingbomShy`, explicitly selected in `formal/lakefile.lean` and CI.
- CI result: `RingbomShy.Refund`, `RingbomShy.AxiomAudit`, and the `RingbomShy` library built successfully (8,927 jobs); the source placeholder check passed; the axiom script rebuilt the library and checked `#print axioms` output for all eleven theorems.

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
- `uniform_table1_cost_salvage_tenth_exact`
- `uniform_table1_zero_cost_salvage_exact`

The axiom audit reports only Lean's standard foundations `propext`, `Classical.choice`, and `Quot.sound` for each theorem. It found no `sorryAx`, `admitAx`, project-declared axioms, or missing theorem reports.

## Scope limit

Lean certifies the listed rational identities, endpoint comparison/equality, exact counterexample, threshold feasibility, fixed-set monotonicity, and two exact Table 1 FOC roots, derivative-bracket values, and primitive-profit gaps. It does not encode the entire parameterized piecewise argmax correspondence, its initial no-booking plateau/tie branches, uniqueness/globality of the uniform private optimum, or the general uniform-distribution welfare calculus. Those remain in the human-readable derivations and have separate exact-rational adversarial checks. This certificate must not be cited as formal verification of those unformalized results.

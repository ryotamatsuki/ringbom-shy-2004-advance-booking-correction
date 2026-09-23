# Stage 7.5A — Scope, quantifier, and portability certificate

## Input and decision

- Input commit: `15dce0c768a9cd59776f5e47f487a7a9e370e152` (Stage 7.5 architecture decision).
- Frozen contribution: model-specific correction of the published two-type result, with full feasibility and outside-option correspondence under the source-consistent weak-participation convention.
- **Verdict: PASS — MODEL-SPECIFIC.** No claim of portability to general screening models is made.

## Quantifiers and scope

The endpoint identity is algebraic for positive `p`, `σ_H,σ_L<1` and arbitrary real type masses. Its economic interpretation as a two-type market result uses nonnegative masses and the source's two-type payoff primitives. The global correspondence uses `β,p>0`, `c,s≥0`, `r∈[0,1]`, `α_i≥0`, `α_H+α_L=1`, `0≤σ_L<σ_H<1`, and weak participation `EU_i≥0`; source-domain claims additionally impose `β>p>c≥s≥0` and `0<σ_L<σ_H<1`.

The paper will distinguish the endpoint-comparison theorem from global maximization: the corrected inequality is necessary and sufficient only for comparing the two feasible endpoint offers. Global choice also compares feasible thresholds, the zero-profit no-booking region, and any boundary candidate.

## Pre-specified portability checks

### 1. Refund rate versus cash refund

Write `x=rp`, so `x∈[0,p]`. Then `x_i=(p−βσ_i)/(1−σ_i)` and `g_i(x)=p−c−(1−σ_i)(x−s)`. The high-type cost of extending the refund from `x_H` to `x_L` is

`(1−σ_H)(x_L−x_H)=(σ_H−σ_L)(β−p)/(1−σ_L)`.

Thus the factor `1/(1−σ_L)` and the endpoint gap are invariant under the cash-refund normalization. `code/portability_audit_exact.py` verifies the primitive rate and cash calculations by exact rational arithmetic at the source regression and at a second feasible point with non-normalized type masses.

### 2. Arbitrary type masses

The identity is linear in `α_H` and `α_L`; it does not require masses to sum to one. Rescaling both masses scales both endpoint profits and the gap by the same positive factor, leaving the ranking unchanged. The exact checker includes a pair of positive masses summing to `11/2` and confirms the same omitted-factor term. Probability normalization is used only for per-capita reporting and for interpreting `α_i` as population shares.

### 3. Equality and tie convention

The source's uniform cutoff uses weak acceptance (`σ≥σ̂`) and its expected-utility condition admits reservation at equality. This certificate therefore uses `EU_i≥0`. This choice matters at `r_i=0`, `r_i=1`, coincident thresholds, and `β=p`: strict rejection can change the attained candidate payoff and may remove an endpoint from the argmax. An exact boundary check at `β=p,r=1` gives weak-acceptance profit `9/5` and strict-rejection profit zero for masses `(2,3)`, show probabilities `(3/5,1/5)`, and `p=1,c=s=0`.

The headline regression has `0<r_H<r_L<1` and a strict reversal in the two endpoint ranking under the source's weak convention. Its algebraic gap is independent of tie-breaking, but whether the low-type endpoint is attained at the indifference rate is convention-sensitive. The manuscript will state the convention and will not claim tie-invariant attainment.

## Contribution Robustness Certificate

| Claim | Robustness assessment |
|---|---|
| Printed Eq. (6) omits `1/(1−σ_L)` | Invariant under rate-to-cash normalization and arbitrary positive type masses. |
| Exact feasible-endpoint ranking reversal | Strict under the source-consistent weak convention; both thresholds lie strictly inside `[0,1]`. No type-mass renormalization removes it. |
| Complete global refund correspondence | Valid for the stated strategy set and weak tie rule; boundary branches are explicitly convention-dependent. |
| Corollary 1 qualification | Applies only to the source model and requires feasibility plus comparison with the zero-profit outside option. |
| Uniform welfare preservation | Separate from the two-type algebraic error; held on `β>p>c≥s≥0`. The two corrected Table 1 entries are numeric source corrections, not a new welfare theorem. |

No post-hoc parameter restriction, representation switch, or new mechanism is used to obtain the result. The contribution survives as a published-proposition correction; the manuscript will not generalize beyond the identified model.

## Formal verification gate

**FORMAL VERIFICATION PASS, with explicit scope limits.** Lean 4/mathlib checks the endpoint identity, missing-factor comparison, equality, exact two-type regression, feasible-endpoint condition, fixed-participation slope lemma, and two Table 1 private-rate discrepancies. The full case-split argmax correspondence and uniform welfare calculus remain analytic results with a separately written exact-rational primitive-payoff checker. No Lean result is presented as certification of those omitted proof obligations.

Fresh pinned CI on commit `6562740410460f48418baabff5b44912346db35e` completed successfully (8,927 Lean build jobs; axiom audit and source placeholder scan passed). The only reported Lean infrastructure axioms are `[propext, Classical.choice, Quot.sound]`.

## Gate status and Stage 8 contract

- Portability: closed as `MODEL-SPECIFIC`.
- Quantifiers and tie convention: explicit.
- Contribution robustness: pass within the published model.
- Formal verification: closed with bounded claims and recorded limits.
- New unresolved material claims: none identified.

Stage 8 may freeze this theory on the research branch. This certificate does not authorize a merge to `main`, a journal submission, or Stage 15.

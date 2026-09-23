# Theorem certificates — Stage 4 candidate set

Certificates below state the exact quantifiers and separate analytic proof from computational cross-checking. The Lean project, once its CI build passes, certifies the endpoint identity, printed-factor difference, feasible endpoint comparison, equality condition, feasibility and exact values of the regression point, and fixed-participation slope lemma; it does not replace the paper's full case-split proof.

## TC-01 — Primitive payoff and endpoint identity

- **Quantifiers:** `β,p,c,s,α_H,α_L,σ_H,σ_L∈ℚ`; `p>0`, `σ_H,σ_L<1`. No sign assumption on costs, salvage, masses, or `β−p` is needed for the algebraic identity. The economic interpretation adds `α_i≥0`, `α_H+α_L=1`, and `r_i∈[0,1]`.
- **Definitions:** `r_i=(p−βσ_i)/(p(1−σ_i))`; `g_i(r)=p−c−(1−σ_i)(rp−s)`.
- **Claim:** `[α_H g_H(r_L)+α_L g_L(r_L)]−α_Hg_H(r_H)=α_L[σ_L(β−s)−c+s]−α_H(σ_H−σ_L)(β−p)/(1−σ_L)`.
- **Proof:** Substitute the two thresholds into the state-contingent payoff. At a type's own threshold, `g_i(r_i)=σ_i(β−s)+s−c`; the high type's loss from moving from `r_H` to `r_L` is `(1−σ_H)p(r_L−r_H)=(σ_H−σ_L)(β−p)/(1−σ_L)`. Collect terms.
- **Equality/necessary-sufficient:** On a feasible endpoint pair, the sign of the displayed difference is necessary and sufficient for `r_L` to weakly beat `r_H`; equality iff profits tie.
- **Cross-check:** `code/symbolic_derivation.py`, `code/counterexample_exact.py`, `code/independent_correspondence.py`, and Lean `endpoint_gap_identity`, `printed_gap_factor_omission`, `feasible_endpoint_weak_choice_iff`, and `endpoint_equality_iff`.

## TC-02 — Global refund correspondence

- **Quantifiers:** `β,p>0`; `c,s≥0`; `r∈[0,1]`; `α_i≥0`, sum one; `0≤σ_L<σ_H<1`; weak participation `EU_i≥0`.
- **Claim:** The maximizing set is the piecewise set in T2 of `docs/STAGE_04_CONSTRUCTION.md`.
- **Proof:** `EU_i(r)` is affine increasing in `r`, with threshold `r_i`. It determines a finite partition into fixed-participation intervals. On each nonempty interval, profit has slope `−np∑α_i(1−σ_i)<0`; the no-participation interval is flat at zero. Therefore a global maximum is attained at the lower endpoint of every nonempty interval, at `r=0`, or on the initial flat interval. Evaluate each boundary using weak ties. For `β≤p`, direct utility gives the separate cases rather than extrapolating the threshold formula.
- **Clipping/equality:** `r_i<0`, `r_i=0`, `r_i=1`, merged type thresholds, zero masses, participation ties, `β=p`, `β<p`, and no-booking are treated explicitly in `derivations/two_type_global_correspondence.md` and the exact checker.
- **Cross-check:** 800 seeded exact-rational admissible draws plus 21 directed exact edge regressions, with a separate exact grid falsification comparison. Grid agreement is diagnostic only; the slope/partition proof supplies globality.
- **Formal status:** The fixed-set monotonicity lemma is a Lean target. The full correspondence proof remains analytic and is not represented as Lean-certified unless a future certificate explicitly adds it.

## TC-03 — Corollary 1 and exact outside-option regression

- **Quantifiers:** For the counterexample, all parameters are rational and satisfy the source's intended `β>p>c≥s≥0` domain; both thresholds are strictly feasible.
- **Claim:** With `β=1`, `p=999/1000`, `c=9/10`, `s=0`, masses `(1/2,1/2)`, and show probabilities `(1/2,1/10)`, thresholds are `998/999` and `8990/8991`. High-only and both-type endpoint profits are `−1/5` and `−2701/4500`; the no-booking payoff is zero.
- **Conclusion:** The two-type participation conclusion in Corollary 1 cannot be unconditional in high price; both feasible screening candidates are loss-making in a neighborhood below `p=β` for this fixed parameter set.
- **Cross-check:** Independent raw-utility evaluator `code/corollary_counterexample.py`, plus the 21-case exact enumerator.

## TC-04 — Uniform private optimum and welfare preservation

- **Quantifiers:** `β>p>c≥s≥0`, `p>0`, uniform show-up distribution, weak participation. Boundary cases are classified by direct utility.
- **Claim:** The private-profit derivative factors into a positive denominator times a strictly decreasing bracket. The unique constrained optimum is `r̄=max{0,r_int}`. The planner chooses cutoff `(c−s)/(β−s)` and refund `r*`; `r*>r̄` and the welfare loss has the two formulas recorded in `derivations/uniform_rederivation.md`.
- **Proof:** Differentiate the primitive integral; the bracket decreases strictly because `σ̂(r)` decreases. This establishes global uniqueness of the private maximizer. Transfers cancel in welfare, making welfare a strictly concave quadratic in the cutoff. The private cutoff exceeds the social cutoff on the stated strict domain.
- **Strict boundary:** `p=c,s=0` is excluded: at `β=1,p=c=4/5,s=0`, exact formulas give `r*=r̄=0`. `code/uniform_boundary_audit.py` records this scope regression.
- **Cross-check:** `code/symbolic_derivation.py` proves symbolic identities/sign factors; exact boundary utility is separately checked in `code/uniform_boundary_audit.py`.

## TC-05 — Source equation (4) interpretation

- **Claim:** The actual seller payoff depends on the current refund `r`; the printed equation (4) substitutes candidate boundary rates in the upper and middle branches. On each fixed nonempty participating set, seller profit falls strictly with `r`.
- **Proof:** Differentiate primitive expected seller cash flow, giving `−np∑α_i(1−σ_i)`.
- **Implication:** Candidate boundaries are enough only together with feasibility, tie, and no-booking treatment. Equation (4)'s displayed values do not describe the actual payoff at every interior refund in the stated region.

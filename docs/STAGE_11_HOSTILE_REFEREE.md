# Stage 11 — Robustness / hostile-referee attack

## Gate record

- Canonical workflow: research-paper-workflow v2.4, commit `63f11a50a13d9328213498a5a6576d00b9bceef7`, rechecked 2026-09-23.
- Input manuscript commit: `ccc47397aea1c1237819c7d57d035e671c36ffd6`.
- Independent Stage-11 checker commit: `e4b9e38a27b8a7c81fcf6e016495acca720d495b`.
- Branch: `research/stage-00-evidence-freeze`.
- **Verdict: PASS TO STAGE 12.**
- No Stage-4A or Stage-7.5A certification regression was found.
- No theorem, domain, tie convention, or contribution-scope change is required.

## Independent reconstruction

The referee attack did not reuse the Stage-4 symbolic path or import the Stage-4A correspondence checker. The new script `code/stage11_hostile_referee.py` reconstructs consumer utility and state-contingent seller cash flows directly from primitives.

The publisher VOR was re-opened on 2026-09-23. Page 3 visibly prints Eq. (5), Proposition 1, and Eq. (6); Eq. (6) lacks the factor `1/(1-sigma_L)`. The VOR also prints Eq. (4) with `r_2` and `r_1` substituted inside the displayed regional branches, confirming that, as printed, those rows are endpoint values rather than the profit function at an arbitrary interior `r`.

Fresh symbolic reconstruction gives exactly

`(Pi_HL-Pi_H)/n = alpha_L[sigma_L(beta-s)-c+s] - alpha_H(sigma_H-sigma_L)(beta-p)/(1-sigma_L)`.

At the frozen rational regression point, direct primitive cash-flow evaluation reproduces

- `r_H=5/27`,
- `r_L=25/39`,
- `Pi_H/n=53/125`,
- `Pi_HL/n=509/1300`,
- `(Pi_HL-Pi_H)/n=-211/6500`,
- printed Eq.-(6) margin `=1/500>0`.

Thus the printed rule and the actual endpoint ranking disagree strictly inside the source domain.

## Referee attacks

### 1. "This is only a typographical slip"

**Severity:** MAJOR BUT FIXABLE as a publication-positioning objection, not a mathematical defect.

**Evidence:** The missing factor reverses the endpoint choice at a feasible interior parameter point. It therefore changes Proposition 1 as a decision rule rather than merely changing notation. The manuscript also separates the independent Eq.-(4) presentation issue, the global outside-option qualification, and two Table-1 numerical discrepancies.

**Response:** Keep the paper framed as a short correction/comment. Do not inflate the contribution into a new general screening theorem.

**Resolved:** YES.

### 2. Eq. (5) may not imply the corrected factor

**Severity:** FATAL if true.

**Evidence:** Independent symbolic algebra and primitive cash-flow reconstruction agree on the factor `1/(1-sigma_L)`; the exact counterexample reproduces the corrected gap.

**Resolved:** YES.

### 3. The counterexample may violate the published domain or threshold feasibility

**Severity:** FATAL if true.

**Evidence:** `beta=1>p=3/5>c=1/50>=s=0`, `0<sigma_L=7/20<sigma_H=11/20<1`, positive masses sum to one, and `0<5/27<25/39<1`.

**Resolved:** YES.

### 4. Endpoint ranking may be mistaken for global optimality

**Severity:** FATAL if the manuscript made that claim.

**Evidence:** The manuscript explicitly distinguishes Proposition "Corrected endpoint comparison" from the separate global correspondence. It includes `r=0`, feasible participation thresholds, and the initial zero-profit no-booking plateau when tied.

**Resolved:** YES.

### 5. Boundary, clipping, and tie branches may be missing

**Severity:** FATAL if true.

**Evidence:** The theorem covers negative, zero, interior, unit, and above-one raw thresholds, zero type masses, `beta<p`, `beta=p`, `sigma=0`, merged thresholds, and weak participation. The Stage-11 checker includes directed boundary regressions and 5,000 seeded exact-rational draws. A 1/200 exact grid is used only as a falsification cross-check; analytic monotonicity on fixed-participation regions remains the global proof.

**Resolved:** YES.

### 6. The first corollary may still follow despite Eq. (6)

**Severity:** MAJOR BUT FIXABLE.

**Evidence:** The source's qualitative statement about sufficiently high `p` is not a complete global statement when the seller can obtain zero by inducing no reservation. The frozen exact high-price example has both endpoint profits below zero while no booking yields zero.

**Response:** The manuscript does not claim every comparative-static phrase in Corollary 1 is reversed. It states that the global reading requires feasibility, the corrected endpoint comparison, and comparison with the no-booking option.

**Resolved:** YES.

### 7. The complete correspondence is a known theorem in disguise

**Severity:** MAJOR BUT FIXABLE as a novelty objection.

**Evidence:** The finite-candidate argument is standard one-dimensional piecewise-affine optimization. Stage 6 already disclaims novelty for candidate enumeration. The publication contribution is correction of the published proposition and source-specific completion, not a new general optimization theorem.

**Certification regression:** NO.

**Resolved:** YES.

### 8. Broader screening/refund theory may absorb the correction

**Severity:** FATAL to a theorem-novelty claim, but the manuscript makes no such claim.

**Evidence:** Stage-6 comparisons with sequential screening, refund menus, airline revenue management, competitive refund policy, and signaling use materially different timing/choice objects. None inspected source supplies the VOR's disputed algebraic comparison. The manuscript cites no priority claim beyond the correction itself.

**Resolved:** YES WITH PRIOR-DISCLOSURE QUALIFICATION.

### 9. Arbitrary type-mass portability may be an unnecessary generalization

**Severity:** MINOR.

**Evidence:** Positive rescaling of masses leaves argmax unchanged, and the Stage-7.5A portability check verified the representation. The source-normalized case remains nested.

**Response:** No claim of economic generality is attached to this normalization observation.

**Resolved:** YES.

### 10. Uniform optimum may rely only on a local FOC

**Severity:** FATAL if true.

**Evidence:** The direct derivative factorization writes the profit derivative as a positive factor times `g_{hat sigma}(r)-(beta-p)/2`; the bracket is strictly decreasing on `beta>p>c>=s>=0`, so it crosses at most once. The upper endpoint is not an omitted optimum. Algebra also gives `1-r_int = [(beta-p)(beta-p+2(c-s))]/[p(beta-2c+p)]>0` whenever the interior root is positive, so no unreported `min{1,...}` clipping is needed on the active domain.

**Resolved:** YES.

### 11. The two Table-1 corrections may be numerical artifacts

**Severity:** MAJOR BUT FIXABLE.

**Evidence:** They are exact rational roots of the source's own uniform FOC: `8/13` and `2/3`. Direct primitive profits improve strictly over the printed values, and the Stage-4A Lean subset proves the exact roots/bracket values and profit gaps. The manuscript does not claim the full uniform welfare analysis is formally verified.

**Resolved:** YES.

### 12. Welfare may be mechanically or inconsistently accounted

**Severity:** FATAL if true.

**Evidence:** Adding consumer utility to seller profit cancels the refund/payment transfers and leaves `(beta-s)sigma-(c-s)` inside the participation integral. The planner's choice remains the refund-induced participation cutoff, so the paper uses "socially optimal refund" rather than an unrestricted first-best allocation claim.

**Resolved:** YES.

### 13. Formal-verification scope may be overstated

**Severity:** MAJOR BUT FIXABLE if true.

**Evidence:** The manuscript itself makes no Lean-coverage claim. The repository certificate explicitly limits Lean to endpoint algebra/equality, exact regression/feasibility, fixed-set monotonicity, and the two Table-1 exact checks. The full argmax correspondence and general uniform welfare calculus remain analytic plus independent exact checks.

**Resolved:** YES.

### 14. Manuscript exposition may exceed the frozen theorem quantifiers

**Severity:** FATAL if true.

**Evidence:** The endpoint proposition is conditioned on feasible ordered thresholds; the global theorem states its complete primitive domain and weak tie rule; the uniform section states `beta>p>c>=s>=0` and flags excluded denominator/tie boundaries. No generic-screening or whole-paper-invalidity language appears.

**Certification regression:** NO.

**Resolved:** YES.

### 15. The note may be too small for a journal

**Severity:** JOURNAL-POSITIONING ISSUE, not a theory defect.

**Evidence:** The surviving package is a five-page correction with a strict reversal counterexample, complete model-specific correspondence, corrected corollary interpretation, survival map, and two additional table corrections. Stage 12 must evaluate journal/article-type fit without expanding the theory merely to target a higher-ranked venue.

**Resolved for Stage 11:** YES; route to Stage 12.

## Independent falsification evidence

`code/stage11_hostile_referee.py` performs:

- exact primitive-payoff reproduction of the headline counterexample;
- directed tests at `beta<p`, `beta=p`, `sigma_L=0`, `r_H=0`, `r_L=0`, no-booking dominance, and the endpoint equality surface;
- 5,000 seeded exact-rational parameter draws across all three `beta`/price orderings, zero/positive masses, zero/interior show probabilities, and arbitrary nonnegative `c,s`;
- an independent exact grid falsification check at each draw.

No grid point exceeded the frozen theorem's candidate maximum. This is supporting falsification evidence, not the analytic proof of globality.

## Stage-11 gate conclusion

- Unresolved FATAL attacks: **none**.
- Unresolved MAJOR BUT FIXABLE theory attacks: **none**.
- Certification regressions: **none**.
- Theory rollback required: **no**.
- Formal certificate stale: **no**.
- **Canonical verdict: GO — PASS TO STAGE 12.**

## Next-stage contract

Stage 12 must construct a broad correction/comment candidate universe from current official journal evidence and recent comparable article types. Economics Bulletin must be considered explicitly as the source journal, but it must not be selected automatically. The Stage-7.5A classification remains MODEL-SPECIFIC and must not be enlarged to fit a preferred venue.

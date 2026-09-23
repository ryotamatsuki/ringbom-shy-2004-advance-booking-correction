# Stage 4A — Independent mathematical adversarial certification

## Input and provisional verdict

- Input commit: `16ca2f760816df98b414db51d5bbd694c1b7ec37` (Stage 4 analytic construction).
- The independently written exact-rational evaluator and directed attacks pass. The formal project is prepared and its fresh GitHub Actions build is pending.
- **Provisional verdict: ANALYTIC / EXACT-CHECK PASS; FORMAL GATE PENDING.** Stage 4A is not closed until the pinned Lean build, placeholder scan, and theorem axiom audit pass on the research branch.

## Independence and evidence paths

The counterexample was checked through separate representations:

1. `derivations/source_transcription.md` transcribes the VOR's Eq. (5)–(6) and participation convention from the publisher PDF, with equation-to-page map in `sources/source_manifest.md`.
2. `code/symbolic_derivation.py` derives the endpoint-profit difference and threshold ordering symbolically from the displayed threshold and unit-profit formulas.
3. `code/counterexample_exact.py` evaluates the source's primitive expected utility and state-contingent cash flow using Python `Fraction`.
4. `code/independent_correspondence.py` is separately written: it computes participation from raw utility at each endpoint and directly sums state-contingent payoffs. It imports neither of the other two-type programs.
5. The Lean target independently states the rational payoff definitions and proves the endpoint identity, printed-factor gap, feasible endpoint comparison, equality case, feasibility of the regression thresholds, and exact rational regression. CI has not yet certified this last path.

The source paper and historical audit were used as transcription/provenance targets. The mathematical identities were re-derived; the audit's conclusion was not treated as proof.

## Required regression result

For the source-domain point `(β,p,c,s,α_H,α_L,σ_H,σ_L)=(1,3/5,1/50,0,4/5,1/5,11/20,7/20)`, all exact implementations report

| Quantity | Exact value |
|---|---:|
| `r_H` | `5/27` |
| `r_L` | `25/39` |
| High-only primitive profit per unit mass | `53/125` |
| Both-types primitive profit per unit mass | `509/1300` |
| Difference, both minus high-only | `−211/6500` |
| Printed Eq. (6) left side minus right side | `1/500` |

Both rates satisfy `0 < r_H < r_L < 1`; weak participation makes the marginal type enter at its threshold. The printed condition strictly selects `r_L`, while primitive profit strictly favors `r_H`.

## Adversarial coverage

`python3 code/independent_correspondence.py` completed 800 seeded exact-rational admissible draws (`seed=20040923`) and 21 directed rational regressions. The finite grid is only a falsification diagnostic; the global result follows from the analytic fixed-participation slope/threshold-partition proof in `derivations/two_type_global_correspondence.md`.

| Attack | Exact treatment |
|---|---|
| Thresholds below zero / full participation from `r=0` | Directed case with both thresholds negative; raw weak participation evaluated at zero |
| Threshold exactly zero | `r_H=0` and `r_L=0` regressions; equality included at zero |
| Threshold exactly one | `σ_L=0, β>p`, so `r_L=1`; endpoint tie and both mass limits tested |
| Thresholds outside strategy domain | `β<p` classified from raw utility; positive-show types never enter, zero-show type can enter at `r=1` |
| Participation ties | Raw utility `EU_i≥0` at each endpoint; `β=p,r=1` and threshold endpoints covered |
| No participation / initial no-booking plateau | Exact zero-profit interval checked, including endpoint candidates with negative profit |
| Full participation | Both types strictly reserve at `r=0` in a directed case |
| `β=p`, `β<p`, and `β>p` | Separate primitive-utility branches; no quotient extrapolation |
| No-booking option dominates feasible thresholds | High-price exact rational counterexample in `code/corollary_counterexample.py` and directed enumerator case |
| Equality surface | Exact profits tie at both feasible thresholds; argmax is set-valued |
| Absent type / mass limits | `α_H=0`, `α_L=0`, and both positive masses covered |
| `σ_L→0`, `σ_H→1` | Exact near-boundary draws and `σ_L=0` endpoint regressions |
| `p→β`, `p→c`, `c→s`, `s=0` | Rational near-boundary draw plus `code/uniform_boundary_audit.py`; exact `p=c,s=0` regression retained |
| Uniform cutoff quotient singularities | Direct-utility checks for `β=p`, `β−rp=0`, and `p>β` in `code/uniform_boundary_audit.py` |

## Formal verification target and scope

Formalization is **applicable**: the central correction is exact algebra over rationals, with weak inequalities and an equality branch. The pinned Lean 4 / mathlib project targets:

- endpoint-profit identity and necessary-and-sufficient weak endpoint comparison;
- explicit identity for the missing `1/(1−σ_L)` factor;
- endpoint equality iff corrected gap is zero;
- feasibility ordering of the supplied exact counterexample;
- exact rational counterexample values and fixed-set profit monotonicity.

The full piecewise argmax proof and the separate uniform calculus/welfare derivation remain human-readable analytic proofs, cross-checked by an independent exact evaluator and symbolic algebra. No claim that Lean certifies those unformalized arguments is made. No custom axioms, `sorry`, or `admit` are allowed. The current verdict remains pending until the CI log confirms a fresh build and `#print axioms` audit.

## Tests run locally

- `python3 code/counterexample_exact.py` — PASS.
- `python3 code/symbolic_derivation.py` — PASS.
- `python3 code/independent_correspondence.py` — PASS (800 draws; 21 directed cases).
- `python3 code/corollary_counterexample.py` — PASS.
- `python3 code/uniform_boundary_audit.py` — PASS.
- `python3 formal/check_no_placeholders.py` — PASS (source scan only; not a Lean build).
- Local Lean/Lake executables are unavailable; no local formal build is claimed.

## Remaining gate and next-stage contract

- **Unresolved:** fresh CI Lean build and axiom audit.
- **Unresolved:** whether the formal theorem statements compile exactly as written; CI output must be inspected and any failure repaired.
- No mathematical discrepancy remains in the exact regression or current analytic correspondence.
- Stage 4A may close only after the formal gate passes and report records the CI run/commit. If proof compilation fails, repair the formal files without weakening statements or adding assumptions, then rerun CI. If the analytic correspondence is contradicted, reopen Stage 4.
- Stage 6 must re-run novelty kill against the final corrected endpoint theorem and exact global correspondence.

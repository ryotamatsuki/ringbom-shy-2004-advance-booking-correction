# Stage 4A — Independent mathematical adversarial certification

## Input and verdict

- Input commit: `16ca2f760816df98b414db51d5bbd694c1b7ec37` (Stage 4 analytic construction).
- Branch: `research/stage-00-evidence-freeze`.
- The independently written exact-rational evaluator and directed attacks pass. The pinned Lean target was actually built in GitHub Actions.
- **Verdict: PASS within the stated formalization scope.** The exact endpoint algebra, weak choice/equality equivalences, printed-factor identity, rational regression, feasibility arithmetic, and fixed-participation monotonicity compile without proof placeholders or nonstandard axioms. The complete piecewise correspondence and uniform-distribution calculus remain certified by the separate analytic derivation and independent exact checks, not by Lean.

## CI attempt log

- Run 1, commit `ab01adf8c7001f6219d20e301b56da9c7cb95670`, failed during `lean-action` setup because `formal/lake-manifest.json` was absent. The Lean build, placeholder scan, and axiom audit were skipped; this is a reproducibility setup failure, not evidence for or against any theorem. The failure is retained rather than relabeled.
- A lockfile is now being added with mathlib v4.34.0 and every transitive Git dependency pinned to the revisions in mathlib's own v4.34.0 manifest. A fresh CI run is required before closure.
- Run 2, commit `6004017e7316a717ea7cbeda89311fa852fe2e3e`, reached `lake exe cache get` but rejected the manifest's hyphenated root package name as not a Lean `Name`. No mathlib cache or theorem build ran. The root package and manifest name are being changed together to `ringbomShyCorrection` before the next fresh run.
- Run 3, commit `9afe19584b974c9f46d1a88d7c286a3ded82c32b`, failed because the repository placeholder scanner also inspected `.lake/packages` and found test/example placeholders in pinned dependencies. On log reinspection, the action's `lake build` also reported `No targets specified` / `Nothing to build`; it did not compile project Lean sources. The scanner has since been scoped to repository-owned sources.
- Run 4, commit `092c43e55a4c1fb6dd5ec16b0e3474da8afc2993`, passed the scoped source scan but again ran a no-op `lake build` because no default target was declared. The axiom step then failed because no `RingbomShy` oleans existed. This run provides no proof verification. The Lake project now declares `RingbomShy` as its default target, CI passes that target explicitly, and the axiom script builds it before reading the certificate; a fifth fresh run is required.
- Run 5, commit `baaa581533ae01c4e8e65eb9b3093ecb2f985c59`, reached the mathlib-cache step but failed because the scoped Lake dependency was named `mathlib4` while the pinned manifest and mathlib project identify the package as `mathlib`. The theorem target was not built, and placeholder/axiom checks were skipped. The dependency declaration is being changed to the official scoped package name `mathlib` before another fresh run.
- Run 6, commit `7a02dc974be8ca1716d97af4184d34f144c185f8`, succeeded: [GitHub Actions run 35807953310](https://github.com/ryotamatsuki/ringbom-shy-2004-advance-booking-correction/actions/runs/35807953310). Lean 4.34.0 built `RingbomShy.Refund`, `RingbomShy.AxiomAudit`, and the `RingbomShy` library (8,927 jobs); the source-only placeholder scan passed; and all nine theorem axiom reports contained only `propext`, `Classical.choice`, and `Quot.sound`. The mathlib cache omitted two project artifacts, which Lake compiled successfully during the build.

## Independence and evidence paths

The counterexample was checked through separate representations:

1. `derivations/source_transcription.md` transcribes the VOR's Eq. (5)–(6) and participation convention from the publisher PDF, with equation-to-page map in `sources/source_manifest.md`.
2. `code/symbolic_derivation.py` derives the endpoint-profit difference and threshold ordering symbolically from the displayed threshold and unit-profit formulas.
3. `code/counterexample_exact.py` evaluates the source's primitive expected utility and state-contingent cash flow using Python `Fraction`.
4. `code/independent_correspondence.py` is separately written: it computes participation from raw utility at each endpoint and directly sums state-contingent payoffs. It imports neither of the other two-type programs.
5. The Lean target independently states the rational payoff definitions and proves the endpoint identity, printed-factor gap, feasible endpoint comparison, equality case, feasibility of the regression thresholds, and exact rational regression. CI run `35807953310` compiled this path and audited its axioms.

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

## Formal verification certificate and scope

Formalization is **applicable**: the central correction is exact algebra over rationals, with weak inequalities and an equality branch. The pinned Lean 4 / mathlib project, certified by CI run `35807953310`, targets:

- endpoint-profit identity and necessary-and-sufficient weak endpoint comparison;
- explicit identity for the missing `1/(1−σ_L)` factor;
- endpoint equality iff corrected gap is zero;
- feasibility ordering of the supplied exact counterexample;
- exact rational counterexample values and fixed-set profit monotonicity.

The full piecewise argmax proof and the separate uniform calculus/welfare derivation remain human-readable analytic proofs, cross-checked by an independent exact evaluator and symbolic algebra. No claim that Lean certifies those unformalized arguments is made. The CI audit found no custom axioms, `sorry`, or `admit`; only Lean's standard logical foundations appear.

## Tests run locally

- `python3 code/counterexample_exact.py` — PASS.
- `python3 code/symbolic_derivation.py` — PASS.
- `python3 code/independent_correspondence.py` — PASS (800 draws; 21 directed cases).
- `python3 code/corollary_counterexample.py` — PASS.
- `python3 code/uniform_boundary_audit.py` — PASS.
- `python3 formal/check_no_placeholders.py` — PASS (source scan only; not a Lean build).
- Local Lean/Lake executables are unavailable; no local formal build is claimed.

## Stage 4A closure and next-stage contract

- **Closed:** pinned fresh CI build, source placeholder scan, and axiom audit passed on the research branch.
- No mathematical discrepancy remains in the exact regression or current analytic correspondence.
- Reopen Stage 4 if an independent attack contradicts the analytic correspondence; this CI pass certifies only the named Lean theorems.
- Stage 6 must re-run novelty kill against the final corrected endpoint theorem and exact global correspondence.

# Stage 1 evidence ledger

| Claim | Source / page | Independent evidence path | Status / limitation |
|---|---|---|---|
| Primitive type utility (1) and refund bounds | VOR PDF p. 2 | `source_transcription.md`; direct EU in `counterexample_exact.py` and `independent_correspondence.py` | PASS; equality convention explicitly set to weak participation |
| Thresholds (2)–(3), order | VOR PDF p. 2 | Algebraic derivation in `two_type_global_correspondence.md`; SymPy identity in `symbolic_derivation.py` | PASS on `β>p`; order reverses/collapses outside it |
| Candidate payoff comparison (5)–(6) | VOR PDF p. 3 | SymPy exact identity plus direct Fraction primitive payoff and independent enumerator | Printed RHS omits `1/(1−σ_L)`; exact active-domain counterexample reverses sign |
| Exact counterexample | VOR Eq. (6), p. 3 | (1) source transcription; (2) SymPy; (3) raw state-contingent Fraction evaluator; (4) separately written raw-utility candidate enumerator | PASS: `r_H=5/27`, `r_L=25/39`; `Π_H/n=53/125`, `Π_HL/n=509/1300`; printed sign `+1/500`, payoff difference `−211/6500` |
| Profit schedule (4) | VOR PDF p. 3 | State-contingent payoff formula and derivative on each fixed-participation region | The displayed lines are candidate endpoint profits; actual interior profit is r-dependent and strictly decreasing for any active mass |
| Complete two-type global correspondence | VOR Eqs. (1)–(4), pp. 2–3 | Piecewise primitive participation + strict slope argument; exact independent enumerator | PASS under weak tie acceptance; see exact case split and flat no-book region |
| Uniform profit / private refund | VOR Eqs. (7)–(16), printed pp. 3–5 | Fresh SymPy derivation and derivative-monotonicity proof | PASS on `β>p>c≥s≥0`; clipped point `p=p̃` is handled as a corner |
| Welfare identity / social refund / loss | VOR Eqs. (17)–(19), printed pp. 5–6 | Primitive transfer cancellation, cutoff maximization, SymPy identities; exact `p=c` boundary check | PASS on `β>p>c≥s≥0`; `r*>r̄` can become equality at excluded `p=c,s=0`; no dependency on Eq. (6) |
| Corollary 1 outside-option test | VOR Corollary 1, printed p. 3 | Exact raw-utility and state-contingent payoff evaluator in `code/corollary_counterexample.py` | PASS counterexample: at `p=999/1000`, both feasible screening endpoints are negative and no booking yields zero |
| Uniform boundary behavior | VOR Eqs. (8), (14)–(19) | Exact rational direct-utility/formula checker in `code/uniform_boundary_audit.py` | PASS: quotient boundaries use direct utility; `p=c,s=0` equality retained outside strict theorem |
| PDF identity | Publisher PDF, access date 2026-09-23 | Direct browser PDF view; 8 pages | Source version is directly rechecked; byte-level SHA-256 remains explicitly unresolved |

## Commands

```bash
python3 code/counterexample_exact.py
python3 code/symbolic_derivation.py
python3 code/independent_correspondence.py
python3 code/corollary_counterexample.py
python3 code/uniform_boundary_audit.py
```

Symbolic derivation uses SymPy 1.14.0. The exact checkers use only Python `fractions.Fraction`. The three programs have separate implementations and do not call one another.

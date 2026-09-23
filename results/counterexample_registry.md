# Counterexample and boundary regression registry

All entries use exact rational values. The source transcription and active-domain qualifications are documented in `derivations/source_transcription.md` and `derivations/uniform_rederivation.md`.

| ID | Target claim / branch | Parameters or boundary | Exact result | Status / artifact |
|---|---|---|---|---|
| CE-01 | Ringbom–Shy (2004), Eq. (6), high-refund choice | `β=1,p=3/5,c=1/50,s=0, α=(4/5,1/5), σ=(11/20,7/20)` | `r_H=5/27`, `r_L=25/39`; printed gap `+1/500`, primitive `Π_L−Π_H=−211/6500` | Reproduces strict reversal; `code/counterexample_exact.py`, `code/independent_correspondence.py` |
| CE-02 | Unqualified high-price Corollary 1 / outside option | `β=1,p=999/1000,c=9/10,s=0, α=(1/2,1/2), σ=(1/2,1/10)` | `r_H=998/999`, `r_L=8990/8991`; profits `0,−1/5,−2701/4500` for no booking, high-only, both types | No booking strictly dominates both feasible endpoints; `code/corollary_counterexample.py` |
| CE-03 | Strict uniform welfare claim `r*>r̄` at a cost boundary | `β=1,p=c=4/5,s=0` | `r*=r̄=0` | Shows active domain must require `p>c` for strict inequality; `code/uniform_boundary_audit.py` |
| CE-04 | `β<p`, zero-show type at full refund | `β=1/2,p=4/5,σ_L=0`, varying `s−c` | Endpoint payoff is positive, zero, or negative according to `s−c`; argmax is `{1}`, `[0,1]`, or `[0,1)` | Weak-tie boundary classification; `CERTIFICATION_REGRESSION_STAGE4A_SIGMA_ZERO.md` |
| CE-05 | Corrected endpoint equality | `β=1,p=3/5,c=59/260,s=0, α=(1/2,1/2), σ=(11/20,7/20)` | Both feasible endpoint profits equal `21/130`; argmax contains both `5/27` and `25/39` | Equality is set-valued; `code/independent_correspondence.py` |
| CE-06 | Zero threshold / lower strategy boundary | `β=1,p=3/5,σ_H=3/5` and a separate `σ_L=1/5,p=1/5` regression | `r_H=0` or `r_L=0`; weak participation includes the threshold type at zero | `code/independent_correspondence.py` |
| CE-07 | Threshold at upper strategy boundary | `β=1,p=4/5,σ_L=0` | `r_L=1` | Endpoint remains a candidate; mass limits and payoff signs tested in `code/independent_correspondence.py` |
| CE-08 | Full participation from the strategy lower bound | `β=1,p=3/5,σ_H=9/10,σ_L=4/5` | Both raw utilities are positive at `r=0` | Negative thresholds are handled as already active, not clipped into fictitious interior choices |
| CE-09 | No reservation for positive-show types | `β=1/2,p=4/5,σ_H=3/5,σ_L=1/5` | Both types have `EU_i(r)<0` for all `r∈[0,1]` | Argmax is the whole no-booking interval under zero payoff |
| CE-10 | Uniform cutoff quotient singularity | `β=p`, `β−rp=0`, and `p>β` branches | Direct utility distinguishes full-refund ties, a negative utility where denominator vanishes, and no positive-show reservation | `code/uniform_boundary_audit.py`; no division by zero is interpreted as evidence |

The registry separates strict reversals, weak ties, outside-option comparisons, and domain boundaries. It is a regression record, not by itself a proof of global optimality.

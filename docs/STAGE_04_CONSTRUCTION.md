# Stage 4 — Minimal model and theorem construction

## Input and verdict

- Input commit: `54657cae4dc22eb0b617cded2db46900907f6761` (Stage 3 output).
- **Stage 4 analytic construction: PASS TO INDEPENDENT CERTIFICATION.** The central endpoint identity, full feasible argmax correspondence, and independent uniform-section derivation are stated from primitive utility and payoffs. This is not a formal verification or theory-freeze verdict.

## Frozen model statement for certification

Let `β>0`, `p>0`, `c,s≥0`, `r∈[0,1]`, masses `α_H,α_L≥0` with `α_H+α_L=1`, and `0≤σ_L<σ_H<1`. The source uses `0<σ_L`; the `σ_L=0` case is retained as a limiting boundary. Consumers reserve if and only if

`EU_i(r)=σ_i(β−p)−(1−σ_i)(1−r)p≥0`.

Conditional on reservation, unit seller payoff is

`g_i(r)=σ_i(p−c)+(1−σ_i)((1−r)p+s−c)=p−c−(1−σ_i)(rp−s)`.

The seller's raw payoff is

`Π(r)=n∑_i α_i 1{EU_i(r)≥0}g_i(r)`, `n>0`.

On a region with fixed nonempty participating mass,

`Π'(r)=−np∑_(i participating) α_i(1−σ_i)<0`.

The proof uses this region slope plus exact threshold payoffs; no FOC is used to claim globality.

## Candidate theorem statements

**T1 — Corrected endpoint comparison.** If `p>0`, `σ_H>σ_L`, `σ_H,σ_L<1`, and `r_H,r_L` are defined by `EU_i(r_i)=0`, then

`[α_Hg_H(r_L)+α_Lg_L(r_L)]−α_Hg_H(r_H) = α_L[σ_L(β−s)−c+s] − α_H(σ_H−σ_L)(β−p)/(1−σ_L)`.

On the strict screening domain `0<r_H<r_L<1`, with positive masses, the higher-refund endpoint weakly beats the high-only endpoint iff the right-hand side is nonnegative; equality gives an endpoint tie. This is an endpoint comparison only.

**T2 — Complete two-type global argmax.** Under the frozen primitive rule above:

- If `β<p`, positive-show types never reserve. With the source's strict `σ_L>0`, `argmax Π=[0,1]`. In the enlarged `σ=0` boundary, only zero-show types can enter at `r=1`; the argmax is `{1}`, `[0,1]`, or `[0,1)` according to the sign of aggregate endpoint payoff `A_0(s−c)`.
- If `β=p`, no type with `σ_i<1` reserves for `r<1`; all are indifferent at `r=1`. Let `T=∑α_i[σ_i(p−c)+(1−σ_i)(s−c)]`. The argmax is `{1}` if `T>0`, `[0,1]` if `T=0`, and `[0,1)` if `T<0`.
- If `β>p`, form `C={0}∪{r_i:α_i>0, 0<r_i≤1}`, evaluate the primitive `Π` on `C`, and let `M` be the largest value. Let `ρ` be the smallest positive threshold of a positive-mass type if nobody participates at `r=0`. If `M=0` and such a no-booking interval exists, the argmax is the maximizing points in `C` together with `[0,ρ)`; otherwise it is precisely the maximizing points in `C`.

Thresholds below zero indicate participation already at `r=0`; thresholds at zero are ties included by the weak rule; a threshold equal to one is retained; absent types are omitted from `C`. Strictly decreasing profit on every nonempty fixed-set region proves no omitted interior maximizer exists. Exact definitions and all cases are in `derivations/two_type_global_correspondence.md`.

**T3 — Corrected global screening test and Corollary 1.** On `0<r_H<r_L<1`, both masses positive, the both-type endpoint is globally selected iff

`Π(r_L)≥max{0,Π(r_H)}`.

Equality is set-valued. The zero-profit term is the no-booking alternative. The published high-price Corollary 1 does not follow without sign and feasibility assumptions ensuring this global inequality.

**T4 — Uniform-section preservation.** On `β>p>c≥s≥0`, for `σ∼U[0,1]`, the separate active model has cutoff `σ̂=p(1−r)/(β−rp)`, private optimum `r̄=max{0,r_int}` with the source's interior formula, planner cutoff `(c−s)/(β−s)`, and `r*>r̄`. Equations (7)–(19), Propositions 2–4 and the corresponding welfare-loss branches are algebraically independent of the two-type Eq. (6) comparison and survive on this domain. At quotient singularities and outside the active domain, participation is classified from primitive utility, not the cutoff quotient.

## Exact regression point

For `(β,p,c,s,α_H,α_L,σ_H,σ_L)=(1,3/5,1/50,0,4/5,1/5,11/20,7/20)`,

`r_H=5/27`, `r_L=25/39`, `Π_H/n=53/125`, `Π_HL/n=509/1300`, and `Π_HL−Π_H=−211/6500` per unit mass. The printed Eq. (6) left-minus-right equals `1/500`. Both rates lie strictly in `[0,1]`; the parameter point satisfies `β>p>c≥s≥0`.

The direct exact computation, symbolic derivation, and independent primitive enumerator are maintained as separate programs. Stage 4A adds a fourth formal algebra certificate and a directed red-team suite.

## Limitations and next-stage contract

Stage 4 does not infer a global maximum from an FOC, numerical grid, or the endpoint inequality alone. Stage 4A must independently verify all candidate/tie branches, attack limits, and obtain a fresh Lean build. No Stage 8 freeze is allowed until the formal and scope gates close.

# Continuum/uniform section: clean-room rederivation

## Domain and threshold

The paper's closed-form welfare claims are assessed on the active domain `β>p>c≥s≥0`, with `p>0`. The strict inequality `p>c` is necessary for the strict comparison `r*>r̄`; at the excluded boundary `p=c,s=0`, both rates can equal zero. A uniform show-up type `σ∼U[0,1]` reserves iff `EU(σ;r)≥0`.

When `β−rp>0`, rearranging primitive utility gives

`σ̂(r)=p(1−r)/(β−rp)`.

On `β>p>0` and `r∈[0,1]`, `0≤σ̂(r)≤p/β<1` and

`σ̂'(r)=−p(β−p)/(β−rp)^2<0`.

The expected unit seller payoff is

`g_σ(r)=p−c−(1−σ)(rp−s)`.

For uniform types,

`π(r)/n=∫_{σ̂(r)}^1 g_σ(r)dσ`.

Leibniz's rule yields

`π'(r)/n=p(β−p)/(β−rp)^2 · [g_{σ̂(r)}(r)−(β−p)/2]`.

Since `g_{σ̂}=s−c+σ̂(β−s)` and `σ̂(r)` strictly decreases, the bracket strictly decreases in `r`; it crosses zero at most once. This proves globality of the candidate and excludes an omitted profitable endpoint/deviation.

## Private refund

Solving the unique interior FOC gives

`r_int=[β(3p−2(c−s))−2ps−β²]/[p(β−2c+p)]`.

Define

`p̃=β(β+2c−2s)/(3β−2s)`.

On the active domain, the denominator is positive and `r_int>0` iff `p>p̃`. Hence

`r̄=max{0,r_int}`.

The constrained optimum is unique. For `p<p̃`, the derivative is negative for all positive refunds and the unique maximizer is `r̄=0`. At `p=p̃`, the derivative is zero at `r=0` and strictly negative for `r>0`, so the argmax remains `{0}`. For `p>p̃`, the unique interior zero is the global maximizer. The corresponding cutoff is

`σ̂(r̄)=min{p/β, [β−p+2(c−s)]/[2(β−s)]}`.

## Planner refund and welfare loss

Adding consumer utility to seller profit cancels all transfers:

`W(r)/n=∫_{σ̂(r)}^1[(β−s)σ−(c−s)]dσ`.

The unconstrained optimal cutoff is

`σ̂*=(c−s)/(β−s)`.

It lies in `[0,p/β)` under `β>p>c≥s≥0`. Inverting the threshold gives

`r*=1−(c−s)(β−p)/[p(β−c)]`.

If `c=s`, `σ̂*=0` and `r*=1`; if `c>s`, `0<r*<1`. The private cutoff strictly exceeds the social cutoff both when `r̄=0` and when it is interior, so `r*>r̄` on this domain.

The welfare loss is

`ΔW=n(β−s)(σ̂(r̄)−σ̂*)²/2`.

Thus the two branches are

`ΔW=n(β−p)²/[8(β−s)]` if `p>p̃`,

`ΔW=n[p(β−s)−β(c−s)]²/[2β²(β−s)]` if `p≤p̃`.

The first branch has `∂ΔW/∂c=0`, `∂ΔW/∂p=−n(β−p)/[4(β−s)]<0`, and `∂ΔW/∂s=n(β−p)²/[8(β−s)²]>0`, holding the branch fixed. At `p=p̃` the refund function is clipped and branchwise derivatives must not be reported as global smooth comparative statics.

## Boundary and domain audit

- `r=0`: `σ̂=p/β∈(0,1)`; the derivative sign determines whether the constrained optimum is the lower corner.
- `r=1`: `σ̂=0` on `β>p`; the seller derivative is negative there, while the planner chooses it when `c=s`.
- `p=p̃`: the interior root meets `r=0`; the argmax is still the singleton `{0}`.
- `β=p`: the cutoff at `r=1` is `0/0`; direct utility gives no participation for `r<1` and indifference of all types at `r=1`. The strict active-domain theorem does not cover this tie branch.
- `p>β`: even at `r=1`, `EU=σ(β−p)<0` for `σ>0`; participation is empty and the profit function is zero. The unclipped integral formula is invalid there.
- `β−rp=0`: equation (8) cannot be used. At `β<p,r=β/p`, direct utility is `β−p<0`; no type participates. At `β=p,r=1`, all are indifferent.
- `p→c` from above: the formulas remain well-defined. The limit is not itself part of the strict welfare theorem; at `β=1,p=c=4/5,s=0`, both `r*` and `r̄` equal zero, so the strict inequality becomes equality.
- `c→s`: the social cutoff tends to zero and `r*→1`.
- `s→0`: all displayed active-domain expressions are continuous.
- Uniform support endpoints have measure zero. At the `β=p,r=1` tie, weak participation nevertheless applies to the entire continuum because utility is zero for every `σ`.

These results reproduce source equations (7)–(19), Proposition 2, Lemma 1, Propositions 3–4, and the table calculations only on the qualified active domain. They do not depend on the two-type Eq. (6) comparison.

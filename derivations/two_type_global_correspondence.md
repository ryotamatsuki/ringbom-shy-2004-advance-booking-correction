# Two-type model: primitive derivation and complete refund correspondence

## 1. Primitives and behavioral rule

Assume `β>0`, `p>0`, `c,s≥0`, `r∈[0,1]`, `α_H,α_L≥0`, `α_H+α_L=1`, and `0≤σ_L<σ_H<1`. The source uses `0<σ_L<σ_H<1`; the weak lower bound is used only to expose the `σ_L→0` limit. Consumers reserve at equality (`EU_i≥0`). This is the weak-participation reading used in source equation (7); the article does not separately state a tie-breaking convention.

The reservation payoff from source equation (1) is

`EU_i(r)=σ_i(β−p)−(1−σ_i)(1−r)p`

`=σ_i(β−rp)−p(1−r)`.

For `p>0`, this is strictly increasing in `r` for `σ_i<1`. Solving `EU_i(r)=0` gives

`r_i=(p−βσ_i)/(p(1−σ_i))`.

Thus `r_H=r_1` and `r_L=r_2` in the paper's notation. Direct subtraction gives

`r_L−r_H=(β−p)(σ_H−σ_L)/(p(1−σ_H)(1−σ_L))`.

The source's order `r_1<r_2` therefore requires `β>p`; when `β=p` the thresholds coincide at 1, and when `β<p` both are above 1. It is not a consequence of `σ_H>σ_L` alone.

The seller's per-reservation payoff follows directly from the two states:

`g_i(r)=σ_i(p−c)+(1−σ_i)((1−r)p+s−c)`

`=p−c−(1−σ_i)(rp−s)`.

At type `i`'s indifference refund,

`q_i:=g_i(r_i)=σ_i(β−s)+s−c`.

## 2. Correct endpoint comparison

For `β>p` and `0<r_H<r_L<1`, the high type alone participates at `r_H`, and both types participate at `r_L` under weak tie acceptance. Let

`Π_H/n=α_H g_H(r_H)=α_H q_H`,

`Π_{HL}/n=α_H g_H(r_L)+α_L q_L`.

The difference in the high type's payoff between the two rates is

`g_H(r_L)−g_H(r_H)=−(1−σ_H)p(r_L−r_H)`

`=−(σ_H−σ_L)(β−p)/(1−σ_L)`.

Therefore, exactly,

`(Π_{HL}−Π_H)/n = α_L[σ_L(β−s)−c+s] − α_H(σ_H−σ_L)(β−p)/(1−σ_L)`.

Consequently, among these two endpoints, `r_L` weakly beats `r_H` iff

`α_L[σ_L(β−s)−c+s] ≥ α_H(σ_H−σ_L)(β−p)/(1−σ_L)`.

This derivation uses no sign restrictions on `q_H` or `q_L`; it is an endpoint-profit identity. It does not, by itself, imply that either endpoint is globally optimal if the no-participation choice is feasible and more profitable.

The VOR's printed equation (6) drops the factor `1/(1−σ_L)`. It is not algebraically equivalent to the equation (5) endpoint comparison.

## 3. Actual profit schedule and the limitation of source equation (4)

With weak participation, the profit function over the full strategy set is

`Π(r)=n Σ_{i∈{H,L}} α_i 1{EU_i(r)≥0} g_i(r)`.

On a region where the participating set is fixed, its derivative is

`Π'(r)=−np Σ_{i participating} α_i(1−σ_i)`.

It is strictly negative whenever the participating mass is positive. The source's equation (4) substitutes `r_1` and `r_2` in its middle/high branches and hence lists endpoint values, not actual profit for every `r` in those intervals. The endpoint values are sufficient for candidate enumeration only after feasibility, entrant ties, and the no-booking region are included.

## 4. Complete global argmax correspondence

Define `Π(r)` by the primitive indicator formula above and keep all thresholds un-clipped for classification. This is a complete characterization on `r∈[0,1]` under weak participation.

### Case A: `β<p`

For every type with `σ_i>0`, `EU_i(r)≤EU_i(1)=σ_i(β−p)<0`, so it never reserves. A type with `σ_i=0` is strictly out for `r<1` and indifferent at `r=1`; under weak acceptance it reserves at that endpoint. Let `A_0=Σ_i α_i 1{σ_i=0}`. Profit is zero for `r<1`, and the endpoint profit is `A_0(s−c)`. Hence:

- if `A_0(s−c)>0`, the argmax is `{1}`;
- if `A_0(s−c)=0`, the argmax is `[0,1]`;
- if `A_0(s−c)<0`, the argmax is `[0,1)`.

On the source's strict domain `0<σ_L<σ_H<1`, `A_0=0` and all refunds yield zero profit, so the argmax is `[0,1]`. The exact `σ=0` boundary is retained because the audit also reports limiting cases.

### Case B: `β=p`

For `r<1`, types with `σ_i<1` strictly prefer not to reserve. At `r=1`, both types are indifferent and weak participation makes them reserve. Let

`T=Σ_i α_i[σ_i(p−c)+(1−σ_i)(s−c)]`.

Then

- if `T>0`, `argmax Π={1}`;
- if `T=0`, `argmax Π=[0,1]`;
- if `T<0`, `argmax Π=[0,1)`.

This branch is tie-rule sensitive at `r=1`. Under strict rejection of indifference, the `r=1` payoff would instead be zero.

### Case C: `β>p`

The thresholds satisfy `r_H<r_L≤1`; equality at the upper boundary occurs when the low type has `σ_L=0`. Let

`C={0} ∪ {r_i : α_i>0 and 0<r_i≤1}`,

`M=max_{r∈C}Π(r)`, and `C*={r∈C:Π(r)=M}`.

If all positive-mass types have `r_i>0`, let `ρ=min{r_i:α_i>0}`. When `M=0`, the entire interval `[0,ρ)` also maximizes profit because nobody reserves there. The complete argmax is therefore `C*∪[0,ρ)` in this case. In every other case, the argmax is exactly `C*`.

This candidate rule is complete because profit is constant on the initial no-reservation region and strictly decreasing on every nonempty fixed-participation region. All jumps occur at the type-specific thresholds and are evaluated using the stated weak tie rule. It covers negative thresholds (participation already active at `r=0`), zero thresholds (ties at `r=0`), positive feasible thresholds, absent types (`α_i=0`), and the flat no-reservation correspondence. When `σ_i=0`, the threshold can equal 1 and the rule includes it.

## 5. Boundary logic

- `r_i<0`: type `i` strictly participates at `r=0`; negative refund rates are not feasible and must not be recommended.
- `r_i=0`: type `i` is indifferent at zero and participates under the adopted weak rule.
- `0<r_H<r_L<1`: the textbook screening regions exist. Proposition 1's factor correction is valid for comparing `r_H` and `r_L`, but zero-profit nonparticipation can still dominate if the H-only endpoint profit is nonpositive.
- `r_L=0`: both thresholds are nonpositive; both types participate from the lower boundary.
- `r_L=1`: occurs at the relevant boundary `β=p` or in the `σ_L=0` limit; direct utility, not an unclipped cutoff, decides participation.
- `β−rp=0`: the continuum cutoff formula is undefined. If `β<p` and `r=β/p`, then `EU_i=β−p<0` for all positive-`σ` types; a zero-`σ` type remains out until `r=1`. If `β=p,r=1`, all types are indifferent.
- `σ_L→0`: `r_L→1` when `β>p`; at the limit, a type that never shows is indifferent only at a full refund.
- `σ_L→σ_H`: the two thresholds merge. At equality there is no positive-length H-only interval, and a comparison that treats `r_H` as H-only is not the correct tie-inclusive candidate comparison.
- `α_L→0` or `α_H→0`: the endpoint identity has a continuous limit, but absent-type thresholds are omitted from the candidate set; the remaining type's threshold and no-booking interval determine the optimum.
- `p→c`, `c→s`, and `s→0`: no denominator in the corrected comparison or the direct payoff schedule becomes singular. The uniform formulas are separately limited to their stated domain.

## 6. Global optimality and existence

The finite candidate set plus, where applicable, the initial flat interval is a global argmax certificate, not an FOC claim. On every nonempty participation segment the profit slope is strictly negative; at each boundary the exact weak-tie payoff is computed. Thus the maximum is attained. The independent implementation in `code/independent_correspondence.py` evaluates these raw primitives and checks 800 seeded rational parameter draws plus 21 directed exact edge regressions; it does not call the symbolic script or reuse its derived profit difference.

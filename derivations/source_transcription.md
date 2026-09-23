# VOR transcription and source-page ledger

Source: Staffan Ringbom and Oz Shy (2004), “Advance Booking, Cancellations, and Partial Refunds,” *Economics Bulletin* 13(1), 1–7. The source is the publisher-hosted VOR listed in `sources/source_manifest.md`. Physical PDF page numbers differ from printed article pages because the PDF has a separate cover/abstract page.

## Bibliographic record and front matter

- Exact title and author order: “Advance Booking, Cancellations, and Partial Refunds”; Staffan Ringbom and Oz Shy.
- Journal record: *Economics Bulletin*, vol. 13, no. 1, 2004, pp. 1–7.
- The VOR states submitted January 11, 2004 and accepted January 20, 2004. It displays no DOI or PII.
- The PDF contains eight physical pages: one title/abstract page plus seven printed article pages.
- Abstract, paraphrased: the paper develops methods for privately optimal and socially optimal partial refunds, describes screening by show-up probabilities, and claims the social refund exceeds the equilibrium refund.
- There is no separate conclusion heading. The article ends with Proposition 4 and a sentence introducing Table 2's welfare-loss illustrations, followed by references.

## Source assumptions and two-type equations

The two-type section assumes `α_H+α_L=1`, `0<σ_L<σ_H<1`, cost `c≥0`, salvage value `s≥0`, and a single refund rate `r∈[0,1]`. Price `p` is exogenous. No explicit tie rule is stated; the utility condition and later continuum cutoff use weak participation. Our analysis therefore declares `EU≥0` participation and flags equality behavior as a convention.

### Equation (1), physical PDF p. 3 / printed p. 2

For a reserving type `i∈{H,L}`:

`EU_i(r)=σ_i(β−p)−(1−σ_i)(1−r)p`; the outside option is zero.

The source describes the show-up payoff as `β−p` and the cancellation/no-show loss to the consumer as the non-refundable amount `(1−r)p`.

### Equations (2)–(3), physical PDF p. 3 / printed p. 2

Setting (1) equal to zero gives the low-type threshold and high-type threshold, respectively:

`r_2=(p−βσ_L)/(p(1−σ_L))`,

`r_1=(p−βσ_H)/(p(1−σ_H))`.

The source says `r_2>r_1`. Direct subtraction shows this ordering requires `β>p` (for the source's strict type ordering and `p>0`); it does not follow from `σ_H>σ_L` alone.

### Equation (4), physical PDF p. 4 / printed p. 3

As displayed, the source labels the following expression `Eπ(r)` for refund regions:

`n(p−c) − [α_L n(1−σ_L)+α_H n(1−σ_H)](r_2p−s)`, for `r≥r_2`;

`α_H n[p−c−(1−σ_H)(r_1p−s)]`, for `r_1≤r<r_2`;

`0`, for `r<r_1`.

The displayed payoff expressions substitute `r_2` and `r_1` in the upper and middle regions. They are endpoint values, not the actual payoff at every interior `r` in those regions. From the source's state-contingent payoffs, the actual schedule at a fixed participation set is affine in the chosen `r` and decreasing whenever positive mass participates.

### Equations (5)–(6), Proposition 1, Corollary 1, physical PDF p. 4 / printed p. 3

Equation (5) compares the two endpoint values:

`(p−c)−[α_L(1−σ_L)+α_H(1−σ_H)](r_2p−s) ≥ α_H[p−c−(1−σ_H)(r_1p−s)]`.

Printed equation (6) and Proposition 1 state that `r_2` is the profit-maximizing refund iff

`α_L[σ_L(β−s)−c+s] ≥ α_H(σ_H−σ_L)(β−p)`,

and otherwise say `r_1` is profit maximizing. Independent algebra in `derivations/two_type_global_correspondence.md` shows that the right-hand term in this comparison must be divided by `(1−σ_L)` when the two endpoint profits are compared. The statement also omits the feasible no-booking alternative and does not state the threshold-feasibility domain.

Corollary 1 states that both types are served if `p` is sufficiently high, `α_H` or `σ_H` sufficiently low, or `σ_L` sufficiently high. The boundary and sign qualifications are audited separately; this transcription does not endorse the blanket claim.

## Continuum and uniform equations

The general-type section assumes `σ∈(0,1]`, an absolutely continuous distribution `F_σ` with `F_σ(0)=0`, `F_σ(1)=1`, and density `f_σ`.

### Equations (7)–(9), physical PDF p. 4 / printed pp. 3–4

For a reserving type `σ`, equation (7) gives `EU(σ;r)=σ(β−p)−(1−σ)(1−r)p`, with zero outside utility. The indifference cutoff is

`σ̂(r)=(p−rp)/(β−rp)` (8),

and the source says types `σ≥σ̂` reserve. Expected unit seller gross profit is

`g_σ(r)=p−c−(1−σ)(rp−s)=p−rp+σ(rp−s)+s−c` (9).

### Equations (10)–(12), physical PDF p. 5 / printed p. 4

Equation (10):

`π(r)=n∫_(σ̂(r),1] g_σ(r) dF_σ`.

Equation (11), as a first-order condition for an interior solution, is

`(1/n)dπ/dr = ∫_(σ̂,1] (∂g_σ/∂r)dF_σ − (dσ̂/dr) f_σ(σ̂) g_σ|_(σ=σ̂)=0`.

The source records `dσ̂/dr=−p(β−p)/(β−rp)^2=−p(1−σ̂)/(β−rp)` and `∂g_σ/∂r=p(σ−1)`. Substitution yields equation (12):

`(1/(np))dπ/dr = ∫_(σ̂,1](σ−1)f_σ(σ)dσ + (β−p) f_σ(σ̂) g_σ|_(σ=σ̂)/(β−rp)^2=0`.

The text says that if no interior solution exists, the non-refundable corner `r=0` maximizes profit. The qualification to the active domain is part of our rederivation.

### Equations (13)–(16) and Proposition 2, physical PDF pp. 5–6 / printed pp. 4–5

For `σ∼U[0,1]`, equation (13) rewrites the FOC as

`(1/(np))dπ/dr = −(β−p)^2/[2(β−rp)^2] + (β−p)g_σ|_(σ=σ̂)/(β−rp)^2 = 0`,

so the source obtains `g_σ|_(σ=σ̂)=(β−p)/2>0`.

Equation (14) gives

`r̄=max{0,[β(3p−2(c−s))−2ps−β^2]/[p(β−2c+p)]}`.

Equation (15) defines

`p̃=β[1−2(β−c)/(3β−2s)] = β(β+2c−2s)/(3β−2s)`.

Equation (16) gives the optimal cutoff

`σ̂(r̄)=min{p/β,[(β−p)+2(c−s)]/[2(β−s)]}`.

Proposition 2 says that for `p>p̃`, the private refund is increasing in `p` and `s` and decreasing in `c`; otherwise `r̄=0`.

### Equation (17), Lemma 1, Proposition 3, Table 1, physical PDF p. 6 / printed p. 5

Equation (17) defines welfare as consumer surplus plus expected seller profit and simplifies it to

`W(r)=n(β−s)∫_(σ̂(r),1]σ dF_σ − n(c−s)∫_(σ̂(r),1]dF_σ`.

Lemma 1 states

`r*=1−(c−s)(β−p)/[p(β−c)]`,

and that unit gross profit is zero at the marginal participating type. Its proof identifies the welfare-optimal cutoff as `(c−s)/(β−s)`.

Proposition 3 says `r*>r̄`; if `s=c`, the social refund is full, and if `s<c`, it is partial. Our independent globality proof is restricted to the active domain stated in the derivation.

Table 1 gives simulated pairs `r̄<r*`, with `β=1`, uniform show-up probabilities. Columns are `(c,s)=(0.2,0.1),(0.1,0.1),(0.1,0),(0,0)`:

| `p` | `(0.2,0.1)` | `(0.1,0.1)` | `(0.1,0)` | `(0,0)` |
|---:|---:|---:|---:|---:|
| 0.8 | 0.929 < 0.969 | 0.969 < 1 | 0.9375 < 0.972 | 0.972 < 1 |
| 0.6 | 0.667 < 0.917 | 0.810 < 1 | 0.714 < 0.926 | 0.833 < 1 |
| 0.5 | 0.364 < 0.875 | 0.250 < 1 | 0.462 < 0.889 | 0.357 < 1 |
| 0.4 | 0 < 0.8125 | 0.250 < 1 | 0 < 0.833 | 0.357 < 1 |

### Equations (18)–(19), Proposition 4, Table 2, physical PDF p. 7 / printed p. 6

Equation (18) expresses the welfare loss as

`ΔW=W(r*)−W(r̄)=n∫_((c−s)/(β−s))^(σ̂(r̄))[(β−s)σ−(c−s)]dF_σ>0`.

For uniform types, equation (19) gives

`ΔW = n(β−p)^2/[8(β−s)]` if `p>p̃`,

and

`ΔW = n[p(β−s)−β(c−s)]^2/[2β^2(β−s)]` if `p≤p̃`.

Proposition 4 says, on the high-price branch `p>p̃`, welfare loss is independent of `c`, decreasing in `p`, and increasing in `s`.

Table 2 reports simulated welfare losses for `β=1`, uniform types, and `n=1000`, with columns `(c,s)=(0.2,0.1),(0.1,0.1),(0.1,0),(0,0)`:

| `p` | `(0.2,0.1)` | `(0.1,0.1)` | `(0.1,0)` | `(0,0)` |
|---:|---:|---:|---:|---:|
| 0.8 | 5.556 | 5.556 | 5.000 | 5.000 |
| 0.6 | 22.22 | 22.22 | 20.00 | 20.00 |
| 0.5 | 34.72 | 34.72 | 31.25 | 31.25 |
| 0.4 | 37.56 | 50.00 | 45.00 | 45.00 |

## References printed in the VOR

The VOR's reference list contains the following 13 records; spelling below follows the VOR where noted. These are transcribed for source completeness, not all cited by the correction manuscript.

1. Courty, P. and H. Li (2000), “Sequantial Screening,” *Review of Economic Studies* 67:697–717. The VOR spells “Sequential” as “Sequantial.”
2. Dana, J. D. J. (1998), “Advanced Purchase Discounts and Price Discrimination in Competitive Markets,” *Journal of Political Economy* 106(2):395–422.
3. Gale, I. (1993), “Price Dispersion in a Market with Advance-Purchases,” *Review of Industrial Organization* 8(4):451–464.
4. Gale, I. L. and T. J. Holmes (1992), “The Efficiency of Advance-Purchase Discounts in the Presence of Aggregate Demand Uncertainty,” *International Journal of Industrial Organization* 10(3):413–425.
5. Gale, I. L. and T. J. Holmes (1993), “Advance-Purchase Discounts and Monopoly Allocation of Capacity,” *American Economic Review* 83(1):135–146.
6. Mann, D. P. and J. P. Wissink (1988), “Money-Back Contracts with Double Moral Hazard,” *RAND Journal of Economics* 19(2):285–292.
7. Mann, D. P. and J. P. Wissink (1990), “Money-Back Warranties vs. Replacement Warranties: A Simple Comparison,” *American Economic Review* 80(2):432–436.
8. McGill, J. and G. van Ryzin (1999), “Revenue Management: Research Overview and Prospects,” *Transportation Science* 33(2):233–256.
9. Miravete, E. J. (1996), “Screening Consumers through Alternative Pricing Mechanisms,” *Journal of Regulatory Economics* 9(2):111–132.
10. Moorthy, S. and K. Srinivasan (1995), “Signalling Quality With a Money-Back Guarantee: The Role of Transaction Costs,” *Marketing Science* 14(4):442–466.
11. Ringbom, S. and O. Shy (2003), “Reservations and Refunds,” working paper; VOR says available from `www.ozshy.com`.
12. Shiou, S. (1996), “Price and Money Back Guarantees as Signals of Product Quality,” *Journal of Economics and Management Strategy* 5(3):361–377.
13. Xie, J. and S. M. Shugan (2001), “Electronic Tickets, Smart Cards, and Online Payments: When and How to Advance Sell,” *Marketing Science* 20(3):219–243.

## Equation-to-source locator

| Object | PDF page | Printed page |
|---|---:|---:|
| Abstract and submission metadata | 1 | — |
| Eq. (1) | 3 | 2 |
| Eqs. (2)–(3) | 3 | 2 |
| Eqs. (4)–(6), Proposition 1, Corollary 1 | 4 | 3 |
| Eqs. (7)–(9) | 4 | 3 |
| Eqs. (10)–(16) | 5 | 4 |
| Proposition 2 continuation; Eq. (17), Lemma 1, Proposition 3, Table 1 | 6 | 5 |
| Eqs. (18)–(19), Proposition 4, Table 2 | 7 | 6 |
| References | 7–8 | 6–7 |

The last table is a page locator, while each formula above supplies the source equation number. The source copyright PDF is not included in this repository.

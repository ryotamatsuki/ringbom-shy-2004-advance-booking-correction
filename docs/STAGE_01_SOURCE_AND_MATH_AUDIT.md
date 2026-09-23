# Stage 1 — Source and Mathematical Audit

## Verdict

**GO TO NOVELTY GATE.** The VOR is directly re-opened, the central Eq. (5)–(6) discrepancy is reproduced by distinct methods, and the research question has a precise remaining claim: the corrected feasible two-type correspondence. The binary VOR-PDF hash remains unavailable through the retrieval surface; source identity is otherwise frozen and that limitation is recorded rather than concealed.

## Canonical source model

One seller chooses a single `r∈[0,1]` after an exogenous `p`; potential consumers have reservation value `β` and show-up probability `σ`. A consumer reserves iff `EU(σ;r)≥0`; conditional seller unit profit is state-contingent. In the two-type section, show probabilities satisfy `0<σ_L<σ_H<1`; masses satisfy `α_H+α_L=1`. The source does not state a tie-breaking rule in the two-type section; weak acceptance follows its equation (7) and is made explicit here.

## Equation-by-equation findings

| Source object | Independent finding |
|---|---|
| Eq. (1), expected utility | Correct as transcribed. Utility is increasing in `r` for `p>0`, `σ<1`. |
| Eqs. (2)–(3), thresholds | Correct indifference formulas. Their order `r_1<r_2` requires `β>p`; the paper does not state this beside the two-type section. |
| Eq. (4), profit schedule | Its displayed values are threshold endpoint profits, not profit at every rate in each stated interval. Actual profit is linear and strictly decreasing in `r` within a fixed nonempty participant set. |
| Eq. (5), candidate comparison | Correct as a comparison of the two endpoint candidate profits when both thresholds represent the intended participation sets. |
| Proposition 1 / Eq. (6) | Incorrect algebra: the high-type term requires division by `1−σ_L`. Exact counterexample is within `β>p>c≥s≥0`, with both thresholds strictly feasible. |
| Corollary 1 | Its listed sufficient conditions omit feasibility and the seller's zero-profit no-booking alternative. An exact high-price sequence below makes both feasible screening endpoints loss-making, so no reservation is globally optimal. |
| Eqs. (7)–(12) | Correct on the interior threshold domain `β>p>0`, with density/regularity for Leibniz differentiation. Outside it, clipping and direct utility are needed. |
| Eqs. (13)–(16), Proposition 2 | Correctly re-derived on `β>p>c≥s≥0`; the private optimum is globally unique by a strictly decreasing derivative bracket. The clipped point `p=p̃` is a kink. |
| Eq. (17), Lemma 1, Proposition 3 | Correct on `β>p>c≥s≥0`. Refunds cancel as transfers; the planner chooses the cutoff `(c−s)/(β−s)`. The strict inequality `r*>r̄` fails as a strict statement at the excluded boundary `p=c,s=0`, where both can be zero. |
| Eqs. (18)–(19), Proposition 4 | Correct after the domain qualification and branchwise interpretation. The stated high-price derivatives are local to `p>p̃`. |
| Tables 1–2 | Independent exact recheck finds two incorrect private-refund entries in Table 1 (both in the `p=0.5` row); the other Table 1 refund/social values and all Table 2 welfare-loss values reproduce. These are numerical illustrations, not independent proof. |

## Corrected endpoint identity and exact regression

The independent exact point is

`(β,p,c,s,α_H,α_L,σ_H,σ_L)=(1,3/5,1/50,0,4/5,1/5,11/20,7/20)`.

The thresholds are `r_1=5/27` and `r_2=25/39`. The primitive expected profits per potential-consumer mass are `53/125` (H only) and `509/1300` (both), so the actual difference is `−211/6500`. The printed Eq. (6) condition has left-minus-right `+1/500`. Hence the source selects the lower-profit endpoint.

Evidence paths: VOR transcription; independent SymPy identity; raw state-contingent expected-payoff code using `Fraction`; separately written direct-utility candidate enumerator. Separate exact tests cover Corollary 1's outside-option issue and uniform boundary limits; see `results/evidence_ledger_stage01.md` and `code/`.

## Feasibility, ties, and no-participation audit

For `β>p`, thresholds are ordered and below 1, but they can be negative. A negative `r_1` means high types already participate at `r=0`; it cannot be selected as a feasible refund. A positive `r_1` can still yield negative seller profit, so the interval before the first positive threshold, where nobody reserves and profit is zero, can dominate both textbook endpoint candidates. At `r_i=0`, the tie is included under weak acceptance. At `β=p`, both groups become indifferent at `r=1`; at `β<p`, no positive-σ consumer reserves even with full refund. These branches and equality behavior are fully recorded in `derivations/two_type_global_correspondence.md`.

**Scope correction from the boundary red-team:** the source's two-type domain has `σ_L>0`, so the preceding statement is correct there. In the deliberately enlarged `σ_L=0` boundary test, a zero-show type is indifferent at `r=1` even when `β<p`. Under the adopted weak-participation rule it reserves at that endpoint, with unit profit `s−c`. This case is now explicit in the global correspondence and exact checker; see `docs/CERTIFICATION_REGRESSION_STAGE4A_SIGMA_ZERO.md`. It does not alter the source-domain counterexample or corrected endpoint identity.

## Corollary 1 / outside-option counterexample

The published Corollary 1 is not valid as an unconditional statement on the primitive domain because its listed comparative conditions do not ensure positive seller profit. Set `β=1`, `c=9/10`, `s=0`, `α_H=α_L=1/2`, `σ_H=1/2`, and `σ_L=1/10`, and take `p=1−1/m` for sufficiently large integer `m`. Both thresholds are feasible for all such `p`. As `p↑β`, the H-only and both-type endpoint profits converge to `−1/5` and `−3/5`; continuity therefore makes both endpoints strictly loss-making throughout a neighborhood below `β`. The no-booking choice gives zero and strictly dominates. At the exact rational regression `p=999/1000`, `r_H=998/999`, `r_L=8990/8991`, `Π_H/n=−1/5`, and `Π_HL/n=−2701/4500`. The exact primitive evaluator is `code/corollary_counterexample.py`.

On the strict screening domain `0<r_H<r_L<1` with positive masses, the corrected global both-served test compares the both-type endpoint to both alternatives: `r_L` is selected iff `Π(r_L)≥max{0,Π(r_H)}`. Equality is set-valued. At threshold/domain boundaries, use the full candidate correspondence in `derivations/two_type_global_correspondence.md`. The algebraic factor correction alone does not imply global optimality. A high-price statement can be recovered only under additional sign and feasibility conditions ensuring that the both-type endpoint is nonnegative and at least as profitable as the high-only endpoint; those conditions are not imposed by Corollary 1 as printed.

## Continuum/uniform and welfare audit

The uniform formula is independent of the two-type comparison. The cutoff, profit derivative, clipped unique refund, social cutoff, welfare-loss branches, and comparative-static signs were rederived from primitives on the strict domain `β>p>c≥s≥0`. At `p=c,s=0`, `r*=r̄=0`; this is a boundary limit, not an exception to hide inside the theorem. At `β=p` or `β−rp=0`, the cutoff quotient is undefined and is replaced by direct utility classification. A new exact recheck found that Table 1 prints `r̄=0.250` for `(β,p,c,s)=(1,0.5,0.1,0.1)` and `r̄=0.357` for `(1,0.5,0,0)`, although the primitive optimum is `8/13` and `2/3`, respectively. The two published values match the `p=0.4` row and are not mere rounding. The direct profit gains at the corrected optima are `361/35280` and `863041/86382368`; all Table 2 welfare-loss entries match recomputation using the primitive optimum. See `code/uniform_table_audit_exact.py` and `results/uniform_table_audit_stage4a.md`.

## Residual question for Stage 2

Whether the exact Eq. (6) correction and complete feasible correspondence have already been publicly disclosed or are absorbed by a prior general refund/screening result. Stage 2 may classify the surviving contribution and decide whether a correction note is justified; it may not widen the model to rescue novelty.

## Next-stage contract

Stage 1 input commit: `f936faa5865da528a300213f2c5c086415c795d0`. Its output commit is recorded in the next-stage commit ledger.

Stage 2 searches exact correction disclosures, the 2003 predecessor, later same-author refund work, all discoverable forward citations, equivalent screening results, and *Economics Bulletin* correction/comment precedent. Preserve the model and theorem statements above.

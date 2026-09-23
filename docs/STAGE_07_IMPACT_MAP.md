# Stage 7 — Welfare, interpretation, and scope impact map

## Input, question, and verdict

- Input commit: `88fc37a00d36ff164414d780e71255aa30c17138` (Stage 6 novelty re-kill).
- Controlling source: the 2004 publisher VOR, with equation/page transcription in `derivations/source_transcription.md`.
- **Verdict: PASS TO STAGE 7.5 WITH DOMAIN QUALIFICATIONS.** The two-type Proposition 1 / Eq. (6) comparison is wrong as printed; its corrected endpoint comparison and the global correspondence are established. Corollary 1 needs feasibility and an outside-option qualification. The uniform theory is independent of Eq. (6) and survives on its strict active domain, while two printed Table 1 private-rate entries require correction. No evidence supports saying the whole paper is invalid.

## Claim-by-claim status

| VOR item / claim | Status | Finding and defensible scope |
|---|---|---|
| Eq. (1), two-type expected utility | **SURVIVES UNCHANGED** | Primitive expected utility is correctly stated. Participation is weak at equality under the paper's continuum convention; the two-type tie rule is made explicit in this reassessment. |
| Eqs. (2)–(3), indifference refunds | **SURVIVES WITH DOMAIN QUALIFICATION** | The threshold formulas are correct for `p>0` and `σ_i<1`. The asserted ordering `r_1<r_2` requires `β>p`; feasibility additionally requires evaluating each un-clipped threshold against `[0,1]`. |
| Eq. (4), displayed piecewise profit | **CORRECTED** | The expressions substitute `r_1` and `r_2`, so they are the payoff values at participation boundaries, not the actual payoff at every interior `r` in each displayed region. The actual schedule is affine and strictly decreasing wherever positive mass participates. The candidate-boundary values themselves are correct. |
| Eq. (5), endpoint inequality | **SURVIVES WITH DOMAIN QUALIFICATION** | It correctly compares the high-only and both-types boundary payoffs when the two thresholds are feasible and represent the stated participation sets. It does not compare either endpoint with no booking. |
| Eq. (6) and Proposition 1, printed criterion | **INVALIDATED** | The high-type loss term is missing `1/(1−σ_L)`. The exact source-domain regression has `r_H=5/27`, `r_L=25/39`, printed rule margin `1/500>0`, but both-types profit minus high-only profit `−211/6500<0`. The printed iff rule is false. |
| Corrected endpoint difference | **CORRECTED** | Per potential-consumer mass, `Π(r_L)−Π(r_H)=α_L[σ_L(β−s)−c+s]−α_H(σ_H−σ_L)(β−p)/(1−σ_L)`. Its sign is necessary and sufficient only for this endpoint comparison. Equality gives an endpoint tie. |
| Complete two-type refund choice | **CORRECTED** | The global correspondence evaluates `r=0`, each positive-mass feasible indifference threshold, and any initial no-booking plateau; it uses raw utility for `β≤p`, ties, negative/zero/one thresholds, absent types, and equal-profit sets. Fixed-set profit is decreasing, so no interior maximizer is omitted. This is model-specific. |
| Corollary 1, both types served under broad comparative conditions | **CORRECTED** | On `0<r_H<r_L<1` with positive masses, the both-types endpoint is globally selected iff `Π(r_L)≥max{0,Π(r_H)}`. The printed high-price implication is false without profitability and feasibility conditions: at `p=999/1000` the two screening endpoints are `−1/5` and `−2701/4500`, while no booking yields zero. The other comparative directions are not blanket guarantees when the low type's incremental payoff is negative. |
| Eqs. (7)–(9), continuum utility, cutoff, unit payoff | **SURVIVES WITH DOMAIN QUALIFICATION** | These formulas are correct where `β−rp>0` and the cutoff lies in the support. On `β>p>0`, the cutoff stays in `[0,p/β]`; outside that active region use clipping or direct utility rather than the quotient. |
| Eqs. (10)–(12), general-distribution profit and FOC | **SURVIVES WITH DOMAIN QUALIFICATION** | The integral and Leibniz derivative are correct for the interior-cutoff case with the stated density regularity. They are not a global-optimum certificate for arbitrary distributions; boundary solutions and cutoff support must be checked. |
| Eqs. (13)–(16) and Proposition 2, uniform private optimum | **SURVIVES WITH DOMAIN QUALIFICATION** | On `β>p>c≥s≥0`, the derivative bracket is strictly decreasing; the unique constrained private optimum is `r̄=max{0,r_int}` and the displayed cutoff/price threshold are correct. At the clipping point `p=p̃`, branchwise derivatives do not define smooth global comparative statics. |
| Eq. (17) and Lemma 1, welfare and social cutoff | **SURVIVES WITH DOMAIN QUALIFICATION** | Transfers cancel in welfare, and the planner cutoff `(c−s)/(β−s)` yields the stated social refund. Distribution gaps may make the maximizing rate nonunique, but the displayed rate remains welfare maximizing under the active domain. |
| Proposition 3, `r*>r̄` | **SURVIVES WITH DOMAIN QUALIFICATION** | The strict inequality and partial/full-refund statement hold on `β>p>c≥s≥0`. At the excluded boundary `p=c,s=0`, both rates can be zero, so strictness fails. |
| Eqs. (18)–(19) and Proposition 4, welfare loss | **SURVIVES WITH DOMAIN QUALIFICATION** | The two uniform welfare-loss branches and high-branch comparative statics reproduce. Statements about derivatives in `p,c,s` are conditional on remaining on the branch `p>p̃`. |
| Table 1, simulated private/social refund rates | **CORRECTED** | Two private rates in the `p=0.5` row are wrong: for `(c,s)=(0.1,0.1)`, replace `0.250` by `8/13≈0.615385`; for `(c,s)=(0,0)`, replace `0.357` by `2/3≈0.666667`. The other 14 private rates and all 16 social rates match at the printed precision. |
| Table 2, simulated welfare loss | **SURVIVES WITH DOMAIN QUALIFICATION** | All 16 displayed welfare-loss values reproduce at the printed precision when computed from the primitive optimum on the table's active domain. The table is illustrative, not a proof. |
| Abstract/conclusion that social refund exceeds the private/equilibrium refund | **SURVIVES WITH DOMAIN QUALIFICATION** | The claim is supported by the uniform analysis on `β>p>c≥s≥0`; it is not derived from the two-type Proposition 1 comparison and should be stated with this domain. |
| Full 2003 predecessor/version chain | **UNRESOLVED** | The VOR's own characterization distinguishes a full-refund predecessor. Public catalog records reveal related working-paper titles but do not supply the predecessor's full text; no absolute priority claim follows. |

## Welfare and interpretation

The Eq. (6) error changes the recommended refund for some parameter values because the incorrect criterion can rank two feasible endpoints in the wrong order. Even with the corrected endpoint ranking, neither endpoint must be chosen if its profit is below zero. The appropriate economic comparison includes the seller's no-booking alternative.

The Corollary 1 counterexample is not merely an endpoint-ranking reversal. Near `p=β`, both types require refunds close to full reimbursement. Under the exact stated values, both candidate schedules lose money, so a seller who can decline reservations earns more by taking no reservations. The source's high-price sentence therefore needs a profitability restriction.

The uniform model is a separate continuous-type problem. Its first-order conditions, clipped private optimum, social cutoff, welfare loss, and comparative statics do not use Eq. (6). On the audited active domain, those results survive. The two Table 1 errors are isolated numeric entries; Table 2 and the underlying private/social formulas are consistent.

## Maximum defensible wording

> The published two-type endpoint condition in Ringbom and Shy (2004) omits a factor, and its unrestricted refund-choice statement also suppresses feasibility and the no-booking option. We give the corrected endpoint comparison and a complete model-specific correspondence. The paper's uniform-distribution welfare results remain valid on their active domain, although two private-refund entries in its Table 1 do not match the model's own formula.

Do not use “fatal flaw,” “invalidates the paper,” “first ever,” or a claim that the uniform welfare theorem is affected by Eq. (6).

## Evidence and next-stage contract

- Endpoint identity, exact counterexamples, candidate correspondence, and uniform formulas: `derivations/two_type_global_correspondence.md`, `derivations/uniform_rederivation.md`, and `docs/THEOREM_CERTIFICATES_STAGE04.md`.
- Exact Table 1 and Table 2 recheck: `code/uniform_table_audit_exact.py` and `results/uniform_table_audit_stage4a.md`.
- Formal scope and CI evidence: `formal/FORMAL_VERIFICATION_CERTIFICATE.md` and `docs/STAGE_04A_CERTIFICATION.md`.
- Novelty boundary: `docs/STAGE_06_NOVELTY_REKILL.md` and `results/novelty_ledger_stage06.md`.
- Stage 7.5 must choose a concise correction/comment architecture, freeze the maximum-defensible statements, and record the unresolved predecessor disclosure boundary. No extension is required to make this contribution intelligible.


# Astra Pre-Submission Remediation — Stage 14 Reopen

Date: 2026-09-23

## Scope

An independent hostile-referee audit classified the manuscript as MAJOR REVISION REQUIRED, not because of a fatal mathematical defect, but because the submission artifact, source, and QA record had drifted and several proof/exposition claims needed tightening.

This remediation does **not** expand the model, add a new general screening theorem, enter Stage 15, merge to main, or submit the paper. The Stage-8 central theorem set remains unchanged. Stage 13/14 are reopened only for integration and submission QA.

## Resolution map

| Audit item | Resolution |
|---|---|
| M01 stale tracked PDF | The repository-tracked PDF is removed. Generated PDFs are ignored by Git. CI emits a commit-specific artifact named `submission-pdf-<commit SHA>` with a SHA-256 companion file. `scripts/check_pdf.sh` fails if the generated PDF is tracked. |
| C01 seller/consumer attribution | Proposition 1 proof states that the seller earns (q_L) from a type-L reservation. |
| C02 accounting primitives | Model text states advance payment, refund/forfeiture, state-contingent seller payoffs, cost treatment, and salvage treatment before expected profit. |
| C03 original Corollary 1 relation | The manuscript states that the new corollary is a profitability/global-choice qualification, not a four-part replacement comparative-statics theorem. |
| C04 “sufficiently high price” | The single point is replaced by an analytic family with fixed primitives and every (p\in(1/2,1)), so failure persists as (p\uparrow\beta). |
| C05 uniform upper boundary/planner feasibility | The private proof records (B(1)<0) and the one-crossing derivative argument; the planner proof records cutoff feasibility and globality. |
| C06 “p>c is necessary” | Replaced by the correct claim that strictness is guaranteed on the stated strict domain but need not hold uniformly after relaxing (p>c); a (p=c,s>0) strict boundary example is regression-tested. |
| C07 negative global maxima | Proposition 2 proof now uses interval domination independently of the sign of profit and explicitly covers the interval after the last threshold event. |
| C08 no-booking wording | “No-booking option” is replaced by an available no-reservation plateau/interval; no independent shutdown strategy is added. |
| C09 broken paths | Inventory points to `code/symbolic_derivation.py`, `formal/RingbomShy.lean`, `formal/RingbomShy/Refund.lean`, and `formal/RingbomShy/AxiomAudit.lean`; the nonexistent `formal/README.md` reference is removed. |
| C10 Stage-11 checker omitted | `scripts/run_checks.sh` now executes `code/stage11_hostile_referee.py`. |
| C11 source notation/equation mapping | The manuscript maps (r_H=r_1) and (r_L=r_2) on the ordered domain and labels source equation numbers explicitly. |
| C12 n/ties/domain transition | (n>0) is explicit; the corollary uses membership in the optimal-refund correspondence rather than unique “selection”; the transition from positive endpoint shares to nonnegative global weights is explained. |

## Corollary 1 interpretation

The VOR states that both types are served when price is sufficiently high, the high-type share or high-type show probability is sufficiently low, or the low-type show probability is sufficiently high. The corrected endpoint margin alone is not a complete global-service criterion.

For each comparative-static direction the global conclusion additionally requires:

1. ordered feasible thresholds to remain in the relevant domain;
2. the corrected endpoint comparison to favor (r_L);
3. (r_L) to beat any available zero-profit no-reservation plateau.

The high-price direction receives a direct analytic counterfamily in the manuscript. The other directions are not promoted into four new theorems; doing so would expand a short correction beyond what is needed.

## Verification additions

- Directed exact near-(\beta) regression points were added to `code/corollary_counterexample.py`.
- The boundary case ((\beta,p,c,s)=(1,1/2,1/2,1/4)), with (\bar r=0) and (r^*=1/2), was added to `code/uniform_boundary_audit.py`.
- The Stage-11 independent checker is now part of `scripts/run_checks.sh`.
- Final closure requires a fresh CI run, PDF checksum, page-by-page inspection, and Stage-14 record update.

## Do-not-change commitments

The exact decision-reversal counterexample, corrected endpoint decomposition, endpoint/global distinction, raw-threshold treatment, weak-participation indicator profit, set-valued argmax treatment, limited uniform-survival claim, two Table-1 corrections, limited Lean certificate, one-reference manuscript architecture, and approximately five-page Comment format remain intact.

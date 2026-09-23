# Certification regression: exact zero-show boundary

## Defect found

The first independent correspondence enumerator generalized the source's strict lower bound `σ_L>0` to `σ_L≥0`, but its `β<p` branch then treated all refunds as a zero-profit no-booking plateau. That statement is false at the exact boundary `σ=0,r=1` under weak participation: the consumer is indifferent and reserves.

## Earliest affected gate

Stage 4 / Stage 4A. The source-domain statement remains valid; the defect was in the broadened boundary claim and its independent checker.

## Repair

For `β<p`, all positive-show types stay out. Zero-show types enter only at `r=1`, where each reservation yields `s−c`. The argmax is `{1}` if aggregate endpoint profit is positive, `[0,1]` if zero, and `[0,1)` if negative.

## Evidence and regression

- Corrected analytic case: `derivations/two_type_global_correspondence.md`.
- Corrected primitive-payoff enumerator: `code/independent_correspondence.py`.
- Exact positive/zero/negative endpoint-profit cases are included in `edge_regressions()`.

## Certification regression record

| Missed defect | Earlier checkpoint | Obligation that should have caught it | Repair | Earliest rollback | Permanent regression |
|---|---|---|---|---|---|
| `σ=0, β<p, r=1` tie participation omitted | Initial Stage 4 derivation / Stage 4A edge suite | Boundary/tie correspondence and independent raw-utility enumeration | Explicitly classify zero-show endpoint; add exact sign cases | Stage 4 and 4A | `code/independent_correspondence.py::edge_regressions` |

The affected boundary is outside the publisher's strict two-type parameter domain. It is retained as a fully solved limiting case, not used to strengthen the paper's source-domain claim.

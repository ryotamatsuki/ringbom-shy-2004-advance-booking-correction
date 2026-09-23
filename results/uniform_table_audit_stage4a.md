# Exact audit of the VOR uniform Tables 1–2

## Result

The publisher PDF's Table 1 contains two private-refund entries that do not match equation (14) or the primitive expected-profit optimum. Both entries are in the `p=0.5`, `β=1` row. The corresponding social-refund entries are `1` and are correct. All other Table 1 private/social rates and all Table 2 welfare-loss entries reproduce at the displayed precision.

| Parameters `(β,p,c,s)` | VOR Table 1 private rate | Exact primitive optimum | Bracket at VOR rate | Primitive profit at VOR rate | Primitive profit at optimum | Gain at optimum |
|---|---:|---:|---:|---:|---:|---:|
| `(1,1/2,1/10,1/10)` | `0.250` | `8/13 ≈ 0.615385` | `19/140 > 0` | `11/49` | `169/720` | `361/35280 > 0` |
| `(1,1/2,0,0)` | `0.357` | `2/3 ≈ 0.666667` | `929/6572 > 0` at exact displayed decimal `357/1000` | `732250/2699449` | `9/32` | `863041/86382368 > 0` |

The positive bracket means profit is still increasing at each printed rate. The uniform derivative bracket is strictly decreasing in `r` on `β>p>c≥s≥0`; it has a unique root at the corrected value in each row, so these are not alternative tied optima.

## Primitive derivation and direct calculation

For a uniform show-up type, the participation cutoff and primitive expected seller profit per potential customer are

`h(r)=p(1-r)/(β-rp)`,

`π(r)/n = (p-c-(rp-s))(1-h) + (rp-s)(1-h²)/2`.

Leibniz differentiation gives

`π'(r)/n = p(β-p)/(β-rp)² · [s-c+h(r)(β-s)−(β-p)/2]`.

The factor outside brackets is positive on the active domain. Since `h'(r)<0` and `β-s>0`, the bracket strictly decreases, proving a unique global constrained optimum at its interior zero (or the lower corner if the zero is nonpositive). Solving the bracket equation directly gives the exact roots listed above. The separate exact checker evaluates the integral and the gains using `fractions.Fraction`; it does not import `symbolic_derivation.py`.

## Complete table regression

`python3 code/uniform_table_audit_exact.py` checks the 16 displayed parameter combinations against the publisher's values:

- Table 1 private rates: exactly two discrepancies, listed above.
- Table 1 social rates: zero discrepancies.
- Table 2 welfare-loss values: zero discrepancies.
- The two printed rates are each exactly the matching `p=0.4` row entry in the same cost/salvage column, consistent with a row-copy error. This is a description of the numeric pattern, not a claim about how the error occurred.

Table 2 remains consistent because it matches the primitive optimum, not the erroneous Table 1 rates. The uniform optimum formulas and Propositions 2–4 are unchanged on `β>p>c≥s≥0`; only the two numeric cells are corrected.

## Independent evidence and status

1. **VOR transcription:** the publisher PDF prints `0.250` and `0.357` in the two cells; the source table is on physical PDF page 6 / printed page 5.
2. **Clean-room derivation:** `derivations/uniform_rederivation.md` solves the derivative bracket from the integral, yielding the roots `8/13` and `2/3`.
3. **Direct exact checker:** `code/uniform_table_audit_exact.py` integrates primitive profit and compares each disputed rate with the exact optimum; it also scans all table cells.
4. **Lean target:** `uniform_table1_cost_salvage_tenth_exact` and `uniform_table1_zero_cost_salvage_exact` prove the rational roots, positive derivative brackets at the printed rates, and strict primitive-profit gains.

This finding is separate from the two-type Eq. (6) correction. It was discovered in the source-survival audit and requires the Stage 4A formal CI rerun before the candidate claim set is frozen.

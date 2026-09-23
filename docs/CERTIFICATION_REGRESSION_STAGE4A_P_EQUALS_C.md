# Certification regression: strict welfare inequality at `p=c`

## Defect found

The first uniform-model write-up widened the source's active domain to include `p=c` and then stated the strict Proposition 3 inequality `r*>r̄` throughout that extension. The strict claim is false at `β=1`, `p=c=4/5`, `s=0`: the private and social refunds are both zero, and the private and social participation cutoffs are both `4/5`.

## Earliest affected gate

Stage 1 domain audit and Stage 4 theorem scope. The exact formulas themselves remain defined at this point; the failure is the unqualified strict conclusion.

## Repair

The core preservation theorem uses the source's strict active domain `β>p>c≥s≥0`. The equality point is retained only as a boundary regression. At `p=c` with `s>0`, the strict relation may still hold; the point above is enough to show equality cannot be folded into the strict theorem without further conditions.

## Evidence and regression

- Independent derivation: `derivations/uniform_rederivation.md`.
- Direct exact rational check: `code/uniform_boundary_audit.py`.
- Near-boundary check with `p>c`: same script verifies strict `r*>r̄` at `β=1`, `p=801/1000`, `c=4/5`, `s=0`.

| Missed defect | Earlier checkpoint | Repair | Earliest rollback | Permanent regression |
|---|---|---|---|---|
| `r*=r̄=0` at `p=c,s=0` contradicts a theorem stated with `p≥c` | Initial Stage 1 uniform scope statement | Restrict strict Proposition 3 preservation result to `p>c`; preserve the boundary as an equality case | Stage 1 and Stage 4 | `code/uniform_boundary_audit.py` |

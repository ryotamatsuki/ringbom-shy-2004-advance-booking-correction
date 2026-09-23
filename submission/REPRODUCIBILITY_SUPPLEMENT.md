# Optional Reproducibility / Verification Supplement

This file is the referee-facing map to the reproducibility artifacts. It introduces no new theorem and need not be uploaded unless the editor or portal makes supplemental material useful.

## What can be reproduced

1. The two-type indifference thresholds and primitive seller payoffs.
2. The corrected endpoint-profit difference and missing `1/(1-sigma_L)` factor.
3. The exact rational strict-reversal counterexample.
4. The complete source-model candidate-set / no-booking correspondence under weak participation.
5. Directed feasibility, equality, zero-mass, `sigma=0`, `beta=p`, and no-booking regressions.
6. The uniform-model private optimum on the audited active domain and the two corrected Table-1 values.
7. The proof-critical Lean subset identified in the formal-verification certificate.

## Primary commands

From a clean checkout:

```bash
python3 -m pip install -r requirements.txt
bash scripts/run_checks.sh
bash scripts/build_manuscript.sh
bash scripts/check_pdf.sh
```

For the proof assistant, follow `formal/README.md` and the pinned toolchain files. The formal certificate records exactly what is and is not proved in Lean.

## Independence structure

- Construction path: analytic derivations plus symbolic/exact scripts.
- Stage 4A: separately written primitive-payoff correspondence checker and edge attacks.
- Stage 11: a second hostile-referee implementation (`code/stage11_hostile_referee.py`) that reconstructs utility and cash flows from primitives and does not import the project derivation.
- Formal path: Lean proof of selected algebraic / exact proof-critical claims.

A green proof-assistant build is not presented as proof of unformalized economic primitives, the complete global argmax correspondence, or the full uniform welfare calculus.

## Source handling

The publisher VOR is identified in `sources/source_manifest.md`. It is not redistributed in the repository. The source byte hash remains explicitly unresolved because the publisher byte stream was unavailable to the retrieval path; equations and page locations were checked directly against the publisher-hosted PDF.

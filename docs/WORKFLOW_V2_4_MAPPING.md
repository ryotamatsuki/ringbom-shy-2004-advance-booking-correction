# Scaffold-to-canonical workflow mapping

Checked against `ryotamatsuki/research-paper-workflow` `main`, commit `63f11a50a13d9328213498a5a6576d00b9bceef7` (v2.4), on 2026-09-23.

The starter repository's `docs/WORKFLOW.md` describes a local eight-step correction workflow. It is retained as historical setup documentation; it does not replace or compress canonical gates. Canonical v2.4 controls when requirements differ.

| Local scaffold concept | Canonical v2.4 stage(s) | Application here |
|---|---|---|
| Stage 0 Evidence Freeze | Stage 0 intake + Stage 1 source audit | VOR, provenance, source map, exact transferred discrepancy and prior disclosure are frozen before publication claims. |
| Stage 1 Model Canonicalization | Stage 1 + Stage 4 | Primitive model, strategy set, thresholds, tie convention and feasible domain are transcribed, then reconstructed. |
| Stage 2 Clean-Room Derivation | Stage 4 | Symbolic derivation and direct primitive payoff are distinct evidence paths. |
| Stage 3 Boundary / Global Audit | Stage 4A | Exact candidate correspondence, no-participation intervals, ties, clipping, and boundary parameters are attacked independently. |
| Stage 4 Corrected Result Freeze | Stages 4, 4A, 6, 7, 7.5, 7.5A, 8 | A local freeze is not valid until every canonical upstream gate passes. |
| Stage 5 Downstream Impact | Stage 7 | Two-type screening claims are separated from the continuum/uniform welfare analysis. |
| Stage 6 Independent Recheck | Stages 4A, 7.5A, 11 | Independent enumerator, formal-verification gate, and hostile referee are distinct. |
| Stage 7 Manuscript Construction | Stages 9–10, 13 | Reproducibility is established before the paper is integrated. |
| Stage 8 Novelty / Journal / QA | Stages 2, 6, 11–14 | Novelty is tested before and after theorem construction; journal requirements are live-checked. |

## Mandatory canonical routing retained

`0 → 1 → 2 → 3 → 4 → 4A → 6 → 7 → 7.5 → 7.5A → 8 → 9 → 10 → 11 → 12 → 13 → 14`.

Stage 5 is entered only for one diagnosed repair; Stage 15 is out of scope. Formal verification is embedded at 4A/7.5A and must close as `FORMAL VERIFICATION PASS` or `FORMALIZATION NOT APPLICABLE — REASON RECORDED` before Stage 8. The v2.4 portability and contribution-robustness requirements remain journal-neutral.

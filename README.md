# Ringbom–Shy (2004) Advance Booking Correction

## Target paper

Staffan Ringbom and Oz Shy (2004), “Advance Booking, Cancellations, and Partial Refunds,” Economics Bulletin 13(1), 1–7.

## Project purpose

Re-derive the two-type refund choice, verify the missing 1/(1−σ_L) factor in Proposition 1 / Eq. (6), establish the feasible refund correspondence, and determine the exact impact on the paper’s screening claims.

## Current status

**Stage 0 — Evidence Freeze / independent re-verification.**

No publication-facing correction theorem is frozen yet. The master audit findings are transferred only as hypotheses/evidence to be independently reconstructed in this repository.

## Starting evidence

- Master audit provenance: `ryotamatsuki/ozshypapers — audits/advance_booking_refunds_2004_final.md`
- Source status: Publisher Version of Record directly inspected in the master audit.
- Initial signal: The transferred audit contains an exact active-domain counterexample in which the printed Proposition 1 selects the wrong refund regime.

## Repository policy

1. Re-derive all publication-facing claims from the original model rather than copying the master-audit conclusion.
2. Separate source transcription, derivation, counterexample, corrected theorem, and downstream implications.
3. Treat local FOCs as insufficient when regime changes, clipping, entry/exit, or boundary actions are feasible.
4. Preserve exact equality and boundary cases in the equilibrium correspondence.
5. Numerical and symbolic checks support but do not replace analytical proof.
6. Do not draft a submission claim until the Version-of-Record lineage and prior-disclosure search are frozen.
7. Keep the master audit repository as provenance; this repository becomes canonical only for publication-facing development after Stage 0 passes.

## Planned structure

```text
README.md
PROJECT_STATUS.md
PROVENANCE.md
CLAIM_BOUNDARY.md
EVIDENCE_MAP.md
docs/
  STAGE_00_EVIDENCE_FREEZE.md
derivations/
code/
results/
sources/
manuscript/
submission/
```

## Immediate next step

Complete `docs/STAGE_00_EVIDENCE_FREEZE.md`: freeze the exact source/version, independently reproduce the transferred discrepancy, run a fresh prior-disclosure search, and decide whether the project passes into theorem/proposition development.


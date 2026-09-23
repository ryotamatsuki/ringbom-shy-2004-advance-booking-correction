# Ringbom–Shy (2004) advance-booking correction

This repository contains a clean-room correction of the two-type refund-choice result in Staffan Ringbom and Oz Shy, “Advance Booking, Cancellations, and Partial Refunds,” *Economics Bulletin* 13(1), 1–7 (2004).

## Current research status

The corrected theory is frozen on `research/stage-00-evidence-freeze` at Stage 8. The current manuscript is an anonymous five-page LaTeX correction note. Submission QA is in progress; no journal has received a submission, and `main` has not been changed.

The principal finding is that the printed Proposition 1 / equation (6) omits `1/(1−σ_L)` in the high-type profit-loss term. The branch also records a complete feasible refund correspondence, a corrected reading of Corollary 1, and two private-refund numerical corrections in Table 1. The original paper's uniform welfare results survive on their active domain.

## Reproduce the checks

Requirements: Python 3.12 or newer, `pip install -r requirements.txt`; Lean 4 and mathlib are pinned under `formal/`; LaTeX requires `latexmk` and a TeX Live installation with the recommended LaTeX packages.

```bash
python3 -m pip install -r requirements.txt
bash scripts/run_checks.sh
cd formal && lake build RingbomShy
python3 check_no_placeholders.py
python3 audit_axioms.py
cd ..
bash scripts/build_manuscript.sh
```

The scripts use exact rational arithmetic for the counterexamples and boundary checks. `code/independent_correspondence.py` is a separately written primitive-payoff enumerator; it does not import the symbolic derivation. The manuscript build is source-reproducible; PDF byte-for-byte identity can vary with TeX Live and system font versions.

## Repository map

- `docs/`: canonical v2.4 stage decisions and audit records.
- `derivations/`: source transcription and clean-room derivations.
- `code/`: symbolic, exact-rational, and independent checks.
- `formal/`: pinned Lean 4/mathlib project and formal certificate.
- `manuscript/`: anonymous LaTeX source.
- `output/pdf/anonymous-manuscript.pdf`: clean anonymous build artifact.
- `submission/`: journal-selection and preflight package; no submission action has been taken.
- `sources/source_manifest.md`: VOR identity, provenance, access date, source-page map, and source limitations. The copyrighted PDF is not redistributed.

See `PROJECT_STATUS.md`, `CLAIM_BOUNDARY.md`, and `docs/WORKFLOW_V2_4_MAPPING.md` for the current gate and claim limits.

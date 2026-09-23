# Evidence Map

## Core claim paths

1. Source transcription and equation/page mapping: `derivations/source_transcription.md` and `sources/source_manifest.md`.
2. Exact endpoint algebra: `derivations/two_type_global_correspondence.md`, `code/symbolic_derivation.py`, and `formal/RingbomShy/Refund.lean`.
3. Exact headline counterexample: `code/counterexample_exact.py`, `formal/RingbomShy/Refund.lean`, and the theorem certificate.
4. Independent global correspondence attack: `code/independent_correspondence.py` (800 seeded exact-rational draws plus 21 directed boundary cases).
5. Corollary 1 outside-option example: `code/corollary_counterexample.py`.
6. Uniform boundary and table checks: `code/uniform_boundary_audit.py`, `code/uniform_table_audit_exact.py`, and `results/uniform_table_audit_stage4a.md`.
7. Portability: `code/portability_audit_exact.py` and `docs/STAGE_07_5A_PORTABILITY_CERTIFICATE.md`.
8. Formal proof limits and CI evidence: `formal/FORMAL_VERIFICATION_CERTIFICATE.md` and `docs/STAGE_04A_CERTIFICATION.md`.
9. Final prose: `manuscript/main.tex`; exact source/citation metadata: `sources/source_manifest.md`.

## Reproduction

`bash scripts/run_checks.sh` runs deterministic exact and symbolic checks. Lean build and axiom/placeholder audit run in the formal-verification workflow. The manuscript workflow builds the anonymous PDF from the tracked LaTeX source. Generated caches and LaTeX auxiliaries are excluded; no source-paper PDF is redistributed.

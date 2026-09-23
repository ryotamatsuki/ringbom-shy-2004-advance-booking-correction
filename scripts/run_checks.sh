#!/usr/bin/env bash
set -euo pipefail

python3 -m py_compile code/*.py formal/*.py
python3 code/symbolic_derivation.py
python3 code/counterexample_exact.py
python3 code/independent_correspondence.py
python3 code/stage11_hostile_referee.py
python3 code/corollary_counterexample.py
python3 code/uniform_boundary_audit.py
python3 code/uniform_table_audit_exact.py
python3 code/portability_audit_exact.py
python3 formal/check_no_placeholders.py

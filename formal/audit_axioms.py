from pathlib import Path
import subprocess
import sys

root = Path(__file__).resolve().parent
result = subprocess.run(
    ["lake", "env", "lean", "RingbomShy/AxiomAudit.lean"],
    cwd=root,
    check=False,
    capture_output=True,
    text=True,
)
sys.stdout.write(result.stdout)
sys.stderr.write(result.stderr)
if result.returncode:
    sys.exit(result.returncode)

if "sorryAx" in result.stdout or "admitAx" in result.stdout:
    print("FAIL: placeholder axiom detected in theorem axiom report")
    sys.exit(1)

required = (
    "endpoint_gap_identity",
    "endpoint_weak_choice_iff",
    "endpoint_equality_iff",
    "printed_gap_factor_omission",
    "feasible_endpoint_weak_choice_iff",
    "corrected_gap_exact_regression",
    "exact_regression_feasible",
    "weighted_unit_profit_nonincreasing",
    "fixed_set_profit_nonincreasing",
)
missing = [name for name in required if name not in result.stdout]
if missing:
    print(f"FAIL: missing axiom report(s): {missing}")
    sys.exit(1)

print("PASS: theorem axiom audit contains no sorryAx/admitAx")

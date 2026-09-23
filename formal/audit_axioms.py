from pathlib import Path
import re
import subprocess
import sys

root = Path(__file__).resolve().parent
build = subprocess.run(
    ["lake", "build", "RingbomShy"],
    cwd=root,
    check=False,
    capture_output=True,
    text=True,
)
sys.stdout.write(build.stdout)
sys.stderr.write(build.stderr)
if build.returncode:
    sys.exit(build.returncode)

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

# The ordinary foundations are the only allowed assumptions in these theorem
# certificates. Unexpected axioms, including Lean.ofReduceBool, fail the audit.
allowed_axioms = {"propext", "Classical.choice", "Quot.sound"}
reported_axioms = []
for line in result.stdout.splitlines():
    if "depends on axioms:" not in line:
        continue
    payload = line.split("depends on axioms:", 1)[1].strip()
    names = payload.strip("[] ")
    reported_axioms.extend(name.strip() for name in names.split(",") if name.strip())
unexpected_axioms = sorted(set(reported_axioms) - allowed_axioms)
if unexpected_axioms:
    print(f"FAIL: nonstandard theorem axioms detected: {unexpected_axioms}")
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

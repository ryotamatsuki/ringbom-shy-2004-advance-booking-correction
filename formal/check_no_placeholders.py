from pathlib import Path
import re
import sys

bad = []
for path in Path(__file__).parent.rglob("*.lean"):
    text = path.read_text(encoding="utf-8")
    if re.search(r"\b(sorry|admit)\b", text):
        bad.append(f"placeholder token in {path}")
    if re.search(r"^\s*(?:unsafe\s+)?axiom\b", text, flags=re.MULTILINE):
        bad.append(f"axiom declaration in {path}")

if bad:
    print("\n".join(bad))
    sys.exit(1)
print("PASS: no sorry/admit tokens or axiom declarations in formal sources")

"""Compare transparent rules with an invented probability-threshold baseline."""
import json
from pathlib import Path
from lab1_rules import rule_based, probability_based

ROOT = Path(__file__).resolve().parent
cases = json.loads((ROOT / "inputs" / "core_cases.json").read_text(encoding="utf-8-sig"))["cases"]

print("case | rule-based | probability threshold | disagreement")
for case in cases:
    rule, _ = rule_based(case)
    threshold = probability_based(case)
    print(f"{case['id']} | {rule} | {threshold} | {rule != threshold}")

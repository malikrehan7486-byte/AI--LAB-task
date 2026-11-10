"""Run exactly four core rule tests and print expected, actual, and reason."""
import json
from pathlib import Path
from lab1_rules import rule_based

ROOT = Path(__file__).resolve().parent
cases = json.loads((ROOT / "inputs" / "core_cases.json").read_text(encoding="utf-8-sig"))["cases"]
expected = ["Review", "Hold", "Hold", "Review"]
print("CASE RESULTS (exactly four core cases)")
for case, expected_result in zip(cases, expected):
    actual, reason = rule_based(case)
    inputs = {k: v for k, v in case.items() if k != "id"}
    status = "PASS" if actual == expected_result else "FAIL"
    print(f"\nCase: {case['id']} [{status}]")
    print(f"Input: {inputs}")
    print(f"Expected: {expected_result}")
    print(f"Actual: {actual}")
    print(f"Reason: {reason}")

"""Transparent scholarship screening rules for Lab 1.
All numeric cutoffs are synthetic lab assumptions, not real policy.
"""

SCORE_THRESHOLD = 70
MINIMUM_GPA = 2.5


def rule_based(case):
    """Return (decision, reason); Review means human review, never an award."""
    checks = [
        (case["score"] >= SCORE_THRESHOLD, f"score {case['score']} >= {SCORE_THRESHOLD}"),
        (case["documents_complete"], "all required documents complete"),
        (case["minimum_gpa"] >= MINIMUM_GPA,
         f"minimum_gpa {case['minimum_gpa']} >= {MINIMUM_GPA}"),
        (case["recommendation_received"], "recommendation_received is true"),
    ]
    failed = [description for passed, description in checks if not passed]
    if failed:
        return "Hold", "Failed condition(s): " + "; ".join(failed)
    return "Review", "All four explicit conditions passed; send to a human reviewer."


def probability_based(case):
    """Demonstration threshold only; probability values are invented, not model output."""
    return "Review" if case["probability"] >= 0.70 else "Hold"

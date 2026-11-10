# Lab 1 AI Paradigms and Scholarship Screening

This folder contains the reproducible Lab 1 submission files. `Review` means only that an application is flagged for human review; it is not an award decision. The numeric cutoffs are synthetic lab assumptions and do not represent a university policy.

## Files

- `Lab1_Report.docx` - sourced historical timeline, comparison, rule tests, disagreement table, edge-case analysis, reflection, and responsible-practice notes.
- `lab1_rules.py` - transparent scholarship decision rules and a probability-threshold demonstration.
- `lab1_compare.py` - compares the rule output with the invented probability threshold on the same four inputs.
- `lab1_rules_tests.py` - prints input, expected result, actual result, and reason for exactly four core cases.
- `inputs/core_cases.json` - all reproducible inputs, including invented probability values.
- `traces/` - captured outputs from both scripts.

## Requirements

Python 3.9 or newer. No external packages are required.

## Run

From this `lab1` folder:

```bash
python lab1_rules_tests.py
python lab1_compare.py
```

The probability column is a supplied demonstration value, not a trained or calibrated model. There is no model training and no claim of predictive accuracy.

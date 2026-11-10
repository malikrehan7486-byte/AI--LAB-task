# Lab 2 Intelligent Agents and PEAS

This folder contains a reproducible Lab 2 submission. The classroom program is a simulation: it prints target modes and command/no-command decisions but does not control hardware.

## Files

- `Lab2_Report.docx` - PEAS designs, environment classifications, comparison, complete trace, edge case, reflection, and references.
- `lab2_percepts.py` - stateless reflex baseline from the lab example.
- `lab2_model.py` - stateful classroom agent; remembers the previous target mode and indicates whether a command should be sent.
- `lab2_check.py` - runs the seven supplied percepts and prints the full state-transition trace.
- `inputs/classroom_percepts.json` - reproducible percept sequence.
- `traces/stateful_trace.txt` - captured run output.

## Requirements

Python 3.9 or newer. No external packages are needed.

## Run

From this `lab2` folder:

```bash
python lab2_percepts.py
python lab2_check.py
```

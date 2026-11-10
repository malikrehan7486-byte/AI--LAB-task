# Lab 4 Informed Search and A*

Reproducible Lab 4 submission for heuristic auditing and A* search. The program uses the supplied graph, heuristic, endpoints, and a deterministic priority tie-break: lowest f, then lowest g, then earlier insertion order.

## Files

- `Lab4_Report.docx` - manual frontier calculations, admissibility and consistency checks, A*/UCS comparison, overestimate experiment, and edge-case discussion.
- `lab4_astar_audit.py` - runnable A*, zero-heuristic UCS control, independent path-cost sum, expansion trace, and overestimate experiment.
- `inputs/campus_graph.json` - graph, heuristic, start/goal, and modified heuristic value.
- `traces/lab4_results.txt` - captured run output.

## Run

Python 3.9 or newer; no third-party packages required. From this `lab4` folder:

```bash
python lab4_astar_audit.py
```

Expansion count includes nodes whose successors were examined and excludes the goal; the processed trace includes the goal. A* checks stale queue entries before checking the goal. All graph edge costs are nonnegative.

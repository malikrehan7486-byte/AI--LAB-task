# Lab 3 Uninformed Search

Reproducible Lab 3 files for BFS, DFS, DLS, IDDFS, and UCS. All graph inputs and successor orders are explicit. The weighted graph contains the documented C-G corridor extension; weights are nonnegative travel-cost units.

## Files

- `Lab3_Report.docx` - manual traces, limits, weighted comparison, limitations, reflection, and references.
- `lab3_bfs_dfs.py` - BFS and DFS implementations.
- `lab3_depth_search.py` - DLS and IDDFS with path-local cycle checks and FOUND/CUTOFF/FAILURE statuses.
- `lab3_ucs.py` - UCS using a priority queue.
- `lab3_check.py` - runs all required cases and prints observed paths and orders.
- `inputs/original_graph.json` and `inputs/weighted_graph.json` - reproducible graph definitions.
- `traces/lab3_results.txt` - captured complete output.

## Run

Python 3.9 or newer; no extra packages required. From this `lab3` folder:

```bash
python lab3_check.py
```

Successor order is fixed. BFS/DFS stop when the goal is processed. DLS counts root depth as zero. UCS requires nonnegative edge costs.

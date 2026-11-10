# Lab 5 Adversarial Search

Reproducible implementations of Minimax and alpha-beta pruning for the supplied full binary utility tree.

## Files

- `Lab5_Report.docx` - hand trace, algorithm outputs, leaf-count comparison, ordering experiment, limitations, and reflection.
- `lab5_minimax.py` - Minimax and alpha-beta with terminal-leaf counters, visited leaf order, and pruned subtree log.
- `inputs/game_trees.json` - original score tree and reordered equivalent.
- `traces/lab5_results.txt` - captured program output.

## Assumptions

The six supplied scores are padded with two zeros, as directed in the manual, yielding a complete depth-3 binary tree. Root is MAX; turns alternate MAX/MIN. In the reordered tree, only the two child subtrees of the right MIN node are swapped; utilities are unchanged.

## Run

Python 3.9 or newer; no third-party packages required. From this `lab5` folder:

```bash
python lab5_minimax.py
```

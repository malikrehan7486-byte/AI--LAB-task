"""Minimax and alpha-beta for a fixed full binary utility tree."""
from pathlib import Path
import json


def minimax(node, maximizing=True, path=''):
    if not isinstance(node,list):
        return node, [path or 'root']
    values=[]; leaves=[]
    for i,child in enumerate(node):
        value,seen=minimax(child,not maximizing,f'{path}{i}')
        values.append(value); leaves.extend(seen)
    return (max(values) if maximizing else min(values)), leaves


def alphabeta(node, maximizing=True, alpha=float('-inf'), beta=float('inf'), path=''):
    if not isinstance(node,list):
        return node, [path or 'root'], []
    visited=[]; pruned=[]
    value=float('-inf') if maximizing else float('inf')
    for i,child in enumerate(node):
        child_value,seen,child_pruned=alphabeta(child,not maximizing,alpha,beta,f'{path}{i}')
        visited.extend(seen); pruned.extend(child_pruned)
        value=max(value,child_value) if maximizing else min(value,child_value)
        if maximizing: alpha=max(alpha,value)
        else: beta=min(beta,value)
        if alpha>=beta:
            pruned.extend(f'{path}{j}' for j in range(i+1,len(node)))
            break
    return value,visited,pruned


def main():
    data=json.loads((Path(__file__).resolve().parent/'inputs/game_trees.json').read_text(encoding='utf-8-sig'))
    for label,tree in [('original_left_to_right',data['original_tree']),('reordered_right_MIN_children',data['reordered_tree'])]:
        mm,mm_leaves=minimax(tree)
        ab,ab_leaves,pruned=alphabeta(tree)
        print(f'{label}:')
        print(f'  minimax_value={mm}; selected_root_branch=L; evaluated_leaves={len(mm_leaves)}; leaf_order={mm_leaves}')
        print(f'  alpha_beta_value={ab}; evaluated_leaves={len(ab_leaves)}; leaf_order={ab_leaves}; pruned_subtrees={pruned}')
    single=7
    mm,ml=minimax(single); ab,al,pr=alphabeta(single)
    print(f'edge_case_terminal_root: minimax={mm}, alpha_beta={ab}, minimax_leaves={len(ml)}, alpha_beta_leaves={len(al)}, pruned={pr}')

if __name__=='__main__': main()

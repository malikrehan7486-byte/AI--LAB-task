"""Uninformed BFS and DFS with reproducible expansion traces."""
from collections import deque

def bfs(graph, start, goal):
    q=deque([(start,[start])]); seen={start}; order=[]
    while q:
        node,path=q.popleft(); order.append(node)
        if node==goal: return path,order
        for n in graph.get(node,[]):
            if n not in seen:
                seen.add(n); q.append((n,path+[n]))
    return None,order

def dfs(graph, start, goal):
    stack=[(start,[start])]; seen=set(); order=[]
    while stack:
        node,path=stack.pop()
        if node in seen: continue
        seen.add(node); order.append(node)
        if node==goal: return path,order
        for n in reversed(graph.get(node,[])):
            if n not in seen: stack.append((n,path+[n]))
    return None,order

if __name__=='__main__':
    import json
    from pathlib import Path
    p=Path(__file__).resolve().parent
    d=json.loads((p/'inputs/original_graph.json').read_text(encoding='utf-8-sig'))
    g=d['successors']
    for name,fn in [('BFS',bfs),('DFS',dfs)]:
        path,order=fn(g,d['start'],d['goal']); print(f'{name}: path={path}; processed={order}')

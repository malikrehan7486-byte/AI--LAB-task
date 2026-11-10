"""Run required search cases and print the complete reproducible results."""
import json
from pathlib import Path
from lab3_bfs_dfs import bfs,dfs
from lab3_depth_search import dls,iddfs
from lab3_ucs import ucs
ROOT=Path(__file__).resolve().parent
orig=json.loads((ROOT/'inputs/original_graph.json').read_text(encoding='utf-8-sig'))
g=orig['successors']; start=orig['start']; goal=orig['goal']
print('ORIGINAL A-G GRAPH')
for name,fn in [('BFS',bfs),('DFS',dfs)]:
 path,order=fn(g,start,goal); print(f'{name} path={path}; processed={order}')
print('DLS LIMITS')
for limit in [1,2,3,4]:
 status,path,order=dls(g,start,goal,limit); print(f'limit={limit}; status={status}; path={path}; processed={order}')
print('IDDFS MAXIMUM DEPTHS')
for maximum in [1,2,3,4]:
 status,path,attempts,order=iddfs(g,start,goal,maximum); print(f'max_depth={maximum}; status={status}; path={path}; attempted={attempts}; processed={order}')
weighted=json.loads((ROOT/'inputs/weighted_graph.json').read_text(encoding='utf-8-sig'))
wg={}
for a,b,w in weighted['edges']: wg.setdefault(a,[]).append((b,w)); wg.setdefault(b,[])
# BFS on the same extended topology (weights ignored).
ug={a:[b for b,_ in es] for a,es in wg.items()}
bpath,bo=bfs(ug,weighted['start'],weighted['goal']); bcost=sum(next(w for b,w in wg[a] if b==z) for a,z in zip(bpath,bpath[1:]))
upath,ucost,uorder=ucs(wg,weighted['start'],weighted['goal'])
verify=sum(next(w for b,w in wg[a] if b==z) for a,z in zip(upath,upath[1:]))
print('WEIGHTED EXTENSION')
print(f'edges={weighted["edges"]}')
print(f'BFS path={bpath}; hops={len(bpath)-1}; cost={bcost}; processed={bo}')
print(f'UCS path={upath}; cost={ucost}; independently_summed={verify}; processed={uorder}')
print('EDGE CASES')
print('start_equals_goal:',dls(g,'A','A',0)[:2],'; IDDFS max_depth=0:',iddfs(g,'A','A',0)[:3])
print('unreachable_goal_Z:',dls(g,'A','Z',4)[:2])
cycle={'S':['A'],'A':['S','G'],'G':[]}
print('cycle_graph_S_to_G:',dls(cycle,'S','G',3)[:2],'; path-local cycle check prevents revisiting S')

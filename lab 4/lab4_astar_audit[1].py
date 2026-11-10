"""A* heuristic audit, UCS control, and overestimate experiment."""
import heapq, json
from itertools import count
from pathlib import Path

ROOT=Path(__file__).resolve().parent

def search(graph, heuristic, start, goal):
    serial=count()
    frontier=[(heuristic.get(start,0),0,next(serial),start,[start])]
    best={start:0}; processed=[]; expanded=[]; snapshots=[]; stale=[]
    while frontier:
        f,g,_,node,path=heapq.heappop(frontier)
        if g != best.get(node):
            stale.append((node,g,best.get(node)))
            continue
        processed.append((node,g,heuristic.get(node,0),f))
        if node==goal:
            return {'path':path,'cost':g,'processed':processed,'expanded':expanded,'snapshots':snapshots,'stale':stale}
        expanded.append(node)
        for nxt,w in graph.get(node,[]):
            ng=g+w
            if ng < best.get(nxt,float('inf')):
                best[nxt]=ng
                nh=heuristic.get(nxt,0)
                heapq.heappush(frontier,(ng+nh,ng,next(serial),nxt,path+[nxt]))
        live=[(x[0],x[1],x[3]) for x in frontier if x[1]==best.get(x[3])]
        snapshots.append((node,sorted(live)))
    return {'path':None,'cost':None,'processed':processed,'expanded':expanded,'snapshots':snapshots,'stale':stale}

def path_cost(graph,path):
    if not path:return None
    total=0
    for u,v in zip(path,path[1:]):
        total+=next(w for n,w in graph[u] if n==v)
    return total

def run():
    data=json.loads((ROOT/'inputs/campus_graph.json').read_text(encoding='utf-8-sig'))
    graph=data['graph']; start=data['start']; goal=data['goal']; h=data['heuristic']
    astar=search(graph,h,start,goal)
    ucs=search(graph,{n:0 for n in graph},start,goal)
    bad=dict(h); bad[data['overestimate']['node']]=data['overestimate']['modified']
    over=search(graph,bad,start,goal)
    true={'S':6,'A':5,'B':5,'C':3,'G':0}
    print('HEURISTIC AUDIT')
    for n in ['S','A','B','C','G']:
        print(f'{n}: h={h[n]}, true_remaining={true[n]}, admissible={h[n] <= true[n]}')
    print('Consistency edges:')
    for u,edges in graph.items():
        for v,w in edges:
            print(f'{u}->{v}: {h[u]} <= {w}+{h[v]} = {w+h[v]} : {h[u] <= w+h[v]}')
    print('\nMANUAL FRONTIER SNAPSHOTS (A* with supplied h)')
    for i,(node,fr) in enumerate(astar['snapshots'][:3],1):
        before=astar['processed'][i-1]
        print(f'expansion {i}: selected {node} (g={before[1]}, h={before[2]}, f={before[3]}); frontier after={fr}')
    print('\nA* SUPPLIED HEURISTIC')
    for name,res in [('A*',astar),('UCS h=0',ucs)]:
        print(f'{name}: path={res["path"]}; returned_cost={res["cost"]}; independently_summed={path_cost(graph,res["path"])}; processed={res["processed"]}; expanded={res["expanded"]}; expansion_count={len(res["expanded"])}; stale_ignored={res["stale"]}')
    print('\nOVERESTIMATE h(C)=10')
    print(f'original h(C)=2; modified h(C)=10; true_remaining(C)=3')
    print(f'path={over["path"]}; returned_cost={over["cost"]}; independently_summed={path_cost(graph,over["path"])}; processed={over["processed"]}; expanded={over["expanded"]}; expansion_count={len(over["expanded"])}')
    print('\nEDGE CASE start=goal')
    edge=search(graph,h,'S','S')
    print(f'path={edge["path"]}; cost={edge["cost"]}; processed={edge["processed"]}; expanded={edge["expanded"]}')
if __name__=='__main__': run()

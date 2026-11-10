"""Uniform-cost search on a nonnegative weighted graph."""
import heapq
from itertools import count

def ucs(graph,start,goal):
    serial=count(); frontier=[(0,next(serial),start,[start])]; best={start:0}; order=[]
    while frontier:
        cost,_,node,path=heapq.heappop(frontier)
        if cost!=best.get(node): continue
        order.append((node,cost))
        if node==goal: return path,cost,order
        for nxt,weight in graph.get(node,[]):
            new_cost=cost+weight
            if nxt not in best or new_cost<best[nxt]:
                best[nxt]=new_cost; heapq.heappush(frontier,(new_cost,next(serial),nxt,path+[nxt]))
    return None,None,order

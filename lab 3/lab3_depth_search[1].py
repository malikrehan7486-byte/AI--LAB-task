"""Depth-limited and iterative-deepening DFS with path-local cycle checks."""

def dls(graph,start,goal,limit):
    order=[]
    def visit(node,path,depth):
        order.append(node)
        if node==goal: return 'FOUND',path
        successors=[n for n in graph.get(node,[]) if n not in path]
        if depth==limit:
            return ('CUTOFF',None) if successors else ('FAILURE',None)
        cutoff=False
        for n in successors:
            status,result=visit(n,path+[n],depth+1)
            if status=='FOUND': return status,result
            if status=='CUTOFF': cutoff=True
        return ('CUTOFF',None) if cutoff else ('FAILURE',None)
    status,path=dls_result=visit(start,[start],0)
    return status,path,order

def iddfs(graph,start,goal,max_depth):
    attempts=[]; all_order=[]
    for limit in range(max_depth+1):
        attempts.append(limit); status,path,order=dls(graph,start,goal,limit); all_order.extend(order)
        if status=='FOUND': return status,path,attempts,all_order
        if status=='FAILURE': return status,None,attempts,all_order
    return 'CUTOFF',None,attempts,all_order

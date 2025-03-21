from collections import deque
def bfs(g,s):
    v,q=set(),deque([s])
    while q:
        n=q.popleft()
        if n not in v:
            print(n,end="");v.add(n);q.extend(g[n])
bfs({0:[1,2],1:[2],2:[0,3],3:[3]},2)
            

from collections import deque

moi = lambda: map(int, input().split())
n,m = moi()
indegree = [0] * (n+1)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = moi()
    graph[a].append(b)
    indegree[b]+=1

q = deque()

for i in range(1,n+1):
    if not indegree[i]:
        q.append(i)

def bfs():
    while q:
        x = q.popleft()
        print(x, end = " ")
        for nx in graph[x]:
            if indegree[nx]:
                indegree[nx]-=1
                if not indegree[nx]:
                    q.append(nx)
bfs()

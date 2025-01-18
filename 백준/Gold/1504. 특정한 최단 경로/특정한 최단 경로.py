from collections import deque
n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])
v1,v2 = map(int, input().split())
inf = int(1e10)
def bfs(x):
    q = deque()
    q.append([x,0])
    vis = [inf] * (n+1)
    vis[x] = 0
    while q:
        node, cost = q.popleft()
        for next, dist in graph[node]:
            cal = cost + dist
            if vis[next] > cal:
                q.append([next, cal])
                vis[next] = cal
    return vis
origin = bfs(1)
v1_dist = bfs(v1)
v2_dsit = bfs(v2)

res1 =  origin[v1] + v1_dist[v2] + v2_dsit[n]
res2 =  origin[v2] + v2_dsit[v1] + v1_dist[n]
res = min(res1, res2)
if res >= inf:
    print(-1)
else:
    print(res)
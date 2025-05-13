from collections import deque
n = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a,b,c = map(int, input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])


def bfs(x):
    visit = [-1] * (n+1)
    q = deque()
    visit[x] = 0
    q.append(x)
    while q:
        x = q.popleft()
        for nx, ndist in graph[x]:
            if visit[nx] == -1:
                ncost = ndist+visit[x]
                visit[nx] = ncost
                q.append(nx)
    return visit
dist = bfs(1)
a = dist.index(max(dist))
dist2 = bfs(a)
b = dist2.index(max(dist2))
dist3 = bfs(b)

for i in range(1, n+1):
    print(max(dist2[i], dist3[i]))
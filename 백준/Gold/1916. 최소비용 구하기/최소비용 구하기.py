import heapq
import sys
inf = sys.maxsize
n = int(input())
m = int(input())
graph = [[] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
s,e = map(int, input().split())
def dijk(s, e):
    visit = [inf] * (n+1)
    q = []
    visit[s] = 0
    heapq.heappush(q, [0, s])
    while q:
        cost, node = heapq.heappop(q)
        if visit[node] < cost:
            continue
        for nx, dist in graph[node]:
            cal = dist + cost
            if visit[nx] > cal:
                visit[nx] = cal
                heapq.heappush(q, [cal, nx])
    return visit[e]

print(dijk(s,e))
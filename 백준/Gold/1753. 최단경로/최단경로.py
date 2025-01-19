import heapq
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
s = int(input())
graph = [[] for _ in range(n+1)]
inf = sys.maxsize
visit = [inf] * (n+1)
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    visit[start] = 0
    heapq.heappush(q,(0, start))
    while q:
        cost, node = heapq.heappop(q)
        if visit[node] < cost:
            continue
        for nx, dist in graph[node]:
            cal  =cost + dist
            if visit[nx] > cal:
                visit[nx] = cal
                heapq.heappush(q, (cal, nx))
dijkstra(s)
for i in range(1, n+1):
    if visit[i] == inf:
        print("INF")
    else:
        print(visit[i])
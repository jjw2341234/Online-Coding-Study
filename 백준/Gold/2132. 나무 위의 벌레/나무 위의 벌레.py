import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    dist = [-1] * (N+1)
    dist[start] = fruits[start]
    q = deque([start])
    max_node = start

    while q:
        now = q.popleft()
        for nxt in graph[now]:
            if dist[nxt] == -1:
                dist[nxt] = dist[now] + fruits[nxt]
                q.append(nxt)
                if dist[nxt] > dist[max_node]:
                    max_node = nxt
                elif dist[nxt] == dist[max_node]:
                    max_node = min(max_node, nxt)
    return max_node, dist

N = int(input())
fruits = [0] + list(map(int, input().split()))
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

if N == 1:
    print(fruits[1], 1)
else:
    A, _ = bfs(1)          # 지름의 한 끝 A
    B, dist = bfs(A)       # 지름의 다른 끝 B 및 거리 정보

    print(dist[B], min(A, B))

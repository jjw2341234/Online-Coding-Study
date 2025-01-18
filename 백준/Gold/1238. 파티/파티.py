import heapq
n,m,x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append([b,c])

def bfs(start, end):
    q = [[0, start]]
    visit = [int(1e10)] * (n+1)
    visit[start] = 0
    while q:
        cost, node = heapq.heappop(q)
        if visit[node] < cost:
            continue
        for next, dist in graph[node]:
            cal = dist + cost
            if visit[next] > cal:
                visit[next] = cal
                heapq.heappush(q, [cal, next])
    return visit[end]
result = 0
for i in range(1, n+1):
    if i == x: continue
    go = bfs(i, x)
    back = bfs(x, i)
    result = max(result, go + back)
print(result)
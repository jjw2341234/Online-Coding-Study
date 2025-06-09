import heapq
moi = lambda: map(int, input().split())
def prim(x):
    res = 0
    q = []
    heapq.heappush(q, (0, x))
    visit = [False] * n
    while q:
        cost, node = heapq.heappop(q)
        if visit[node]:
            continue
        res+= cost
        visit[node] = True
        for nxt_cost, nxt_node in graph[node]:
            if not visit[nxt_node]:
                heapq.heappush(q, (nxt_cost, nxt_node))
    return res


while True:
    n,m = moi()
    if n == 0 and m == 0:
        break
    total_cost = 0
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u,v,c = moi()
        graph[u].append((c,v))
        graph[v].append((c,u))
        total_cost += c
    print(total_cost - prim(0))
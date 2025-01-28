import heapq
n = int(input())
inf  = int(1e9)
graph = [[] for _ in range(n+1)]
t = int(input())
for _ in range(t):
    a,b,c = map(int, input().split())
    graph[a].append([b,c])
s,e = map(int, input().split())
dp = [[inf, [i]] for i in range(n+1)]

def dijkstra(x):
    dp[x][0] = 0
    heap = [[0, x]]
    while heap:
        cost, node = heapq.heappop(heap)
        if dp[node][0] < cost:
            continue
        for t,v in graph[node]:
            new_cost = v + cost
            if dp[t][0] > new_cost:
                dp[t][0] = new_cost
                dp[t][1] = dp[node][1] + [t]
                heapq.heappush(heap, [new_cost, t])
dijkstra(s)
print(dp[e][0])
print(len(dp[e][1]))
print(*dp[e][1])
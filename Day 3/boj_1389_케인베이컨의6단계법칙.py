import heapq
n,m = map(int, input().split())
graph = [[] for i in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append((1, b))
    graph[b].append((1, a))
res = 0

def nearest(s):
    visit = [int(1e10) for i in range(n+1)]
    min_heap = [(0, s)]
    while min_heap:
        cost, node = heapq.heappop(min_heap)
        for dist, nnode in graph[node]:
            dist+= cost
            if dist < visit[nnode]:
                visit[nnode] = dist
                heapq.heappush(min_heap, (dist, nnode))
    return sum(visit[1:])

res= 10000000
id = 100000000
for i in range(1, n+1):
    if res > nearest(i):
        res = nearest(i)
        id = i
print(id)
import heapq
s,e = map(int, input().split())
inf = int(1e6)
visit=  [inf] * (100001)
visit[s] = 0
q = []
heapq.heappush(q, (0, s))
while q:
    dist, node = heapq.heappop(q)
    if visit[node] < dist:
        continue

    for n in [node+1, node-1, 2*node]:
        if n < 0 or n >=100001:
            continue
        cost = dist
        if n != node*2:
            cost+=1
        if cost < visit[n]:
            visit[n] = cost
            heapq.heappush(q, (cost, n))
print(visit[e])
from collections import deque
n = int(input())
graph = [[] for i in range(n+1)]
for _ in range(n-1):
    a,b,c  = map(int, input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])

def bfs(x):
    q = deque()
    q.append([x, 0])
    visit = [-1]*(n+1)
    visit[x] = 0
    while q:
        node, dist = q.popleft()
        for adj_node, adj_dist in graph[node]:
            if visit[adj_node] == -1:
                cal_dist = dist + adj_dist
                q.append([adj_node, cal_dist])
                visit[adj_node] = cal_dist
    res = max(visit)
    return visit.index(res), res
print(bfs(bfs(1)[0])[1])
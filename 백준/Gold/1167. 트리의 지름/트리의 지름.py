from collections import deque
n = int(input())
graph = [[] for i in range(n+1)]
for _ in range(n):
    arr  = list(map(int, input().split()))
    a = arr[0]
    b = arr[1:]
    b.pop(-1)
    for i in range(0,len(b), 2):
        graph[a].append([b[i], b[i+1]])

def bfs(x):
    q = deque()
    q.append([x, 0])
    visit = [-1]*(n+1)
    visit[x] = 0
    res= [0,0]
    while q:
        node, dist = q.popleft()
        for adj_node, adj_dist in graph[node]:
            if visit[adj_node] == -1:
                cal_dist = dist + adj_dist
                q.append([adj_node, cal_dist])
                visit[adj_node] = cal_dist
                if res[1] < cal_dist:
                    res[0] = adj_node
                    res[1] = cal_dist
    return res
point, _ = bfs(1)
print(bfs(point)[1])
n, m = map(int, input().split())
inf = int(1e9)
graph = [[inf] *n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == j:
            graph[i][j] = 0

for _ in range(m):
    a,b = map(int, input().split())
    graph[a-1][b-1] = 1
    graph[b-1][a-1] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

res = inf * 10
index = 0
for ind in range(len(graph)):
    if sum(graph[ind]) < res:
        res = sum(graph[ind])
        index = ind+1

print(index)
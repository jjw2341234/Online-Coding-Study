n,m = map(int, input().split())

graph = [[int(1e9)] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    graph[i][i] = 0

for _ in range(m):
    a,b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


res = int(1e9)
result = []
for i in range(1, n):
    for j in range(2, n+1):
        tmp = 0
        for k in range(1, n+1):
            tmp += min(graph[i][k], graph[j][k]) * 2
        if tmp < res:
            res = tmp
            result = [i,j,res]
print(*result)
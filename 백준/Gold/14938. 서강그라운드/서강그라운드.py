n,m,r = map(int, input().split())
area = list(map(int,input().split()))
INF=1e9
graph = [[INF] * (n+1) for _ in range(n+1)]
for _ in range(r):
    a,b,c = map(int, input().split())
    graph[a][b],graph[b][a]=c,c
for i in range(1, n+1):
    graph[i][i] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
res = 0
for i in range(1, n+1):
    s = 0
    for j in range(1, n+1):
        if graph[i][j] <= m:
            s+= area[j-1]
    res = max(s, res)
print(res)
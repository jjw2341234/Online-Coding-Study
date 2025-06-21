t = int(input())
moi = lambda: map(int, input().split())

def dfs(x):
    visit[x] = 1
    dynamite = 0
    for nx, ncost in graph[x]:
        if not visit[nx]:
            dynamite+= min(ncost ,dfs(nx))
    return dynamite if dynamite else int(1e9)

for _ in range(t):
    n,m = moi()
    if n == 1:
        print(0)
    else:
        graph = [[] for _ in range(n+1)]
        visit = [0] * (n+1)
        for _ in range(m):
            a,b,c = moi()
            graph[a].append((b,c))
            graph[b].append((a,c))
        print(dfs(1))

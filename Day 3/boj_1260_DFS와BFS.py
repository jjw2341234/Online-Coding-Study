from collections import deque
n,m,s = map(int, input().split())
graph = [[0] * (n+1) for i in range(n+1)]
visit = [0] * (n+1)
visit[s] = 1
visit2 = [0] * (n+1)
visit2[s] = 1

for _ in range(m):
    a,b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
def dfs(s):
    print(s, end = " ")
    for i in range(1, n+1):
        if graph[s][i] and not visit[i]:
            visit[i] = 1
            dfs(i)
dfs(s)
print()
def bfs(s):
    q = deque()
    q.append(s)
    visit2[s] = 1
    while q:
        x = q.popleft()
        print(x, end = " ")
        for i in range(1, n+1):
            if graph[x][i] and not visit2[i]:
                visit2[i] = 1
                q.append(i)
bfs(s)
n = int(input())
graph = [[] for _ in range(n+1)]

visit = [0] * (n+1)

for _ in range(n-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dp = [[0] * (2) for _ in range(n+1)]

def dfs(x):
    dp[x][1] = 1
    visit[x] = 1

    for i in graph[x]:
        if not visit[i]:
            dfs(i)
            dp[x][0]+= max(dp[i])
            dp[x][1]+=dp[i][0]
dfs(1)
print(max(dp[1]))
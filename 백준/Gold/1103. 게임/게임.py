n,m = map(int, input().split())

arr = [list(input().rstrip()) for _ in range(n)]

visit = [[0] * m for _ in range(n)]
dp = [row[:] for row in visit]

def dfs(x,y):
    if visit[x][y]:
        print(-1)
        exit(0)
    if dp[x][y]:
        return dp[x][y]
    val = 1
    visit[x][y] = 1
    k = int(arr[x][y])
    for dx, dy in ([1,0], [-1,0], [0,1], [0,-1]):
        nx = x + k*dx
        ny = y + k*dy
        if 0<=nx<n and 0<=ny<m and arr[nx][ny]!='H':
            val = max(val, dfs(nx, ny) + 1)
    visit[x][y] = 0
    dp[x][y] = val
    return dp[x][y]

print(dfs(0,0))
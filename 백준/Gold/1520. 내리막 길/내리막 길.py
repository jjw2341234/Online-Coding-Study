import sys
sys.setrecursionlimit(10**6)


n,m = map(int, input().split())
arr  = [list(map(int, input().split())) for _ in range(n)]
dir = [(0,1), (0,-1), (1,0), (-1,0)]
def check(x,y):
    if 0<=x<n and 0<=y<m:
        return True
    else:
        return False

dp = [[-1] * m for _ in range(n)]

def dfs(x,y):
    global res
    if x == n-1 and y == m-1:
        return 1
    
    if dp[x][y] != -1:
        return dp[x][y]
    dp[x][y] = 0

    for i in range(4):
        nx = x+dir[i][0]
        ny = y+dir[i][1]
        if check(nx, ny) and arr[x][y] > arr[nx][ny]:
            dp[x][y] += dfs(nx, ny)
    
    return dp[x][y]

print(dfs(0,0))
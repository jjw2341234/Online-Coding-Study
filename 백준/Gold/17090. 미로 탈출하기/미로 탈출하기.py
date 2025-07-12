import sys
input = sys.stdin.readline
sys.setrecursionlimit(600000)

def move(i, j):
    if i < 0 or i >= n or j < 0 or j >= m:
        return 1  

    if dp[i][j] != -1:
        return dp[i][j]  

    if visited[i][j]:  
        return 0       

    visited[i][j] = True  

    ni, nj = i, j
    if g[i][j] == "D":
        ni += 1
    elif g[i][j] == "U":
        ni -= 1
    elif g[i][j] == "L":
        nj -= 1
    elif g[i][j] == "R":
        nj += 1

    dp[i][j] = move(ni, nj)

    visited[i][j] = False  

    return dp[i][j]

n, m = map(int, input().split())
g = [list(input().strip()) for _ in range(n)]

dp = [[-1] * m for _ in range(n)]        
visited = [[False] * m for _ in range(n)]  

ans = 0
for i in range(n):
    for j in range(m):
        if move(i, j) == 1:
            ans += 1

print(ans)

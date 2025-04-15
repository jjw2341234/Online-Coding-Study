moi = lambda: map(int, input().split())

n,m = moi()

grid = [list(input().rstrip()) for _ in range(n)]

dp = [0] * (n+1)

dp[n] = 1

for j in range(m):
    small = 0
    tmp = [0] * (n+1)
    for i in range(n):
        if grid[i][j] == 'B':
            small = i+1

    big = n
    for i in range(n-1, -1, -1):
        if grid[i][j] == 'R':
            big = i
    
    for i in range(n, -1, -1):
        if i < n:
            dp[i]+= dp[i+1]
        if small <= i <= big:
            tmp[i] = dp[i]

    dp = tmp
print(sum(dp))

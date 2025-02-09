n, m= map(int, input().split())
arr = [[0,0]] + [list(map(int, input().split())) for _ in range(m)]
dp = [[0] * (n+1) for _ in range(m+1)]
for i in range(1,m+1):
    for j in range(1,n+1):
        if arr[i][1] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j - arr[i][1]] + arr[i][0], dp[i-1][j])
print(dp[m][n])
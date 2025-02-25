n,m = map(int, input().split())

#일단 n이 타겟이다.

dp = [[0] * (201) for _ in range(201)]

for i in range(1, n+1):
    dp[1][i] = 1

for i in range(1, m+1):
    dp[i][1] = i
    for j in range(1, n+1):
        dp[i][j] = max(dp[i][j], dp[i-1][j] + dp[i][j-1]) % 1000000000

print(dp[m][n])
n,w  = map(int, input().split())
bag = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * (w+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1,w+1):
        size, weight = bag[i-1]
        if j >= size:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-size] + weight)
        else:
            dp[i][j] = dp[i-1][j]
print(dp[-1][-1])
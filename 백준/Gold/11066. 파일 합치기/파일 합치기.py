t   = int(input())
for  _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    dp = [[0] *n for _ in range(n)]
    for i in range(n-1):
        dp[i][i+1] = arr[i] + arr[i+1]
        for j in range(i+2, n):
            dp[i][j] = dp[i][j-1] + arr[j]
    
    for v in range(2, n):
        for i in range(n-v):
            j = i+v
            dp[i][j] += min([dp[i][k] + dp[k+1][j] for k in range(i,j)])
    print(dp[0][n-1])

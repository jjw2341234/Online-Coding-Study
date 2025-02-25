n = int(input())

if n == 1:
    print(0)
else:
    dp = [0] * (n+1)
    dp[2] = 3
    for i in range(4, n+1, 2):
        dp[i] = 3*dp[i-2] + 2
        for j in range(2, i-2, 2):
            dp[i] += 2*dp[j]
    print(dp[n])
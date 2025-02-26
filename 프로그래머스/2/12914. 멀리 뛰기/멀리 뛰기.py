def solution(n):
    answer = 0
    dp = [0] * (n+1)
    dp[1] = 1
    if n == 1:
        return 1
    dp[2] = 2
    if n == 2:
        return 2
    dp[3] = 3
    if n == 3:
        return 3
    else:
        for i in range(4,n+1):
            dp[i] = (dp[i-1]+ dp[i-2]) % 1234567
        return dp[n]
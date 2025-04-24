n = int(input())
MOD = 10**9

dp = [0] * (n + 1)
dp[1] = 0
if n >= 2:
    dp[2] = 1

for i in range(3, n + 1):
    dp[i] = (dp[i - 1] + dp[i - 2]) * (i - 1) % MOD

print(dp[n])

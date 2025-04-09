import sys
input = sys.stdin.readline

MOD = int(1e9 + 7)
dp = [0] * 191230
dp[0] = 1
dp[1] = 1

for i in range(2, 191230):
    dp[i] = (dp[i - 1] + dp[i - 2]) % MOD

t = int(input())
for _ in range(t):
    a = int(input())
    print(dp[a])

import sys
input = sys.stdin.readline
n = int(input())
dp = [0] * n
for i in range(n):
    a,b = map(int, input().split())
    if i:dp[i] = max(dp[i-1], dp[i])
    if i + a <= n:dp[i+a-1] = max(dp[i+a-1], dp[i-1] + b)
print(dp[-1])
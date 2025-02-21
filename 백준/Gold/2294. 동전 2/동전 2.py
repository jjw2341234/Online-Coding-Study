n,m = map(int, input().split())
arr = list()
for _ in range(n):
    a = int(input())
    arr.append(a)

dp = [int(1e9)] * (m+1)
dp[0] = 0
for cost in arr:
    for i in range(cost, m+1):
        dp[i] = min(dp[i], dp[i-cost] + 1)
if dp[m] == int(1e9):
    print(-1)
else:
    print(dp[m])
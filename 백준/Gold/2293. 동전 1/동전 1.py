n, m = map(int, input().split())
arr = []
for _ in range(n):
    a = int(input())
    arr.append(a)
dp = [0] * (m+1)
dp[0] =1 
for cost in arr:
    for i in range(cost, m+1):
        dp[i] = dp[i] + dp[i-cost]
print(dp[m])
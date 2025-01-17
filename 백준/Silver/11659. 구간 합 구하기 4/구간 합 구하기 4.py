n,m = map(int, input().split())
arr = list(map(int, input().split()))
dp = arr
for i in range(1, n):
    dp[i] = dp[i-1] + arr[i]
for _ in range(m):
    a,b = map(int, input().split())
    a-=1
    b-=1
    if a == 0:
        print(dp[b])
    else:
        print(dp[b] - dp[a-1])

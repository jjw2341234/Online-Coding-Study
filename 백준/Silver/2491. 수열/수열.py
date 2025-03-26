n = int(input())

moi = lambda : map(int, input().split())

arr = list(moi())

dp = [1] * (n)
dp2 = [1] * (n)

for  i in range(1, n):
    if arr[i-1] <= arr[i]:
        dp[i]+= dp[i-1]

for i in range(n-1, 0, -1):
    if arr[i-1] >= arr[i]:
        dp2[i-1]+= dp2[i]

max_dp1, max_dp2 = max(dp), max(dp2)

print(max(max_dp1, max_dp2))

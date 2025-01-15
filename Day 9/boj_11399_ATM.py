n = int(input())
arr = list(map(int, input().split()))
arr.sort()
dp = arr
for i in range(1,n):
    dp[i]+= dp[i-1]
result = sum(dp)
print(result)
n = int(input())
dp = [0] * (100000)
cur = 0
arr = []
for _ in range(n):
    a,b,c = map(int, input().split())
    arr.append((b,a,c))
arr.sort()
end_time = [a[0] for a in arr]
dp = [0] * (n+1)

for i in range(1, n+1):
    e,s,p = arr[i-1]
    dp[i] = dp[i-1]
    start, end = 0, n
    while start<=end:
        mid = (start + end)//2
        if end_time[mid]<= s:
            start = mid+1
        else:
            end = mid-1
    dp[i] = max(dp[i], dp[start] + p)
print(dp[-1])

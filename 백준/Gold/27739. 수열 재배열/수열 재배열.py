import sys
input = sys.stdin.readline

def lis(ar):
    dp = [1] * n
    for j in range(1, n):
        if ar[j-1] < ar[j]:
            dp[j] = dp[j-1] + 1
    return max(dp)

n,m = map(int, input().split())
arr = list(map(int, input().split()))
res = 0
for i in range(n-m+1):
    sub = arr[i:i+m]
    sub1 = sorted(sub)
    tmp  = arr[:i] + sub1 + arr[i+m:]
    temp = []
    temp2 = []
    for s in sub1:
        if i-1 >= 0 and s < arr[i-1]:
            temp2.append(s)
        else:
            temp.append(s)
    tmp2 = arr[:i] + temp + temp2 + arr[i+m:]
    temp = []
    temp2 = []
    for s in sub1:
        if i+m < n and s <arr[i+m]:
            temp2.append(s)
        else:
            temp.append(s)
    tmp3 = arr[:i] + temp + temp2 + arr[i+m:]
    res = max(res, lis(tmp), lis(tmp2), lis(tmp3))

print(res)
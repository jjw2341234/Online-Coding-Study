from collections import defaultdict
moi = lambda: map(int, input().split())
c,n = moi()
dp = [float('inf')] * (1000+1)
num = []
for _ in range(n):
    num.append(tuple(moi()))
dp[0] = 0
for i in range(c+1):
    for v,k in num:
        if i+k >c:
            dp[c]  = min(dp[c] , dp[i] + v)
            continue
        dp[i+k]  = min(dp[i+k] , dp[i] + v)
print(dp[c])
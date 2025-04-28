moi = lambda: map(int, input().split())
n, m  = moi()
visitors = list(moi())
dp = [0] * (n)
dp[0] = visitors[0]
res = dict()
for i in range(1, n):
    dp[i] = dp[i-1] + visitors[i]
for i in range(n-1, -1, -1):
    if i and (i-m) >=0:
        dp[i] -= dp[i-m]
for d in dp:
    if d not in res:
        res[d]=1
    else:
        res[d]+=1

r = max(res)
if r == 0:
    print("SAD")
else:
    print(r)
    print(res[r])
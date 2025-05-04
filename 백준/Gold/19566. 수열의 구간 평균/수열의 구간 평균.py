import sys
from collections import defaultdict
input = sys.stdin.readline
moi = lambda: map(int, input().split())
n,k = moi()
arr = list(moi())
dp = [0] * (n)
dp[0] = arr[0] - k
for i in range(1, n):
    dp[i] = dp[i-1] - k + arr[i]
ind = defaultdict(int)
for i in range(n):
    ind[dp[i]] += 1
res = 0
for k, v in ind.items():
    res += (v-1) * v//2
    if k == 0:
        res+= v
print(res)
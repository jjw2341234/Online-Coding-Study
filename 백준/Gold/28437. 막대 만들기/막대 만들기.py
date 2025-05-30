moi = lambda: map(int, input().split())
n = int(input())
arr = list(moi())
dp  = [0] * 100001
for i in range(n):
    dp[arr[i]] +=1

for i in range(1, 100001):
    if not dp[i]:
        continue
    tmp = i + i
    while tmp <= 100000:
        dp[tmp]+= dp[i]
        tmp+=i
q = int(input())
l = list(moi())
for i in range(q):print(dp[l[i]], end = " ")
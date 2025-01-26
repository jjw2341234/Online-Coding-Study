n = int(input())
dp = [5] * (n+1)
k = 1
while k**2 <= n:
    dp[k**2] = 1
    k+=1
for i in range(1, n+1):
    if dp[i] == 1:
        continue
    j = 1
    while j*j <= i:
        dp[i] = min(dp[i], dp[j*j] + dp[i - j*j])
        j+=1
print(dp[n])
n = int(input())
mod = 1000000007
string = input().rstrip()
dp = [0] * (n+1)
dp[0] = 1
for _ in range(len(string)):
    tmp = 0
    new_dp  = [0] * (n+1)

    for i in range(n+1):
        tmp = (tmp + dp[i]) % mod
        if i > 25:
            tmp = (tmp - dp[i-26] + mod) % mod
        new_dp[i] = tmp
    dp = new_dp
print(dp[-1])
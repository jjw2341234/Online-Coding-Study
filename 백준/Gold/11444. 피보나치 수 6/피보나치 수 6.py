import sys
sys.setrecursionlimit(10000000)
n = int(input())
dp = {}
dp[0] = 0
dp[1] = 1
dp[2] = 1
def dynamic(i):
    if i not in dp:
        if i % 2:
            dp[i] = (dynamic(i//2) ** 2 + dynamic(i//2 + 1)** 2)  % 1000000007
        else:
            dp[i] = (dynamic(i//2) * (dynamic(i//2) + 2*dynamic(i//2 - 1))) % 1000000007
    return dp[i]

print(dynamic(n))
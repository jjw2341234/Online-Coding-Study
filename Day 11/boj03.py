import math
n = int(input())
dp = [0,1]
for i in range(2, n+1):
    minv = 1e9
    print(i)
    for j in range(1, int(i**0.5) + 1):
        minv = min(minv, dp[i - j ** 2])
        print(minv, i-j**2)
    dp.append(minv + 1) 
print(dp[n])
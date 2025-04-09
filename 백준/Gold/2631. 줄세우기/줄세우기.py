# 해당 문제는 증가하는 부분수열을 나열하는 문제와 같다.
n = int(input())

dp = [1] * (n+1)
num = [0]

for i in range(n):
    num.append(int(input()))

for i in range(1, n+1):
    for j in range(1,i):
        if num[j] < num[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(n-max(dp))
n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
dp = arr
for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            dp[i][j]+= arr[i-1][j]
        elif i == j:
            dp[i][j] += arr[i-1][j-1]
        else:
            dp[i][j] += max(arr[i-1][j-1], arr[i-1][j])
print(max(arr[n-1]))
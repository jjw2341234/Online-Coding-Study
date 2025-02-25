n = int(input())

arr = list(map(int, input().split()))

dp = [1] * n

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)

max_dp = max(dp)
print(max_dp)
sub_seq = []
for i in range(n-1, -1, -1):
    if dp[i] == max_dp:
        sub_seq.append(arr[i])
        max_dp-=1
sub_seq.sort()
print(*sub_seq)
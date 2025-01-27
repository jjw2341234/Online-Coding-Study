n = int(input())
arr = list(map(int, input().split()))
rev = arr[::-1]
cnt_arr = [1 for i in range(n)]
cnt_rev = [1 for i in range(n)]
for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            cnt_arr[i] = max(cnt_arr[i], cnt_arr[j]+1)
        if rev[i] > rev[j]:
            cnt_rev[i] = max(cnt_rev[i], cnt_rev[j]+1)

res = [0 for i in range(n)]

for i in range(n):
    res[i] = cnt_arr[i] + cnt_rev[n-i-1] - 1
print(max(res))

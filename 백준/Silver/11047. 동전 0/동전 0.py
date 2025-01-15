n,m = map(int, input().split())
arr = [int(input()) for i in range(n)]
cnt = 0
for i in range(n-1, -1, -1):
    if m == 0:
        break
    else:
        if arr[i] <= m:
            cnt+=(m//arr[i])
            m%=arr[i]
print(cnt)


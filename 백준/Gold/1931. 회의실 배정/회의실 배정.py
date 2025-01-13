n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]
arr.sort(key=lambda x: (x[1], x[0]))
s,e = arr[0]
cnt = 1
for i in range(1, len(arr)):
    if e <= arr[i][0]:
        cnt+=1
        s,e = arr[i]
print(cnt)
n = int(input())
arr = list(map(int, input().split()))

sets = set()
sets.add(arr[0] + arr[0])
cnt = 0
for i in range(1, n):
    for j in range(i):
        if arr[i] - arr[j] in sets:
            cnt+=1
            break
    for j in range(i+1):
        sets.add(arr[i] + arr[j])
print(cnt)
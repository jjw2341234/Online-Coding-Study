n = int(input())
arr = list(map(int, input().split()))
res = 0
lists = [0] *  1000001
for i in range(n):
    lists[i] = arr[i]
for i in range(n):
    if lists[i+1] > lists[i+2]:
        cnt = min(lists[i], lists[i+1] - lists[i+2])
        res+= cnt * 5
        lists[i]-=cnt
        lists[i+1]-=cnt
    if lists[i] and lists[i+1] and lists[i+2]:
        cnt = min(lists[i], lists[i+1])
        res+= 7*cnt
        lists[i]-=cnt
        lists[i+1]-=cnt
        lists[i+2]-=cnt
    res+= 3*lists[i]
print(res)
n,m = map(int, input().split())
arr = list(map(int, input().split()))
s,e = 1, max(arr)
mid = 0
while s<=e:
    mid = (s+e)//2
    res = 0
    for r in arr:
        if r > mid:
            res+=(r-mid)
    if res >= m:
        s = mid+1
    else:
        e = mid-1
print(e)
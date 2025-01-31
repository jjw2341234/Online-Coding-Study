n,m = map(int, input().split())
arr = sorted(list(set(list(map(int, input().split())))))
res = []

def dfs():
    if len(res) == m:
        print(*res)
        return
    for i in range(len(arr)):
        if len(res) == 0 or (len(res) and res[-1] <= arr[i]):
            res.append(arr[i])
            dfs()
            res.pop()
dfs()
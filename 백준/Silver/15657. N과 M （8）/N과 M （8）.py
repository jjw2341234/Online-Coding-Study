n,m = map(int, input().split())
arr = list(map(int, input().split()))
res = []
arr.sort()
def dfs(idx):
    if len(res) == m: 
        print(*res)
        return
    for i in range(idx,n):
        res.append(arr[i])
        dfs(i)
        res.pop()

dfs(0)
res.sort()
for r in res:
    print(*r)
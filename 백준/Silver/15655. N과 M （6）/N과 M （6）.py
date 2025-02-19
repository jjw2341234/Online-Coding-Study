n,m = map(int, input().split())
lists = list(map(int, input().split()))

lists.sort()
res = []
def dfs(idx):
    if len(res) == m:
        print(*res)
        return
    for i in range(idx, n):
        res.append(lists[i])
        dfs(i+1)
        res.pop()
dfs(0)
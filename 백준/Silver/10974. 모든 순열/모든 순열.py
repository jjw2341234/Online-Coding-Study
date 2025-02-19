n = int(input())
arr = []
def dfs(lev):
    if lev == n:
        print(*arr)
        return
    for i in range(1, n+1):
        if i not in arr:
            arr.append(i)
            dfs(lev+1)
            arr.pop()
dfs(0)
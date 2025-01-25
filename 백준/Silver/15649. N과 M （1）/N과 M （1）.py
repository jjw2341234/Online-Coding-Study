def dfs(count):
    if count== m:
        print(*arr)
        return
    for i in range(1, n+1):
        if i not in arr:
            arr.append(i)
            dfs(count+1)
            arr.pop()
n,m = map(int, input().split())
arr = []
dfs(0)

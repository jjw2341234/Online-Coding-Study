def dfs(cnt):
    if cnt == m:
        print(*arr)
        return
    for i in range(1, n+1):
        if arr:
            if arr[-1] <= i:
                arr.append(i)
                dfs(cnt+1)
                arr.pop()
        else:
            arr.append(i)
            dfs(cnt+1)
            arr.pop()
n,m = map(int, input().split())
arr = []
dfs(0)

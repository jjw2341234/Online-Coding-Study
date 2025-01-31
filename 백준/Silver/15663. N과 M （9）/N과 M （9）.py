def dfs():
    check = 0
    if len(res) == m:
        print(*res)
        return
    for i in range(n):
        if check != arr[i] and not visit[i]:
            res.append(arr[i])
            visit[i] = 1
            check = arr[i]
            dfs() 
            res.pop()
            visit[i] = 0
n,m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
visit = [0] * (n)
res = []
dfs()

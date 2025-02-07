n,m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
visit = [0] * n
ans = int(-1e9)
def dfs(cnt, idx):
    global ans
    if cnt == 3:
        tmp = 0
        for i in range(n):
            if visit[i]:
                tmp+= arr[i]
        if tmp <= m:
            ans = max(ans, tmp)
    else:
        for i in range(idx, n):
            if not visit[i]:
                visit[i] = 1
                dfs(cnt+1, i+1)
                visit[i] = 0
dfs(0,0)
print(ans)
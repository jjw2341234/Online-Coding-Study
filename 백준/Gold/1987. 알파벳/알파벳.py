def dfs(x,y,cnt):
    global max_
    max_ = max(max_, cnt)
    for nx, ny in ([x+1, y], [x-1, y], [x, y+1], [x, y-1]):
        if 0<=nx<n and 0<=ny<m and arr[nx][ny] not in alpha:
            alpha.add(arr[nx][ny])
            dfs(nx,ny,cnt+1)
            alpha.remove(arr[nx][ny])
    

n,m = map(int, input().split())
arr  = [list(input().strip()) for _ in range(n)]
max_ = 1
alpha = set(arr[0][0])
dfs(0,0,max_)
print(max_)
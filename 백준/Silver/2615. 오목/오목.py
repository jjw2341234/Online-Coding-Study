n = 19
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [0,1,-1,1]
dy = [1,1,1,0]

def dfs(x,y):
    for i in range(4):
        cnt = 1
        nx = x + dx[i]
        ny = y + dy[i]    
        while 0<=nx < n and 0<=ny < n and arr[x][y] == arr[nx][ny]:
            cnt+=1
            nx += dx[i]
            ny += dy[i]
            if cnt == 5:
                if not(0<=nx <n and 0<=ny<n and arr[nx][ny] == arr[x][y]) and not(0<=x-dx[i] < n and 0<=y - dy[i] < n and arr[x][y] == arr[x-dx[i]][y-dy[i]]):
                    print(arr[x][y])
                    print(x+1, y+1)
                    exit(0)
                else:break

for i in range(n):
    for j in range(n):
        if arr[i][j]:
            dfs(i,j)

print(0)
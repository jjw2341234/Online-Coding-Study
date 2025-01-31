n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
result = 0

def dfs(x,y,dir):
    global result
    if x == n-1 and y == n-1:
        result+=1
        return
    if x+1 <n and y + 1 < n:
        if arr[x+1][y+1] == 0 and arr[x][y+1] == 0 and arr[x+1][y] == 0:
            dfs(x+1, y+1, 2)
    if dir == 0 or dir == 2:
        if y+1 < n:
            if arr[x][y+1] == 0:
                dfs(x, y+1, 0)
    if dir == 1 or dir == 2:
        if x+1 <n:
            if arr[x+1][y] == 0:
                dfs(x+1, y, 1)

dfs(0,1,0)
print(result)
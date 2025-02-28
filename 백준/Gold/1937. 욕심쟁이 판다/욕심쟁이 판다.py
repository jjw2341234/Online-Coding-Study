import copy
from collections import deque
def dfs(x,y):
    if visit[x][y]:
        return visit[x][y]
    visit[x][y] = 1
    for nx, ny in ([x+1, y], [x-1, y], [x,y+1], [x, y-1]):
        if 0<=nx< n and 0<=ny< n and arr[x][y] < arr[nx][ny]:
           visit[x][y] = max(visit[x][y], dfs(nx, ny)+1)
    
    return visit[x][y]

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]
visit = [[0] * n for _ in range(n)]
#여기서 생각해야 할것은 처음 위치를 정해야 한다는것
res = 0
for i in range(n):
    for j in range(n):
        res = max(res,dfs(i,j)) #visit을 설정하지 않아야 할거 같음. 
print(res)
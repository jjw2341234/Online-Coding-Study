from collections import deque
m,n = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]

q = deque()

def bfs():
    while q:
        x,y = q.popleft()
        for nx, ny in [(x+1, y), (x-1, y), (x, y-1), (x, y+1)]:
            if 0<= nx < n and 0<= ny < m and not arr[nx][ny]:
                arr[nx][ny] =  arr[x][y] + 1
                q.append([nx, ny])

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            q.append([i,j])
bfs()
chk = False
res = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            chk = True
        res = max(res, arr[i][j])
if chk:
    print(-1)
else:
    print(res-1)
from collections import deque
m,n,h = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(n)] for i in range(h)]
q = deque()

def bfs():
    while q:
        z,x,y = q.popleft()
        for dz, dx, dy in [(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,-1), (0,0,1)]:
            nx = x + dx
            ny = y + dy
            nz = z + dz
            if 0<=nz<h and 0<=nx<n and 0<=ny <m and not arr[nz][nx][ny]:
                arr[nz][nx][ny] = arr[z][x][y] + 1
                q.append([nz, nx, ny])

for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k] == 1:
                q.append([i,j,k])
bfs()
cannot = False
res = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if not arr[i][j][k]:
                cannot = True
            res = max(res, arr[i][j][k])

if cannot:
    print(-1)
else:
    print(res-1)
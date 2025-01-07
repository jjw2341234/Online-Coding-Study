from collections import deque

m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

q = deque()
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] == 1:
            q.append([i,j])

def bfs():
    while q:
        x,y = q.popleft()
        for dx, dy in [(-1,0), (1,0), (0, 1), (0, -1)]:
            nx = x + dx
            ny = y + dy
            if 0<= nx < n and 0<= ny < m and not arr[nx][ny]:
                arr[nx][ny] = arr[x][y] + 1
                q.append([nx, ny])
bfs()
res = max(map(max, arr)) - 1

for ar in arr:
    for a in ar:
        if a == 0:
            res = -1
print(res)
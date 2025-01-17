from collections import deque

n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visit = [[-1] * m for _ in range(n)]

def bfs(i,j):
    q = deque()
    q.append([i,j])
    visit[i][j] = 0
    while q:
        x,y = q.popleft()
        for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
            if 0<=nx< n and 0<=ny<m and visit[nx][ny] == -1:
                if arr[nx][ny] == 0:
                    visit[nx][ny] = 0
                elif arr[nx][ny] == 1:
                    visit[nx][ny] = visit[x][y] + 1
                    q.append([nx, ny])


for i in range(n):
    for j in range(m):
        if arr[i][j] == 2 and visit[i][j] == -1:
            bfs(i,j)

for i in range(n):
    for j in range(m):
        if not arr[i][j]:
            print(0, end = " ")
        else:
            print(visit[i][j], end = " ")
    print()
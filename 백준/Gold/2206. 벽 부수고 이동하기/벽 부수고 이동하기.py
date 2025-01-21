from collections import deque
n,m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]
visit = [[[0] * 2 for _ in range(m)] for _ in range(n)]
visit[0][0][0] = 1
def bfs(x,y,cnt):
    q = deque()
    q.append([x,y,cnt])
    while q:
        x,y,cnt = q.popleft()
        if x == n-1 and y == m-1:
            return visit[x][y][cnt]

        for nx,ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
            if nx <0 or nx >= n or ny >= m or ny < 0:
                continue
            if arr[nx][ny] and not cnt:
                visit[nx][ny][1] = visit[x][y][0] + 1
                q.append([nx, ny, 1])
            elif arr[nx][ny] == 0 and visit[nx][ny][cnt] == 0:
                visit[nx][ny][cnt] = visit[x][y][cnt] + 1
                q.append([nx, ny, cnt])
    return -1
print(bfs(0,0,0))
from collections import deque
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
pos = []
x,y,size = 0,0,2

for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            x = i
            y = j

def bfs(x,y, shark_size):
    visit = [[0] * n for _ in range(n)]
    dist = [[0] * n for _ in range(n)]

    q = deque([[x,y]])
    visit[x][y] = 1
    cand = []
    while q:
        x,y = q.popleft()
        for nx, ny in ([x+1, y], [x-1, y], [x, y+1], [x, y-1]):
            if 0<=nx<n and 0<=ny<n and visit[nx][ny] == 0:
                if arr[nx][ny] <= shark_size:
                    q.append([nx, ny])
                    visit[nx][ny] = 1
                    dist[nx][ny] = dist[x][y] + 1
                    if arr[nx][ny] < shark_size and arr[nx][ny]:
                        cand.append([nx, ny, dist[nx][ny]])
    return sorted(cand, key=lambda x: (-x[2], -x[0], -x[1]))
cnt = 0
res = 0
while True:
    shark = bfs(x,y,size)
    if len(shark) == 0:
        break
    nx, ny, dist = shark.pop()
    res+= dist
    arr[x][y], arr[nx][ny] = 0,0
    x,y = nx, ny
    cnt+=1
    if cnt == size:
        size+=1
        cnt = 0
print(res)



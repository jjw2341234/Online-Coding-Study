from collections import deque
n = int(input())
arr = [list(map(int, input())) for i in range(n)]
visit = [[0] * n for i in range(n)]
def bfs(x,y):
    q = deque()
    cnt = 1
    q.append([x,y])
    visit[x][y] = 1
    while q:
        x,y = q.popleft()
        for dx, dy in [(-1,0), (1,0), (0,-1), (0, 1)]:
            nx = dx + x
            ny = dy + y
            if 0<=nx<n and 0<=ny<n and arr[nx][ny] and visit[nx][ny] == 0:
                visit[nx][ny] = 1
                cnt+=1
                q.append([nx, ny])
    return cnt
cnt = 0
res = []
for i in range(n):
    for j in range(n):
        if arr[i][j] and not visit[i][j]:
            res.append(bfs(i,j))
            cnt+=1
print(len(res))
res.sort()
for r in res:
    print(r)
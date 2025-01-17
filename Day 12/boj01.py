from collections import deque
n,m = map(int, input().split())
str = [list(input().strip()) for i in range(n)]
doyun  = []
for i in range(n):
    for j in range(m):
        if str[i][j] == 'I':
            doyun.append([i,j])
visit = [[0] * m for _ in range(n)]
cnt = 0
def bfs():
    global cnt
    x,y = doyun[0]
    visit[x][y] = 1
    q = deque()
    q.append([x, y])
    while q:
        x,y  = q.popleft()
        for nx, ny in [[x+1, y], [x-1, y], [x, y+1], [x, y-1]]:
            if 0<=nx< n and 0<=ny<m and str[nx][ny] != "X" and visit[nx][ny] == 0:
                visit[nx][ny] = 1
                if str[nx][ny] == "P":
                    cnt+=1
                q.append([nx, ny])

bfs()       
if not cnt:
    print("TT")
else:
    print(cnt)
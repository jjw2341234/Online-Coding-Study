from collections import deque

moi = lambda : map(int, input().split())

n,m = moi()
arr = [list(moi()) for _ in range(n)]

def bfs():
    q = deque()
    q.append([0,0])
    visit[0][0] = 1
    while q:
        x,y, = q.popleft()
        for nx, ny in [(x+1, y), (x-1, y), (x, y-1), (x, y+1)]:
            if 0<=nx< n and 0<=ny<m and not visit[nx][ny]:
                if arr[nx][ny]>=1:
                    arr[nx][ny]+=1
                else:
                    visit[nx][ny] = 1
                    q.append([nx, ny])

time = 0
while 1:
    visit = [[0] * (m) for _ in range(n)]
    flag = 0
    bfs()
    for i in range(n):
        for j in range(m):
            if arr[i][j] >= 3:
                flag = 1
                arr[i][j] = 0
            elif arr[i][j] == 2:
                arr[i][j] = 1
    if flag == 1:
        time+=1
    else:
        break
print(time)
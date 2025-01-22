from collections import deque

n,m = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]

def bfs():
    q = deque()
    q.append([0,0])
    visit[0][0] = 1
    while q:
        x,y = q.popleft()
        for nx, ny in [(x+1, y), (x-1, y), (x,y+1), (x,y-1)]:
            if 0<=nx<n and 0<=ny<m and not visit[nx][ny]:
                if arr[nx][ny]>=1:
                    arr[nx][ny]+=1
                else:
                    visit[nx][ny] = 1
                    q.append([nx, ny])

time = 0
while 1:
    visit = [[0] * m for _ in range(n)]
    bfs()
    flag = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] >=3:
                arr[i][j] = 0
                flag = 1
            elif  arr[i][j] == 2:
                arr[i][j] = 1
    if flag == 1:
        time+=1
    else:
        break
print(time)
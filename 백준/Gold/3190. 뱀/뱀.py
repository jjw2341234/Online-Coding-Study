from collections import deque
n = int(input())
k = int(input())

maps = [[0] * (n+1) for _ in range(n+1)]
for _ in range(k): 
    a,b = map(int, input().split())
    maps[a][b] = 2
info  = {}
m = int(input())
for _ in range(m):
    sec, dir = input().split()
    info[int(sec)] = dir
x,y = 1,1
maps[x][y] = 1
d = 0
dx = [0,1,0,-1]
dy = [1,0,-1,0]

time = 0
q = deque()
q.append([1,1])
while True:
    nx, ny = x+dx[d], y+ dy[d]
    if nx<=0 or nx>n or ny>n or ny <=0 or [nx, ny] in q:
        break

    if maps[nx][ny] != 2:
        a,b = q.popleft()
        maps[a][b] = 0
    x,y = nx, ny
    maps[x][y] = 1
    q.append([x,y])
    time+=1
    
    if time in info.keys():
        if info[time] == 'D':
            d = (d+1)%4
        else:
            if d == 0:
                d = 3
            else:
                d-=1
print(time+1)
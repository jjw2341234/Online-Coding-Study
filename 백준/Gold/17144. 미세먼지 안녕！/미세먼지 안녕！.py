from collections import deque

r,c,t = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(r)]

dust = []
machine = []

def diffuse():
    while dust:
        x,y, val = dust.pop()
        cnt = 0
        for nx, ny in ([x+1, y], [x-1, y], [x, y-1], [x, y+1]):
            if 0<=nx<r and 0<=ny < c and (nx, ny) not in machine:
                arr[nx][ny]+= val//5
                cnt+=1
        arr[x][y] -= val//5 * cnt

def clean_down():
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    x,y = machine[1] # 여기는 가면 안된다
    dir = 0
    down,y = x,1
    prev = 0
    while True:
        nx, ny = x + dx[dir], y + dy[dir]
        if nx == -1 or ny == -1 or nx == r or ny == c:
            dir = (dir+1) % 4
            continue
        if x == down and y == 0:
            break
        arr[x][y], prev = prev, arr[x][y]
        x,y = nx, ny
    return

for i in range(r):
    for j in range(c):
        if arr[i][j] > 0:
            dust.append((i,j, arr[i][j]))
        elif arr[i][j] == -1:
            machine.append((i,j))

def clean_up():
    dx = [0,-1,0,1]
    dy = [1,0,-1,0]
    x,y = machine[0] # 여기는 가면 안된다
    dir = 0
    up,y = x,1
    prev = 0
    while True:
        nx, ny = x + dx[dir], y + dy[dir]
        if nx == -1 or ny == -1 or nx == r or ny == c:
            dir = (dir+1) % 4
            continue
        if x == up and y == 0:
            break
        arr[x][y], prev = prev, arr[x][y]
        x,y = nx, ny
    return
for _ in range(t):
    diffuse()
    clean_up()
    clean_down()
    for i in range(r):
        for j in range(c):
            if arr[i][j]>0:
                dust.append([i,j, arr[i][j]])

ans = 0
for i in range(r):
    for j in range(c):
        if arr[i][j] > 0:
            ans+= arr[i][j]
print(ans)
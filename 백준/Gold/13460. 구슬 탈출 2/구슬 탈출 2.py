from collections import deque
n,m = map(int, input().split())
arr = [list(input().strip()) for _ in range(n)]
r = []
b = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]
visit = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'B':
            b.append([i,j])
        if arr[i][j] == 'R':
            r.append([i,j])

def move(x,y,dx,dy):
    cnt = 0
    while arr[x+dx][y+dy] != '#' and arr[x][y] != 'O':
        x+=dx
        y+=dy
        cnt+=1
    return x,y, cnt

def bfs():
    rx,ry = r.pop()
    bx,by = b.pop()
    q =deque()
    q.append([rx, ry, bx, by, 1])
    visit.append((rx,ry,bx,by))
    while q:
        rx, ry, bx, by, res = q.popleft()
        if res > 10:
            break
        for i in range(4):
            nrx,nry,rcnt = move(rx,ry,dx[i],dy[i])
            nbx,nby,bcnt = move(bx,by,dx[i],dy[i])

            if arr[nbx][nby] == 'O':
                continue
            if arr[nrx][nry] == 'O':
                print(res)
                return
            
            if nrx == nbx and nry == nby:
                if rcnt <= bcnt:
                    nbx-=dx[i]
                    nby-=dy[i]
                else:
                    nrx-=dx[i]
                    nry-=dy[i]
            if (nrx,nry,nbx,nby) not in visit:
                visit.append((nrx, nry, nbx, nby))
                q.append([nrx, nry, nbx, nby, res+1])
    print(-1)

bfs()

from collections import deque
n = int(input())
string = [list(input().strip()) for i in range(n)]

visit = [[0] * n for i in range(n)]
res = []
def bfs(x, y, c):
    q =deque()
    q.append([x,y])
    visit[x][y] = 1
    while q:
        x,y = q.popleft()
        for nx, ny in [(x-1, y), (x+1, y), (x, y+1), (x, y-1)]:
            if 0<=nx < n and 0<= ny < n and not visit[nx][ny] and string[nx][ny] in c:
                visit[nx][ny] = 1
                q.append([nx, ny])

blue, red, green = 0,0,0

for i in range(n):
    for j in range(n):
        if not visit[i][j]:
            if string[i][j] == 'R':
                bfs(i,j,'R')
                red+=1
            if string[i][j] == 'G':
                bfs(i,j,'G')
                green+=1
            if string[i][j] == 'B':
                bfs(i,j,'B')
                blue+=1
res.append(blue + red + green)
visit = [[0] * n for i in range(n)]
blue, red, green = 0,0,0

for i in range(n):
    for j in range(n):
        if not visit[i][j]:
            if string[i][j] == 'R' or string[i][j] == 'G':
                bfs(i,j,'GR')
                green+=1
            if string[i][j] == 'B':
                bfs(i,j,'B')
                blue+=1
res.append(blue+green)
print(*res)
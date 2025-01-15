from collections import deque
T = int(input())
def bfs(i,j):
    q = deque()
    q.append([i,j])
    visit[i][j] = 1
    while q:
        x,y = q.popleft()
        for dx, dy in ([1,0], [-1,0], [0,1], [0,-1]):
            nx = x + dx
            ny = y + dy
            if 0<= nx < n and 0<= ny < m and arr[nx][ny] and not visit[nx][ny]:
                visit[nx][ny] = 1
                q.append([nx, ny])
for _ in range(T):
    n,m,k = map(int, input().split())
    cnt = 0
    visit = [[0] * m for i in range(n)]
    arr = [[0] * m for i in range(n)]
    for w in range(k):
        x,y = map(int, input().split())
        arr[x][y] = 1

    for i in range(n):
        for j in range(m):
            if arr[i][j] and not visit[i][j]:
                bfs(i,j)
                cnt+=1     
    print(cnt)
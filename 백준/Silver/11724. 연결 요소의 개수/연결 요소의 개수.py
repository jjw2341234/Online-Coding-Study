from collections import deque
n,m =map(int, input().split())
arr = [[0] * (n+1) for i in range(n+1)]
visit = [0] * (n+1)
for _ in range(m):
    x,y = map(int, input().split())
    arr[x][y] = 1
    arr[y][x] = 1

def bfs(s):
    q = deque()
    q.append(s)
    visit[s] = 1
    while q:
        x = q.popleft()
        for nx in range(1, n+1):
            if arr[x][nx] and not visit[nx]:
                visit[nx] = 1
                q.append(nx)

res = 0
for i in range(1, n+1):
    if not visit[i]:
        bfs(i)
        res+=1
print(res)
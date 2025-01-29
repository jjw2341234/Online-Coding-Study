from collections import deque
import copy
n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
res = 0
def bfs():
    global res
    q =deque()
    visit = copy.deepcopy(arr)
    for i in range(n):
        for j in range(m):
            if visit[i][j] == 2:
                q.append([i,j])
    while q:
        x,y = q.popleft()
        for nx, ny in [(x+1,y), (x-1, y), (x,y+1), (x,y-1)]:
            if 0<=nx<n and 0<=ny<m and visit[nx][ny] == 0 :
                visit[nx][ny] = 2
                q.append([nx, ny])
    answer = 0
    for i in range(n):
        for j in range(m):
            if visit[i][j] == 0:
                answer+=1
    res = max(answer, res)

def wall(cnt):
    if cnt == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                arr[i][j] = 1
                wall(cnt+1)
                arr[i][j] = 0
wall(0)
print(res)
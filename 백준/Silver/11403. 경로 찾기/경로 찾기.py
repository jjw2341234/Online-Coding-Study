from collections import deque
n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]
visit = [[0] * n for i in range(n)]
q = deque()


def bfs(s,y):
    q.append([s,y])
    visit[s][y] = 1
    while q:
        x,y = q.popleft()
        for i in range(n):
            if arr[y][i] and not arr[s][i] and not visit[x][i]:
                arr[s][i] = 1
                visit[s][i] = 1
                q.append([s,i])

for i in range(n):
    for j in range(n):
        if arr[i][j] and not visit[i][j]:
            bfs(i,j)
for ar in arr:
    print(*ar)
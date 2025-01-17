from collections import deque
n,m = map(int, input().split())
visit = [0] * (101)
snake = {}
ladder = {}
for _ in range(n):
    x,y = map(int, input().split())
    ladder[x] = y

for _ in range(m):
    x,y = map(int, input().split())
    snake[x] = y

q = deque([1])

while q:
    x = q.popleft()
    if x == 100:
        print(visit[x])
        break
    for nx in range(x+1, x+7):
        if nx <= 100 and not visit[nx]:
            if nx in ladder.keys():
                nx = ladder[nx]
            if nx in snake.keys():
                nx = snake[nx]
            if not visit[nx]:
                visit[nx] = visit[x] + 1
                q.append(nx)


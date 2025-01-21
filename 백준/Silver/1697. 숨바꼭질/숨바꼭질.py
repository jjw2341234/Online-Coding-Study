from collections import deque

def bfs(x):
    q = deque()
    q.append(x)
    while q:
        x = q.popleft()
        if visit[e]:
            return visit[e]
        for nx in [x-1, x+1, 2*x]:
            if 0<=nx< 100001 and visit[nx] == 0:
                visit[nx] = visit[x] + 1
                q.append(nx)

s,e = map(int, input().split())
if s == e:
    print(0)
    exit(0)
visit = [0] * (100001)
print(bfs(s))

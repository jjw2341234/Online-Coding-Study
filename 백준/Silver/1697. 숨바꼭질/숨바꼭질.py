from collections import deque
s,e = map(int, input().split())
inf = int(1e6+1)
visit = [0] * inf

def bfs(s):
    q = deque()
    q.append(s)
    while q:
        x = q.popleft()
        if x == e:
            print(visit[e])
            return
        for i in (x-1, x+1, 2*x):
            if 0<= i < inf and not visit[i]:
                visit[i] = visit[x] + 1
                q.append(i)

bfs(s)

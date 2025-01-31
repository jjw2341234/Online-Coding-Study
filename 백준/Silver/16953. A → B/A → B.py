from collections import deque
s,e = map(int, input().split())
def bfs():
    q = deque()
    q.append([s,1])
    while q:
        x, cnt= q.popleft()
        if x == e:
            print(cnt)
            return
        for nx in ([2*x, 10*x+1]):
            if s<=nx <=e:
                q.append([nx, cnt+1])
    else:
        print(-1)
        return
bfs()
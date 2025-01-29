from collections import deque
def bfs(s, e):
    global cnt
    global res
    q =deque()
    q.append(s)
    visit[s] = 0
    while q:
        x = q.popleft()
        tmp = visit[x]
        if x == e:
            res = tmp
            cnt+=1
            continue
        for nx in [x+1, x-1, x*2]:
            if 0<=nx<100001:
                if visit[nx] == 0:
                    visit[nx] = visit[x] + 1
                    q.append(nx)
                elif visit[nx] == visit[x] + 1:
                    q.append(nx)



n,m = map(int, input().split())
arr = [0] * (100001)
visit = [0] * (100001)
cnt = 0
res = 0
bfs(n,m)
print(res)
print(cnt)
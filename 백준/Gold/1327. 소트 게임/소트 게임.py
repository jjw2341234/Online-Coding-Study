from collections import deque
moi = lambda: map(int, input().split())
n,m = moi()
start  = tuple(moi())
visit = dict()
visit[start] = 0
goal  = tuple(sorted(start))

def bfs(x):
    q = deque()
    q.append(x)
    while q:
        arr = q.popleft()
        tmp = visit[arr]
        for i in range(len(arr)):
            if i + m -1 < n:
                a = list(arr)
                a[i:i+m] = a[i:i+m][::-1]
                a = tuple(a)
                if a not in visit:
                    visit[a] = tmp + 1
                    q.append(a)
bfs(start)
try:
    print(visit[goal]) 
except:
    print(-1)
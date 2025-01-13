from collections import deque
n = int(input())
m = int(input())
arr = [[0] * (n+1) for i in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1
visit = [0] * (n+1) 
def bfs(s):
    q =deque()
    q.append(s)
    visit[s] = 1
    while q:
        x = q.popleft()
        for i in range(1, n+1):
            if arr[x][i] and not visit[i]:
                visit[i] = 1
                q.append(i)
bfs(1)
cnt = 0
for v in visit:
    if v == 1:
        cnt+=1
print(cnt-1)
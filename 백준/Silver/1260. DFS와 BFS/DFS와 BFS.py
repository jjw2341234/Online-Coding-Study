from collections import deque

def bfs(s):
    q =deque()
    q.append(s)
    v[s] = 1
    while q:
        x = q.popleft()
        print(x, end = " ")
        for nxt in range(len(arr[x])):
            if not v[nxt] and arr[x][nxt]:
                v[nxt] = 1
                q.append(nxt)

def dfs(s):
    stack = [s]
    v[s] = 1
    print(s, end = " ")
    for i in range(len(arr[s])):
        if not v[i] and arr[s][i] == 1:
            dfs(i) 
n,m,s = map(int, input().split())
v = [0] * (n+1)
arr  = [[0] * (n+1) for _ in range(n+1)]
for _ in range(m):
    x,y = map(int, input().split())
    arr[x][y] = arr[y][x] = 1

dfs(s)

print()

v = [0] * (n+1)

bfs(s)

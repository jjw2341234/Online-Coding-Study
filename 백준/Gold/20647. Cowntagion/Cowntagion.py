import sys
sys.setrecursionlimit(100000)

input = sys.stdin.readline
n = int(input())
moi  = lambda: map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    x,y = moi()
    graph[x].append(y)
    graph[y].append(x)

farm = [0] * (n+1)
farm[1] = 1
cnt = 0

def dfs(x, p):
    global cnt
    ccnt = 0
    for nx in graph[x]:
        if nx != p:
            ccnt+=1
    while ccnt >= farm[x]:
        cnt+=1
        farm[x] *=2

    for nx in graph[x]:
        if nx != p:
            farm[nx] = 1
            farm[x]-=1
            dfs(nx, x)
            cnt+=1
dfs(1, -1)
print(cnt)


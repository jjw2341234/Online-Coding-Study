import sys
sys.setrecursionlimit(10**5)
n = int(input())
graph=[[] for _ in range(n)]

for _ in range(n-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

values = list(map(int, input().split()))

visit = [0] * (n)
def dfs(x):
    visit[x] = 1
    total= values[x]
    for next in graph[x]:
        if not visit[next]:
            gains = dfs(next)
            if gains>0:
                total+= gains
    return total
print(dfs(0))

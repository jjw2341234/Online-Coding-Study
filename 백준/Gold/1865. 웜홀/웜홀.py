import heapq
import sys
input = sys.stdin.readline

inf = sys.maxsize
def dijk(s):
    visit = [inf] * (n+1)
    visit[s] = 0
    q = []
    q.append([0, s])
    for i in range(n):
        for s in range(1, n+1):
            for next, cost in graph[s]:
                if visit[next] > visit[s] + cost:
                    visit[next] = visit[s] + cost
                    if i == n-1:
                        return True
    return False
        
t = int(input())
for  _ in range(t):
    n,m,w = map(int, input().split())
    chk = 0
    graph = [[] for i in range(n+1)]
    for i in range(m):
        a,b,c = map(int, input().split())
        graph[a].append([b,c])
        graph[b].append([a,c])
    for i in range(w):
        a,b,c = map(int, input().split())
        graph[a].append([b,-c])
    res = dijk(1)
    if res:
        print("YES")
    else:
        print("NO")
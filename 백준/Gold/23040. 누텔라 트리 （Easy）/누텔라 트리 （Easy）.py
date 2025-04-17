import sys
input = sys.stdin.readline
n = int(input())

p = [i for i in range(n+1)]
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a,b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)

color = " "+input().rstrip()
def find(x): #그래프 내의 연결개수 
    while x != p[x]:
        p[x] = p[p[x]]
        x = p[x]
    return x
sz = [1] * (n+1)

def union(a,b):
    a = find(a)
    b = find(b)
    if a == b:
        return
    p[b] = a
    sz[a]+=sz[b]

for i in range(n+1):
    for nxt in graph[i]:
        if color[i] == 'R' and color[nxt] == 'R':
            union(i, nxt)
res = 0
for i in range(1, n+1):
    if color[i] == 'B':
        for nxt in graph[i]:
            if color[nxt] == 'R':
                res+=sz[find(nxt)]
print(res)         
import sys
input = sys.stdin.readline
moi = lambda: map(int, input().split())
def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]
    
def union(a,b):
    a = find(a)
    b = find(b)
    parent[a]  = b

n,m = moi()
parent = [i for i in range(n+1)]

edges = []
for _ in range(m):
    a,b,c,x = moi()
    if x == 1:
        if find(a) != find(b):
            union(a,b)
    else:
        edges.append((a,b,c))
res = 0
edges.sort(key = lambda x: -x[2])
for i in edges:
    a,b,c = i
    if find(a) != find(b):
        union(a,b)
    else:
        res+=c
print(res)
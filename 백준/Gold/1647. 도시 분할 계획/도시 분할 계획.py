moi = lambda:map(int, input().split())

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)

    parent[a] = b

n,m = moi()
edges  = []
parent = [i for i in range(n+1)]
for _ in range(m):
    a,b,c = moi()
    edges.append((a,b,c))
edges.sort(key = lambda x:  x[2])
res = 0
max_num = 0
for a,b,c in edges:
    if find(a) != find(b):
        union(a,b)
        res += c
        max_num = c
print(res - max_num)

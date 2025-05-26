import sys
input = sys.stdin.readline
moi = lambda: map(int, input().split())

n,m = moi()
def find(x):
    if x!= parent[x]:
        parent[x] = find(parent[x])
    return parent[x]
def union(a,b):
    a = find(a)
    b = find(b)
    if a!= b:
        if a< b:
            parent[a] = b
        else:
            parent[b] = a
parent = [i for i in range(n+1)]
for _ in range(m):
    a,b,c = moi()
    if a == 0:
        union(b,c)
    else:
        if find(b) == find(c):
            print("YES")
        else:
            print("NO")
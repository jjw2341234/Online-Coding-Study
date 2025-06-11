import heapq
import math
def get_dist(a1, b1, a2, b2):
    return (a1 - a2) ** 2 + (b1 - b2) **2
n = int(input())
parent =  [i  for i in range(n)]
pos = []
q = []
for _ in range(n):
    a,b = map(int, input().split())
    pos.append((a,b,_))
for i in range(n):
    x1,y1,node1 = pos[i]
    for j in range(i+1, n):
        x2,y2,node2 = pos[j]
        cost = get_dist(x1, y1, x2, y2)
        heapq.heappush(q, [cost, node1, node2])
def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)
    if a == b:
        return False
    else:
        parent[a] = b
        return True


def kruskal():
    edge_cnt = 0
    while q:
        c, n1, n2= heapq.heappop(q)
        if union(n1, n2):
            edge_cnt+=1
            if edge_cnt == n-1:
                return c
print(kruskal())

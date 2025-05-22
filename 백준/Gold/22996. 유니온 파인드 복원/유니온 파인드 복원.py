import sys
input =sys.stdin.readline

moi  = lambda: map(int, input().split())

n,m = moi()

print(n,m)

parent = [0] + list(moi()) # 0~N까지의 값이 있다

k = int(input())
for _ in range(k):
    v = int(input())
    print(2, v)

graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
for i in range(1, n+1):
    if parent[i] != i: # 부모 노드가 아님
        k+=1
        graph[i].append(parent[i]) #자식 노드는 부모 노드의 값을 가져야 함
        indegree[parent[i]]+=1

stk = []
for i in range(1, n+1):
    if not indegree[i]:
        stk.append(i) #자식 노드만 찾는다
while stk:
    u = stk.pop() #stack에 있는 자식 노드를 기준으로 순회를 해야함
    for v in graph[u]:
        print(1,u,v)
        indegree[v]-=1
        if not indegree[v]:
            stk.append(v)
if k< m:
    for i in range(1, n+1):
        if parent[i] == i:
            v = i
            break
    for _ in range(k, m):
        print(1, v, v)
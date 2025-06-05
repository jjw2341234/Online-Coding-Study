from collections import defaultdict, deque
import sys
input = sys.stdin.readline

moi = lambda: map(int, input().split())
n,m,c = moi()
arr = list(moi())
query = [tuple(moi()) for _ in range(c)]
graph = defaultdict(list)
indegree = [0] * (n+1)
dp = [0] + arr[:]

for a,b,x in query:
    graph[a].append((b, x))
    indegree[b]+=1
q = deque()

for i in range(1, n+1):
    if indegree[i] == 0: 
        q.append(i)
while q:
    cur = q.popleft()
    for nxt, cost in graph[cur]:
        if dp[nxt] < dp[cur] + cost:
            dp[nxt] = dp[cur] + cost
        indegree[nxt]-=1
        if indegree[nxt] == 0:
            q.append(nxt)
for i in range(1, n+1):
    print(dp[i])
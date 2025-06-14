from collections import defaultdict
ans = input().rstrip()
n = int(input())
arr = [input().rstrip() for _ in range(n)]
graph = defaultdict(list)
def graphic(x):
    for i in range(len(ans) - len(x) + 1):
        if ans[i: i+len(x)] == x:graph[i].append(i+len(x))
for i in arr:graphic(i)
visit = [0] * (len(ans) + 1)
def dfs(x):
    visit[x] = 1
    if x == len(ans):
        print(1)
        exit()
    for i in graph[x]:
        if not visit[i]:dfs(i)
dfs(0)
print(0)
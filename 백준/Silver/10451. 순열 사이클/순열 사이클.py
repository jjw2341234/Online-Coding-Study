import sys
input = sys.stdin.readline
t = int(input())

def dfs(x):
    global cnt
    visit[x] = 1
    cycle.append(x)
    if visit[arr[x]]:
        if arr[x] in cycle:
            cnt+=1
        return
    else:
        dfs(arr[x])

for _ in range(t):
    n= int(input())
    arr = [0] + list(map(int, input().split()))
    visit = [0] * (n+1)
    cnt = 0
    for i in range(1, n+1):
        if not visit[i]:
            cycle = []
            dfs(i)
    print(cnt)
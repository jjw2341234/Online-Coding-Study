from collections import deque
t = int(input())
for _ in range(t):
    n,m = map(int, input().split())
    arr = [0] + list(map(int, input().split()))
    graph = [[] for _ in range(n+1)]
    degree = [0] * (n+1)
    dp = [0] * (n+1)
    for _ in range(m):
        a,b = map(int, input().split())
        graph[a].append(b)
        degree[b]+=1

    q = deque()
    for i in range(1, n+1):
        if not degree[i]:
            q.append(i)
            dp[i] = arr[i]
    while q:
        x = q.popleft()
        for i in graph[x]:
            degree[i]-=1
            dp[i] = max(dp[x] + arr[i], dp[i])
            if degree[i] == 0:
                q.append(i)
    r = int(input())
    print(dp[r])
    
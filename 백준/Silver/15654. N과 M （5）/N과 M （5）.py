def dfs(s):
    if s == m:
        print(' '.join(map(str, res)))
        return
    for i in range(n):
        if visit[i]:
            continue
        res.append(arr[i])
        visit[i] = True
        dfs(s+1)  # 같은 원소를 다시 쓰지 않도록 i + 1
        visit[i] = False
        res.pop()

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()  # 오름차순 정렬
visit = [False] * n
res = []
dfs(0)
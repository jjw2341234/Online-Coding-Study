def dfs(count):
    if count== m:
        print(*arr)
        return
    for i in range(1, n+1):
        if i not in arr:
            if len(arr): 
                if arr[-1] < i:
                    arr.append(i)
                    dfs(count+1)
                    arr.pop()
                else:
                    continue
            else:
                arr.append(i)
                dfs(count+1)
                arr.pop()
n,m = map(int, input().split())
arr = []
dfs(0)

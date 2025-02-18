n, s = map(int, input().split())
arr = list(map(int, input().split()))

def dfs(idx, path, r, res):
    # 길이가 r인 조합을 찾으면 res에 추가
    if len(path) == r:
        res.append(path)
        return
    
    # 조합을 생성하기 위해 재귀 호출
    for i in range(idx, len(arr)):
        dfs(i + 1, path + [arr[i]], r, res)  # 현재 원소를 추가하여 재귀 호출

cnt = 0
for i in range(1, n+1):
    res = []
    dfs(0, [], i, res)  # 각 길이에 대해 dfs 호출
    for x in res:
        if sum(x) == s:
            cnt += 1
print(cnt)

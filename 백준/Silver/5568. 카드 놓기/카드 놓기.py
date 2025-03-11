n = int(input())
k =  int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
cnt = 0
res_list = []
def dfs(res):
    global cnt
    global res_list
    if len(res) == k:
        tmp  = []
        for r in res:
            tmp.append(arr[r])
        if ''.join(map(str, tmp)) not in res_list:
            res_list.append( ''.join(map(str, tmp)))
            cnt+=1
            return
    for i in range(len(arr)):
        if i not in res:
            res.append(i)
            dfs(res)
            res.pop()
dfs([])
print(cnt)
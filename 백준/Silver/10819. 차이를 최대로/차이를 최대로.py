import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
arr.sort()
lists = []
res = []
def dfs():
    global res
    
    if len(lists) == n:
        tmp= []
        for i in range(len(lists)):
            tmp.append(arr[lists[i]])
        res.append(tmp[:])
        return
    
    for i in range(n):
        if i not in lists:
            lists.append(i)
            dfs()
            lists.pop()
dfs()
ans = 0 
for r in res:
    tmp = 0
    for i in range(1, n):
        tmp+= abs(r[i-1] -r[i])
    ans = max(tmp, ans)
print(ans) 
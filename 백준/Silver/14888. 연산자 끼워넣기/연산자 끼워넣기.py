n = int(input())
arr = list(map(int, input().split()))
add,sub,mul,div = map(int, input().split())

max_value = int(-1e9)
min_value = int(1e9)

def dfs(limit, res):
    global add, sub, mul, div, max_value, min_value
    if limit == n:
        max_value = max(max_value, res)
        min_value = min(min_value, res)
    else:
        if add >0:
            add-=1
            dfs(limit+1, res+arr[limit])
            add+=1
        if sub >0:
            sub-=1
            dfs(limit+1, res-arr[limit])
            sub+=1
        if mul >0:
            mul-=1
            dfs(limit+1, res*arr[limit])
            mul+=1
        if div >0:
            div-=1
            dfs(limit+1, int(res/arr[limit]))
            div+=1

dfs(1, arr[0])

print(max_value)
print(min_value)
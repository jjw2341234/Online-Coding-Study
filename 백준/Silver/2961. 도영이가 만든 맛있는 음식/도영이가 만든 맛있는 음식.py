n = int(input())

arr = [list(map(int, input().split())) for i in range(n)]
result = int(1e9)

def dfs(depth, cnt, acid,bitter):
    global result
    
    if cnt:
        if abs(acid - bitter) < result:
            result = abs(acid - bitter)

    if depth == n:
        return 


    dfs(depth+1, cnt+1, acid*arr[depth][0], bitter + arr[depth][1])
    dfs(depth+1, cnt, acid, bitter)


dfs(0,0,1,0)
print(result)
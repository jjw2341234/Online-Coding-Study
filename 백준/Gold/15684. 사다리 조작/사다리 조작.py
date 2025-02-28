n,m,h = map(int, input().split())
arr = [[0] * (n) for _ in range(h)]
for _ in range(m):
    x,y = map(int, input().split())
    arr[x-1][y-1] = 1
        
def check():
    for i in range(n):
        st = i 
        for j in range(h):
            if arr[j][st] == 1:
                st+=1
            elif st > 0 and arr[j][st-1] == 1:
                st-=1
        if i!= st:
            return False
    return True
answer = 4
def dfs(cnt, x, y):
    global answer
    if answer <= cnt:
        return 
    if check():
        answer = min(cnt, answer)
        return
    if cnt == 3:
        return
    
    for i in range(x, h):
        for j in range(n-1):
            if arr[i][j] == 0:
                arr[i][j] = 1
                dfs(cnt+1, i, j+2)
                arr[i][j] = 0

dfs(0,0,0)
if answer > 3:
    print(-1)
else:
    print(answer)

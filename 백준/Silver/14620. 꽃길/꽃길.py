n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]
res = int(1e9)

def check(x,y, list):
    for nx, ny in ([x+1, y], [x-1, y], [x, y+1], [x, y-1]):
        if (nx, ny) in list: return False
    return True

def dfs(list, value):
    global res
    if res <= value: return
    if len(list) == 15:
        res = min(res, value)
    else:
        for i in range(1, n-1):
            for j in range(1, n-1):
                if check(i,j,list) and (i,j) not in list:
                    temp = [(i,j)]
                    temp_value = arr[i][j]
                    for nx, ny in ([i+1, j], [i-1, j], [i, j+1], [i, j-1]):
                        temp_value+= arr[nx][ny]
                        temp.append((nx, ny))
                    dfs(list+temp, value + temp_value)

dfs([], 0)
print(res)
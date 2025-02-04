import copy
n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]

def left(arr):
    for i in range(n):
        cursor = 0#가장 왼쪽에 있는 값을 커서로 지정
        for j in range(n):
            if arr[i][j]:
                tmp = arr[i][j]
                arr[i][j] = 0

                if arr[i][cursor] == 0:
                    arr[i][cursor] = tmp
                elif arr[i][cursor] == tmp:
                    arr[i][cursor] = 2*tmp
                    cursor+=1
                else:
                    cursor+=1
                    arr[i][cursor] = tmp
    return arr

def right(arr):
    for i in range(n):
        cursor = n-1#가장 왼쪽에 있는 값을 커서로 지정
        for j in range(n-1, -1, -1):
            if arr[i][j]:
                tmp = arr[i][j]
                arr[i][j] = 0

                if arr[i][cursor] == 0:
                    arr[i][cursor] = tmp
                elif arr[i][cursor] == tmp:
                    arr[i][cursor] = 2*tmp
                    cursor-=1
                else:
                    cursor-=1
                    arr[i][cursor] = tmp
    return arr

def down(arr):
    for j in range(n):
        cursor = 0#가장 왼쪽에 있는 값을 커서로 지정
        for i in range(n):
            if arr[i][j]:
                tmp = arr[i][j]
                arr[i][j] = 0

                if arr[cursor][j] == 0:
                    arr[cursor][j] = tmp
                elif arr[cursor][j] == tmp:
                    arr[cursor][j] = 2*tmp
                    cursor+=1
                else:
                    cursor+=1
                    arr[cursor][j] = tmp
    return arr

def up(arr):
    for j in range(n):
        cursor = n-1#가장 왼쪽에 있는 값을 커서로 지정
        for i in range(n-1, -1, -1):
            if arr[i][j]:
                tmp = arr[i][j]
                arr[i][j] = 0

                if arr[cursor][j] == 0:
                    arr[cursor][j] = tmp
                elif arr[cursor][j] == tmp:
                    arr[cursor][j] = 2*tmp
                    cursor-=1
                else:
                    cursor-=1
                    arr[cursor][j] = tmp
    return arr

def simulations(cnt, arr):
    global res
    if cnt == 5:
        for i in range(n):
            for j in range(n):
                res = max(arr[i][j], res)
        return
    
    for i in range(4):
        arr2 = copy.deepcopy(arr)
        if i == 0:
            simulations(cnt+1, up(arr2))
        elif i == 1:
            simulations(cnt+1, down(arr2))
        elif i == 2:
            simulations(cnt+1, right(arr2))
        elif i == 3:
            simulations(cnt+1, left(arr2))
res = 0
simulations(0, graph)
print(res)
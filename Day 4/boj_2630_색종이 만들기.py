import math
n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]
visit = [[0] * n for _ in range(n)]
z_cnt = 0
o_cnt = 0
def check_validity(x,y,n):
    global z_cnt, o_cnt
    color = arr[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if arr[i][j] != color:
                check_validity(x,y,n//2)
                check_validity(x+n//2,y,n//2)
                check_validity(x,y+n//2,n//2)
                check_validity(x+n//2,y+n//2,n//2)
                return
    if color ==0:
        z_cnt+=1
    else:
        o_cnt+=1
check_validity(0,0,n)
print(z_cnt)
print(o_cnt)
#이거는 다시 풀기


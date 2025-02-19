from collections import deque
import copy
n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
#1~5까지의 값들을 0~4까지로 바꿈
dx = [1,0,-1,0]
dy = [0,1,0,-1]
#남,동,북,서

dir = {1: [[0], [1], [2], [3]],
       2: [[0,2], [1,3]],
       3: [[0,1], [1,2], [2,3], [3,0]], 
       4: [[0,1,2], [1,2,3], [2,3,0], [3,0,1]],
       5:[[0,1,2,3]]
       }
cctv = deque()
for i in range(n):
    for j in range(m):
        if 0<arr[i][j]<6:
            cctv.append([i,j])    
res = int(1e9)
def dfs(lev, board):
    global res 
    if lev == len(cctv):
        cnt = 0
        for i in range(n):
            cnt+=board[i].count(0)
        res = min(res, cnt)
        return
    temp = copy.deepcopy(board)
    x,y = cctv[lev]
    for i in dir[board[x][y]]:
        fill(temp, x, y, i)
        dfs(lev+1, temp)
        temp = copy.deepcopy(board)

def fill(board,x,y, mode):
    for i in mode:
        nx = x
        ny = y
        while 1:
            nx+= dx[i]
            ny+= dy[i]
            if 0<=nx<n and 0<=ny<m: 
                if arr[nx][ny] == 0:
                    board[nx][ny] = -1
                elif arr[nx][ny] == 6:
                    break
            else:
                break

dfs(0, arr)
print(res)
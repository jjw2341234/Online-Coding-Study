import copy
n = 4
board = [[] for _ in range(n)]
for i in range(n):
    tmp = list(map(int, input().split()))
    tmp_list = []
    for j in range(0, 8, 2):
        tmp_list.append([tmp[j], tmp[j+1]-1])
    board[i] = tmp_list

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]

max_score = 0

def dfs(sx, sy, board, score):
    global max_score    
    score+= board[sx][sy][0]
    board[sx][sy][0] = 0

    max_score = max(max_score, score)
    for f in range(1, 17):
        fx,fy = -1,-1
        for x in range(n):
            for y in range(n):
                if board[x][y][0] == f:
                    fx,fy = x,y
                    break
        if fx == -1 and fy == -1:
            continue
        fd = board[fx][fy][1]
        for i in range(8):
            nd = (fd + i)%8
            nx, ny = fx+dx[nd], fy+dy[nd]
            if not (0<= nx < n and 0<=ny < n) or (nx == sx and ny == sy):
                continue
            board[fx][fy][1] = nd
            board[fx][fy], board[nx][ny] = board[nx][ny], board[fx][fy]
            break
    sd = board[sx][sy][1]
    for i in range(1,5):
        nx, ny = sx+dx[sd] * i, sy+dy[sd] * i
        if (0<= nx < n and 0<=ny < n) and board[nx][ny][0]:
           dfs(nx, ny, copy.deepcopy(board), score)
     
dfs(0,0,board, max_score)
print(max_score)
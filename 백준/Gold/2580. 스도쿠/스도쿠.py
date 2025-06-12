import sys
input = sys.stdin.readline
n = 9
sudoku = [list(map(int, input().split())) for _ in range(n)]
sparsity = list()
for i in range(n):
    for j in range(n):
        if not sudoku[i][j]: sparsity.append((i,j))

def check(x,y, a):
    for i in range(n):
        if sudoku[i][y] == a or sudoku[x][i] == a:
            return False
    Box = 3

    for i in range(Box):
        for j in range(Box):
            if sudoku[x//Box * Box + i][y// Box * Box + j] == a:
                return False
    return True

def dfs(idx):
    if idx == len(sparsity):
        for i in sudoku:
            print(*i)
        exit()
    for i in range(1, 10):
        x,y = sparsity[idx]
        if check(x,y,i):
            sudoku[x][y] = i
            dfs(idx+1)
            sudoku[x][y] = 0
dfs(0)
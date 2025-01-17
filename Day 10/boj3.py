n,m = map(int, input().split())
visit =[[0] * (m) for i in range(n)]
arr = [list(map(int, input().split())) for i in range(n)]
maxValue = 0
move = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def ternomino(i,j, res, cnt):
    global maxValue
    if cnt == 4:
        maxValue = max(maxValue, res)
        return
    for x in range(4):
        nx = i+move[x][0]
        ny = j+move[x][1]
        if 0<=nx< n and 0 <= ny < m  and not visit[nx][ny]:
            visit[nx][ny] = 1
            ternomino(nx, ny, res+arr[nx][ny], cnt+1)
            visit[nx][ny] = 0


def exec(i,j):

    global maxValue
    for x in range(4):
        tmp = arr[i][j]
        for y in range(3):
            t = (x + y) % 4
            nx = i + move[t][0]
            ny = j + move[t][1] #해당 문제에서 킥인 부분, 결국 주어진 좌표에서 상하좌우를 다 더하는 방식이다. 

            if not (0<=nx< n and 0 <= ny < m):
                tmp = 0
                break
            tmp+= arr[nx][ny]
        maxValue = max(maxValue, tmp)



for i in range(n):
    for j in range(m):
        visit[i][j] = 1
        ternomino(i,j,arr[i][j], 1)
        visit[i][j] = 0

        exec(i,j)
print(maxValue)



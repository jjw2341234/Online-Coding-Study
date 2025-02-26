from collections import deque
def move(q1, q2, road):
    dir = [(-1,0), (1,0), (0,1), (0,-1)]
    pos = []
    for dx, dy in dir:
        n1 = (q1[0] + dx, q1[1] + dy)
        n2 = (q2[0] + dx, q2[1] + dy)
        
        if road[n1[0]][n1[1]] == 0 and road[n2[0]][n2[1]] == 0:
            pos.append((n1, n2))
        
    if q1[0] == q2[0]:
        for i in [-1,1]:
            if road[q1[0]+i][q1[1]] == 0 and road[q2[0]+i][q2[1]] == 0:
                pos.append((q1, (q1[0] + i, q1[1])))
                pos.append((q2, (q2[0] + i, q2[1])))
    else:
        for i in [-1,1]:
            if road[q1[0]][q1[1]+i] == 0 and road[q2[0]][q2[1]+i] == 0:
                pos.append(((q1[0], q1[1] + i), q1))
                pos.append(((q2[0], q2[1] + i), q2))
    return pos
            
def solution(board):
    n = len(board)
    road = [[1] * (n+2) for _ in range(n+2)]
    for i in range(n):
        for j in range(n):
            road[i+1][j+1] = board[i][j]
    
    q  = deque([((1,1), (1,2), 0)])
    confirm = set([((1,1), (1,2))])
    
    while q:
        q1, q2, cnt = q.popleft()
        if q1 == (n,n) or q2 == (n, n):
            return cnt
        for nxt in move(q1, q2, road):
            if nxt not in confirm:
                q.append((*nxt, cnt+1))
                confirm.add(nxt) 
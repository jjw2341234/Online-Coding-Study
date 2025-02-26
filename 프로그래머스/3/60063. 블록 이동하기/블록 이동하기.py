from collections import deque
    
def move(p1, p2, road):
    
    dirs = [(0,1),(1,0),(-1,0),(0,-1)]
    poss = []
    # 상하좌우로 이동
    for dx, dy in dirs:
        n1 = (p1[0] + dx, p1[1] + dy)
        n2 = (p2[0] + dx, p2[1] + dy)
        if road[n1[0]][n1[1]] == 0 and road[n2[0]][n2[1]] == 0:
            poss.append((n1,n2))
            
    #회전        
    if p1[0] == p2[0]: #수평일때
        for i in [-1,1]:
            if road[p1[0]+i][p1[1]] == 0 and road[p2[0]+i][p2[1]] == 0:
                poss.append((p1, (p1[0]+i,p1[1])))
                poss.append((p2, (p2[0]+i,p2[1])))
    else: # 수직일때
        for i in [-1,1]:
            if road[p1[0]][p1[1]+i] == 0 and road[p2[0]][p2[1]+i] == 0:
                poss.append(((p1[0],p1[1]+i),p1))
                poss.append(((p2[0],p2[1]+i),p2))
    return poss

def solution(board):
    length = len(board)
    #  범위 밖으로 못나가게 벽을 만듬
    road= [[1] * (length+2) for _ in range(length+2)]
    for i in range(length):
        for j in range(length):
            road[i+1][j+1] = board[i][j]

    que = deque([((1, 1), (1, 2), 0)])
    confirm = set([((1, 1), (1, 2))])
    while que:
        p1, p2, result = que.popleft()
        if p1 == (length,length) or p2 == (length,length):
            return result
        for k in move(p1,p2,road):
            if k not in confirm:
                que.append((*k, result+1))
                confirm.add(k)
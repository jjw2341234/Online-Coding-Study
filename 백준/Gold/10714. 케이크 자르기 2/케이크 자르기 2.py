from collections import deque
import sys
inpu = sys.stdin.readline

n = int(input())

cakes = [int(input()) for _ in range(n)]

def dfs(visit, turn, u1, u2): #일단 x를 선택함
    cand = []

    for i in range(n):
        if visit[i]:continue
        if visit[(i-1)%n] or visit[(i+1)%n]:
            cand.append(i)
        
    if not cand:
        return u1

    if turn == 0:
        u2_ind = max(cand, key= lambda x: cakes[x])
        visit[u2_ind] = 1
        res = dfs(visit, 1, u1, u2+cakes[u2_ind])
        visit[u2_ind] = 0
        return res     
    else:
        max_score = 0
        for j in cand:
            visit[j] = 1
            max_score = max(max_score, dfs(visit, 0, u1 + cakes[j], u2))
            visit[j] = 0
        return max_score

ans = 0
for i in range(n):
    visit = [0] * (n)
    visit[i] = 1

    ans = max(ans , dfs(visit, 0, cakes[i], 0))
print(ans)




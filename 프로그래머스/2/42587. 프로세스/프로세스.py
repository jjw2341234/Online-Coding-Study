from collections import deque
def solution(priorities, location):
    answer = 0
    q = deque()
    cnt = 0
    for i,j,in enumerate(priorities):
        q.append([i,j])
    while q:
        now = q.popleft()
        if any(now[1] < queue[1] for queue in q):q.append(now)
        else:
            if now[0] == location: return cnt+1
            cnt+=1
    return cnt
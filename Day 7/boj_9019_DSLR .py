from collections import deque

T = int(input())
for _ in range(T):
    a,b = map(int, input().split())
    visit = [0] * 10001
    q =deque()
    q.append([a, ''])
    visit[a]  = 1
    while q:
        n, cmd = q.popleft()

        if n == b:
            print(cmd)
            break

        d = (n*2) % 10000
        s = (n-1) % 10000
        l = n// 1000 + (n%1000) * 10
        r = n//10 + (n%10) * 1000

        if not visit[d]:
            visit[d] = 1
            q.append([d, cmd + 'D'])
        
        if not visit[s]:
            visit[s] = 1
            q.append([s, cmd + 'S'])

        if not visit[l]:
            visit[l] = 1
            q.append([l, cmd + 'L'])

        if not visit[r]:
            visit[r] = 1
            q.append([r, cmd + 'R'])

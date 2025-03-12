from collections import deque

n,m,r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
box = [[0] * m for _ in range(n)]
q = deque()

index = min(n,m)//2

for i in range(index):
    q.clear()
    q.extend(arr[i][i:m-i])
    q.extend([row[m-1-i] for row in arr[i+1:n-1-i]])
    q.extend(arr[n-1-i][i:m-i][::-1])
    q.extend([row[i] for row in arr[i+1:n-1-i]][::-1])
    q.rotate(-r)

    for j in range(i, m-i):
        arr[i][j] = q.popleft()
    
    for j in range(i+1, n-1-i):
        arr[j][m-1-i] = q.popleft()
    
    for j in range(m-1-i, i-1, -1):
        arr[n-1-i][j] = q.popleft()
    
    for j in range(n-2-i, i, -1):
        arr[j][i] = q.popleft()
    
for i in arr:
    print(*i)
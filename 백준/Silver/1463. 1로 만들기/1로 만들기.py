n = int(input())
visit = [0] * int(1e6+1)
visit[1] = 0
visit[2] = 1
if n <= 2:
    print(visit[n])
    exit(0)
else:
    for i in range(3, n+1):
        visit[i] = visit[i-1] + 1
        if i % 3 == 0:
            visit[i] = min(visit[i], visit[i//3] +1)
        if i % 2 == 0:
            visit[i] = min(visit[i], visit[i//2] + 1)
print(visit[n])
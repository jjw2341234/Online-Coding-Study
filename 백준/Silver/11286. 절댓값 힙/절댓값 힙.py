import heapq
t = int(input())
q = []
for _ in range(t):
    n = int(input())
    if n == 0:
        if q:
            print(heapq.heappop(q)[1])
        else:
            print(0)
    else:
        heapq.heappush(q, (abs(n), n))

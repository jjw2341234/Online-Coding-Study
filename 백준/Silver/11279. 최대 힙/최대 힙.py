import heapq
import sys
input = sys.stdin.readline
t = int(input())
q = []
13
for  _ in range(t):
    n = int(input())
    if q:
        if n == 0:
            print(-heapq.heappop(q))
        else:
            heapq.heappush(q, -n)
    else:
        if n == 0:
            print(0)
        else:
            heapq.heappush(q, -n)
import sys
import heapq
input=sys.stdin.readline
q = []
m = int(input())
for _ in range(m):
    n = int(input())
    if n == 0:
        if len(q):
            print(heapq.heappop(q))
        elif len(q) == 0:
            print(0)
    else:
        heapq.heappush(q, n)
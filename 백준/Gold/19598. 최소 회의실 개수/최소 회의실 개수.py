import heapq

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort()
q = []

heapq.heappush(q, arr[0][1])

for i in range(1, n):
    if q[0] <= arr[i][0]:
        heapq.heappop(q)
    heapq.heappush(q, arr[i][1])
print(len(q))
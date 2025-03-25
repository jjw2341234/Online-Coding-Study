import heapq
n = int(input())

arr = []
for _ in range(n):
    heapq.heappush(arr, int(input()))

cnt = 0
while len(arr) > 1:
    n = heapq.heappop(arr)
    n1 = heapq.heappop(arr)
    s = n+n1
    cnt+=s
    heapq.heappush(arr, s)
print(cnt)
import heapq
moi = lambda: map(int, input().split())
q = []
n,k = moi()
arr = list(moi())
if max(arr) > (n+1)//2:
    print(-1)
    exit()
else:
    for i, v in enumerate(arr):
        heapq.heappush(q, [-v,i+1])
    s, iter = heapq.heappop(q)
    print(iter, end = " ")
    for i in range(n-1):
        s1, iter2 = heapq.heappop(q)
        print(iter2, end = " ")
        if s:
            heapq.heappush(q, [s+1, iter])
        s,iter = s1, iter2
import heapq

n,m = map(int, input().split())
group = [[] for _ in range(200000+1)]

for i in range(n): 
    g, *arr = map(int, input().split())
    for j in arr: 
        heapq.heappush(group[j], i+1)

food = list(map(int, input().split()))
cnt = [0] * (n+1)

for f in food:
    if group[f]:
        cnt[heapq.heappop(group[f])] +=1
for i in range(1, n+1):
    print(cnt[i], end = " ")
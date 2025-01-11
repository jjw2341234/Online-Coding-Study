import heapq

t = int(input())
for _ in range(t):
    n = int(input())
    min_heap,max_heap = [],[]
    visit = [False]*1000001
    for k in range(n):
        alpha, num = input().split(" ")
        num = int(num)
        if alpha == 'I':
            heapq.heappush(min_heap, (num, k))
            heapq.heappush(max_heap, (-num, k))
            visit[k] = True
        else:
            if num == -1:
                while min_heap and not visit[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    visit[min_heap[0][1]] = False
                    heapq.heappop(min_heap)
            else:
                while max_heap and not visit[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    visit[max_heap[0][1]] = False
                    heapq.heappop(max_heap)

    while min_heap and not visit[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not visit[max_heap[0][1]]:
        heapq.heappop(max_heap)

    if not len(min_heap) and not len(max_heap):
        print("EMPTY")
    else:
        print(-max_heap[0][0], min_heap[0][0])


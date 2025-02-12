n = int(input())
res=  list(map(int, input().split()))

arr = [i+1 for i in range(n)]

def card_shuffle(prev, i, k):
    if i > k+1:
        return prev
    if i == 1:
        cnt = 2 **k
    else:
        cnt = 2 ** (k-i+1)
    size = len(prev)
    next=  prev[size - cnt:]
    return card_shuffle(next, i+1, k) + prev[:size-cnt]

k1 = 1
while 2**k1 < n:
    first = card_shuffle(arr, 1, k1)
    k2 = 1
    while 2 ** k2 < n:
        second = card_shuffle(first, 1, k2)
        if second == res:
            print(k1, k2)
            break
        k2 += 1
    k1 += 1
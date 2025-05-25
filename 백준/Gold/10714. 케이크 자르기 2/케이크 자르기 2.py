import sys
from functools import cache
input = sys.stdin.readline
n = int(input())
cakes = [int(input()) for _ in range(n)]
res = 0
res2 = 0
def ioi(l,r):
    if l == r:
        return -1,-1
    if cakes[l] > cakes[r]:
        return (l-1) % n, r
    else:
        return l % n, (r+1) %n
@cache
def cutting(l, r):
    l,r = ioi(l,r)
    if l == -1 and r == -1:
        return 0
    if l == r:
        return cakes[l]
    res = 0
    res = max(res, cutting((l-1) %n, r) + cakes[l]) 
    res = max(res, cutting(l, (r+1) % n) + cakes[r])
    return res
ans = 0
for i in range(n):
    ans = max(ans, cutting((i-1)%n, (i+1) % n) + cakes[i])
print(ans)
import sys
input = sys.stdin.readline
moi = lambda: map(int, input().split())
n,a,b = moi()
arr = list(moi())
arr.sort()
def sleep(k, t):
    a_ = a - t//b
    time = 0 
    cnt = 0
    for i in range(k):
        if time + a <= arr[i]:
            time+=a
            cnt+=1
    time += t # t만큼 수면
    for i in range(k, n):
        if time + a_ <= arr[i]:
            time+= a_
            cnt+=1
    return cnt
ans = 0
for i in range(n):
    for j in range(0, (a-1) * b + 1, b):
        ans = max(ans, sleep(i,j))
print(ans)
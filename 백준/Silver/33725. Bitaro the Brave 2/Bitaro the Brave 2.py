import sys

N = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

c = [0] * (N+1)
d = [0] * (N)

for i in range(N):
    c[i+1] = c[i] + b[i]
    d[i] = a[i] - c[i]

leftm = [0] * N
rightm = [0] * N

leftm[0] = d[0]
rightm[N-1] = d[N-1]

#현재 leftm의 경우, leftm의 값과 d의 값을 비교해서 좋은 값을 가져오는것이 목표이다.

for i in range(1, N):
    leftm[i] = max(leftm[i-1], d[i-1])

for i in range(N-2, -1, -1):
    rightm[i] =max(rightm[i+1],d[i])

ans = float("inf")

for i in range(N):
    k = max(leftm[i]- c[N], rightm[i]) + c[i]
    ans = min(k, ans)
print(ans)
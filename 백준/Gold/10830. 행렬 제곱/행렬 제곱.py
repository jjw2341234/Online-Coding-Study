import sys
input = sys.stdin.readline
n,b = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

def multi(A,B):
    X = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                X[i][j] += A[i][k] * B[k][j] % 1000
    return X

def square(A, b):
    if b == 1:
        return A
    tmp = square(A, b//2)
    if b % 2  == 0:
        return multi(tmp, tmp)
    else:
        return multi(multi(tmp, tmp), A)
res = square(arr, b)
for i in range(n):
    for j in range(n):
        res[i][j]  = res[i][j] % 1000
for k in res:
    print(*k)
    
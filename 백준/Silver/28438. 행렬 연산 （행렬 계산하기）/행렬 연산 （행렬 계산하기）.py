n,m,q = map(int, input().split())
arr = [[0] * m for _ in range(n)]
max_num = max(n,m)
cummula = [[0] * max_num for _ in range(2)]

for _ in range(q):
    c, r,v = map(int, input().split())
    cummula[c-1][r-1]+=v

for c in range(2):
    if c== 0:
        for i in range(n):
            for j in range(m):
                arr[i][j] += cummula[c][i]
    elif c:
        for i in range(m):
            for j in range(n):
                arr[j][i] += cummula[c][i]

for i in range(n):
    print(* arr[i])
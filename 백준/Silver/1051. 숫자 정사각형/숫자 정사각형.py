moi = lambda: map(int, input().split())

n,m = moi()

K = min(n,m)
max_n = max(n,m)
arr = [input().rstrip() for _ in range(n)]

for k in range(K, 0, -1):
    for i in range(n-k):
        for j in range(m-k):
            if arr[i][j] == arr[i+k][j] == arr[i][j+k] == arr[i+k][j+k]:
                print((k+1) **2)
                exit()
print(1)

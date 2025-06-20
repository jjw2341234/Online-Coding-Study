n,m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
withdp = [[0] + [-1e9] * m  for _ in range(n+1)]
withoutdp = [[0] + [-1e9] * m  for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, min(m, (i+1)//2) + 1):
        withoutdp[i][j] = max(withoutdp[i-1][j], withdp[i-1][j])
        withdp[i][j] = max(withoutdp[i-1][j-1], withdp[i-1][j]) + arr[i-1]
print(max(withdp[n][m], withoutdp[n][m]))
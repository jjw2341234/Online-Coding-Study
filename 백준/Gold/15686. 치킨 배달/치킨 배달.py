from itertools import combinations
n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
house = []
chicken = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            chicken.append([i,j])
        elif arr[i][j] == 1:
            house.append([i,j])

res = int(1e9)
chk = combinations(chicken, m)
for c in chk:
    s = 0
    for h in house:
        ch_len = int(1e9)
        for j in range(m):
            ch_len = min(ch_len, abs(h[0] - c[j][0]) + abs(h[1] - c[j][1]))
        s+= ch_len
    res = min(res, s)
print(res)
        


import sys
input = sys.stdin.readline

def parity_check(a,b):
    score = 0
    for i in range(m):
        if a[i] == b[i]:
            score+=1
    return score

moi = lambda: map(int, input().split())
n,m = moi()
ans = list(moi())
query = [list(moi()) for _ in range(n)]
ans_val = 0
res_val = 0
for i in range(n):
    ans_val = max(ans_val, parity_check(ans, query[i]))
for i in range(1, 1<<n):
    temp  = []
    for j in range(n):
        if i &(1 << j):
            temp.append(j)
    if len(temp) == 1 or not len(temp) % 2:
        continue
    tmp = [0] * m
    for j in range(m):
        cnt = [0,0]
        for k in range(len(temp)):
            cnt[query[temp[k]][j]]+=1
        tmp[j] = cnt.index(max(cnt))
    res_val = max(res_val, parity_check(tmp, ans))
if res_val > ans_val:
    print(1)
else:
    print(0)
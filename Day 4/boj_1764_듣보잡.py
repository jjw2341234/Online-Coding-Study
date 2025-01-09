n,m = map(int, input().split())
di = dict()

for _ in range(n):
    a = input()
    if a not in di:
        di[a]=1
res = []
for _ in range(m):
    a = input()
    if a not in di:
        di[a]=1
    else:
        di[a]+=1
for i,j in di.items():
    if j > 1:
        res.append(i)
res.sort()
print(len(res))
for i in range(len(res)):
    print(res[i])
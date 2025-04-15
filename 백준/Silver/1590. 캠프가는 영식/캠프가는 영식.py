moi = lambda: map(int, input().split())

n,t = moi()

graph = [[] for _ in range(n)]

res = []
for i in range(n):
    s,l,c = moi()

    lista = [(l*i)+s for i in range(c)]    
    if lista[-1] < t:
        continue
    s,e = 0, c-1
    
    while s<=e:
        mid = (s+e)//2
        if lista[mid] < t:
            s = mid+1
        else:
            e = mid-1
    res.append(lista[s] - t)

if res:
    print(min(res))
else:
    print(-1)

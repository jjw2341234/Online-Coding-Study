moi = lambda: map(int, input().split())

n,q,u,v = moi()

arr = list(moi())

for _ in range(q):
    c,a,b = moi()
    if c == 0:
        a-=1
        b-=1
        max_val = float('-inf')

        for i in range(a,b+1):
            total = 0
            for j in range(i, b+1):
                total+= arr[j]
                val = u * total + v * (j-i)
                max_val = max(val, max_val)
        print(max_val)
    else:
        a-=1
        arr[a] = b


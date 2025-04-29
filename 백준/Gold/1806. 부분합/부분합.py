moi = lambda: map(int, input().split())
n,m = moi()
arr = list(moi())
s = 0
ans = float('inf')
l,r = 0,0
while 1:
    if s>= m:
        ans = min(ans, r-l)
        s -= arr[l]
        l+=1
    elif r == n:
        break
    else:
        s+= arr[r]
        r+=1

if ans == float('inf'):
    print(0)
else:
    print(ans)
x,y,c = map(float, input().split())
high = min(x,y)
low = 1
ans = 0 

while low + 0.001 <= high:
    w = (high + low)/2
    h1 = (x**2 - w**2)**0.5
    h2 = (y**2 - w**2)**0.5
    check = h1*h2 / (h1 + h2)
    if check >= c:
        ans = w
        low = w
    else:
        high = w
print(ans)
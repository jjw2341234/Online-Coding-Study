import math

t = int(input())
for _ in range(t):
    m,n,x,y = map(int, input().split())
    gcd = math.gcd(m,n)
    lcm = math.lcm(m,n)
    ans = x
    while ans <= lcm:
        if (ans-1) % n +1 == y:
            break
        ans += m
    if ans > lcm:
        print(-1)
    else:
        print(ans)
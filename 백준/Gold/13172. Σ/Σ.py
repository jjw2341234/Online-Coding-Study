import math
t = int(input())
ans = 0
mod = 1000000007
for _ in range(t):
    s,n = map(int, input().split())
    s,n = s//math.gcd(s,n), n//math.gcd(s,n)
    ans += (n*pow(s,-1,mod)) % mod
    ans %= mod
print(ans)

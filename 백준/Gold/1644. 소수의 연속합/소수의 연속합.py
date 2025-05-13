import math
import sys
input = sys.stdin.readline
n = int(input())
arr = [True] * (n+1)
arr[0], arr[1] = False, False
cnt = 0
prime_num = []
for i in range(2, int(math.sqrt(n))+1):
    if arr[i]:
        j = 2
        while i*j <=n:
            arr[i*j] = False
            j+=1
for i in range(2, n+1):
    if arr[i]:
        prime_num.append(i)
        
l,r = 0,0
ans = 0
while r<= len(prime_num):
    sums = sum(prime_num[l:r])
    if sums<=n:
        r+=1
        if sums == n:
            ans+=1
    else:
        l+=1
print(ans)
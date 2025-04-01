import math
import sys
from collections import defaultdict
input = sys.stdin.readline

moi = lambda : map(int, input().split())

n,p,q = moi()

arr = defaultdict(int)
arr[0] = 1
def dp(n):
    
    if arr[n] != 0:
        return arr[n]
    
    arr[n] = dp(math.floor(n//q)) + dp(math.floor(n//p))
    return arr[n]

print(dp(n))

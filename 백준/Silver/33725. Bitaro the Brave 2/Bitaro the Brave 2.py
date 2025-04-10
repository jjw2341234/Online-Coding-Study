import sys

input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

def can_clear(x, a,b, n):
    for j in range(n):
        power = x
        success = True

        for i in range(j, n):
            if power < a[i]:
                success = False
                break
            power+= b[i]
        
        if success:
            for i in range(j):
                if power < a[i]:
                    success = False
                    break
                power+= b[i]
        
        if success:
            return True
    return False


lo = 0
hi = int(10**9)

while lo < hi:
    mid = (lo + hi) //2
    if can_clear(mid, arr, arr2, n):
        hi  = mid
    else:
        lo = mid+1
print(lo)


import sys
input = sys.stdin.readline
#recursion error 방지
sys.setrecursionlimit(10**9)
arr = []
while 1:
    try:
        x = int(input())
        arr.append(x)
    except:
        break
def solution(A):
    if len(A) == 0:
        return 
    left, right = [],[]
    mid = A[0]
    for i in range(1, len(A)):
        if mid < A[i]:
            right = A[i:]
            left = A[1:i]
            break
    else:
        left = A[1:]
    solution(left)
    solution(right)
    print(mid)
solution(arr)
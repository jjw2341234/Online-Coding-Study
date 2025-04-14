#파라매트릭 서치를 이용해서 푸는 방식
#a,b를 각각 범위라고 생각하고 풀어라
#a에서 값을 구할때는 처음 나오는 경우를 설정(a<=)
#b에서 값을 구할때도 처음 나오는 경우를 설정(b<=)
import sys
input = sys.stdin.readline

n,m = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()

def left_binary_search(num):
    s,e = 0, n-1
    while s<=e:
        mid = (s+e)//2
        if arr[mid] < num:
            s = mid+1
        else:
            e = mid-1
    return s

def right_binary_search(num):
    s,e = 0, n-1
    while s<=e:
        mid = (s+e)//2
        if arr[mid] <= num:
            s = mid+1
        else:
            e = mid-1
    return e

for _ in range(m):
    a,b = map(int, input().split())
    max_a, max_b = left_binary_search(a), right_binary_search(b)
    print(max_b - max_a + 1)
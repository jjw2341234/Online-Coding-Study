import sys
input =  sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
res = 0
sum_list = []

if n == 1:
    arr.sort()
    for i in range(0, 5):
        res+=  arr[i]
else:
    sum_list.append(min(arr[0], arr[-1]))
    sum_list.append(min(arr[2], arr[3]))
    sum_list.append(min(arr[1], arr[-2]))
    sum_list.sort()
    min1 = sum_list[0]
    min2 = sum_list[1] + sum_list[0]
    min3 = sum(sum_list)

    n1 = (n-2)**2 + 4*(n-1) * (n-2)
    n2 = 4* (2*n - 3)
    n3 = 4

    res += n1 * min1
    res += n2 * min2
    res += n3 * min3
print(res)
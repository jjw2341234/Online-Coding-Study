n = int(input())
arr = list(map(int, input().split()))
lis = [arr[0]]

def binary_search(target):
    s,e = 0, len(lis)-1
    while s <= e:
        mid = (s+e)//2
        if lis[mid] == target:
            return mid
        elif target < lis[mid]:
            e = mid-1
        else:
            s = mid+1
    return s

dp = [(0, arr[0])]
for i in range(1, n):
    if lis[-1] < arr[i]:
        lis.append(arr[i])
        dp.append((len(lis)-1, arr[i]))
    else:
        s = binary_search(arr[i])
        lis[s] = arr[i]
        dp.append((s, arr[i]))
print(len(lis))

last_idx = len(lis) - 1
res = []
for i in range(len(dp)-1, -1, -1):
    # i번째 값의 index와 마지막 인덱스값과 같다면
    if dp[i][0] == last_idx:
        res.append(dp[i][1])
        last_idx-=1

print(*res[::-1])
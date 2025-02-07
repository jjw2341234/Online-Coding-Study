n = int(input())
arr = list(map(int, input().split()))
arr.sort()
if n >2:
    res = 2
    for i in range(n-2):
        end = i+2
        while True:
            if arr[i] + arr[i+1] > arr[end]:
                res = max(res, end-i+1)
                end+=1
                if end == n: break
            else:break
    print(res)
else: print(n)
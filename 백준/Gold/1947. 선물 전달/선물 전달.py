n = int(input())
max_num = 10**9
arr = [0] * (n+1)
arr[1] = 0
if n>=2:arr[2] = 1

for i in range(3, n+1):
    arr[i] = (arr[i-2] + arr[i-1]) * (i-1) % max_num
print(arr[n])
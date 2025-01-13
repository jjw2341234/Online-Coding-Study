t = int(input())
for _ in range(t):
    arr = [0] * 101
    arr[0] = 0
    arr[1] = 1 
    arr[2] = 1

    n = int(input())

    for i in range(3, n+1):
        arr[i] = arr[i-2] + arr[i-3]
    print(arr[n])
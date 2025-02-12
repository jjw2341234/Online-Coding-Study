def cal(arr):
    stack = []
    res = 0
    arr.append(0)
    for i in range(len(arr)):
        start = i
        value = arr[i]
        while stack and stack[-1][1] >= value:
            start, height = stack.pop()
            res = max(res, (i-start) * height)
        stack.append((start, value))
    print(res)
while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break
    cal(arr[1:])
k = int(input())
arr = list()
for _ in range(k):
    n = int(input())
    if n == 0:
        arr.pop()
    else:
        arr.append(n)
print(sum(arr))

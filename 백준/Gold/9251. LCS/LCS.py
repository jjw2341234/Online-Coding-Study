str_a = list(' '+ input().rstrip())
str_b = list(' '+ input().rstrip())
arr = [[0] * len(str_b) for _ in range(len(str_a))]
for i in range(1, len(str_a)):
    for j in range(1, len(str_b)):
        if str_a[i] == str_b[j]:
            arr[i][j] = arr[i-1][j-1] + 1
        else:
            arr[i][j] = max(arr[i-1][j], arr[i][j-1])
print(arr[-1][-1])
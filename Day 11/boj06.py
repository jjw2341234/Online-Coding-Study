n = int(input())
ar = list(map(int, input().split()))
arr=  list(set(ar))
arr.sort()
dic = {arr[i]: i for i in range(len(arr))}

for i in ar:
    print(dic[i], end = " ")
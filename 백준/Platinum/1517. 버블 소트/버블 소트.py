n = int(input())
arr = list(map(int, input().split()))
arr.insert(0,0)
result = 0
tmp = [0] * (n+1)
def merge_sort(l, r):
    global result
    if r < l + 1: return
    m  = l + (r-l)//2
    merge_sort(l, m)
    merge_sort(m+1, r)
    for i in range(l, r+1):
        tmp[i] = arr[i]
    k = l
    index1 = l
    index2 = m+1
    while index1 <= m and index2 <= r:
        if tmp[index1] > tmp[index2]:
            arr[k] = tmp[index2]
            result += index2 - k
            index2+=1
            k+=1

        else:
            arr[k] = tmp[index1]
            index1+=1
            k+=1
    
    while index2 <=r:
        arr[k] = tmp[index2]
        k+=1
        index2+=1
    while index1 <=m:
        arr[k] = tmp[index1]
        k+=1
        index1+=1


merge_sort(1, n)
print(result)

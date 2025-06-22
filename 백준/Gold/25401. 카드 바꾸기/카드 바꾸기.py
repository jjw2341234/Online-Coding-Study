n = int(input())
arr =list(map(int, input().split()))
cnt = int(1e9)
for i in range(n):
    ind = []
    for j in range(i+1, n):
        if (arr[j] - arr[i]) % (j-i) == 0:
            tmp = (arr[j] - arr[i])//(j-i)
            ind.append(tmp)
    
    ind = list(set(ind))
    for k in ind:
        tmp_cnt = 0
        for j in range(i+1, n):
            amnt = j-i
            if arr[i] + amnt * k != arr[j]:
                tmp_cnt+=1
        for j in range(i):
            amnt = j-i
            if arr[i] + amnt * k != arr[j]:
                tmp_cnt+=1
        cnt = min(tmp_cnt, cnt)
print(cnt)

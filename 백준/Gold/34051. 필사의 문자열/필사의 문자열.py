n = int(input())
str1 = input().strip()
res = str1[::]
flg = 0
for i in range(n-1):
    idx = 0
    for j in range(i+1, n):
        if str1[i] < str1[j]:
            idx = j
            flg = 1 
    if flg: 
        for j in range(i+1, n):
            if str1[i] < str1[j]:
                idx = j
            tmp = str1[:i] + str1[i:idx+1][::-1]+ str1[idx+1:]
            res = max(tmp, res)
        break
print(res)
            
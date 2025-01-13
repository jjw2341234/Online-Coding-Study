t = int(input())
for _ in range(t):
    n  = int(input())
    dic = dict()
    for i in range(n):
        a,b = input().split()
        if b not in dic:
            dic[b] = 1
        else:
            dic[b]+=1
    res = 1
    for i in dic.values():
        res *=(i+1)
    res-=1
    print(res) 
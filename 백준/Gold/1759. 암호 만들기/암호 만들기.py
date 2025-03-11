n,m = map(int, input().split())

str = list(input().split())
str.sort()
res_list = []
def pwd(x, res):
    global res_list
    if len(res) == n:
        rcnt = 0
        for r in res:
            if r in "aeiou":
                rcnt+=1
        if n-rcnt >= 2 and rcnt:
            if ''.join(res) not in res_list:
                res_list.append(''.join(res))
            return 
    for i in range(x, len(str)):
        if str[i] not in res:
            res.append(str[i])
            pwd(i+1, res)
            res.pop()
pwd(0, [])
for r in res_list:
    print(r)

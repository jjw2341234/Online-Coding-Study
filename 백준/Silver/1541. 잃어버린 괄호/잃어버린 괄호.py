import re
string = input()
st = string.split("-")
num = []
for s in st:
    res = 0
    tmp = s.split('+')
    for j in tmp:
        res+= int(j)
    num.append(res)

n  = num[0]
for i in range(1, len(num)):
    n-=num[i]
print(n)
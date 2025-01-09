import re
string = input()
st = string.split("-") #해당 문제의 키 포인트, -를 기준으로 괄호를 만들어야 최소값을 만듦.
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
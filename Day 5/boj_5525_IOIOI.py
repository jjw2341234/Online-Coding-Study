n = int(input())
length = int(input())
s = input()
cursor, cnt, res = 0, 0, 0

while cursor < length-1:
    if s[cursor: cursor+3] == "IOI":
        cnt+=1
        cursor+=2
        if cnt == n:
            res+=1
            cnt-=1
    else:
        cursor+=1
        cnt = 0
print(res)
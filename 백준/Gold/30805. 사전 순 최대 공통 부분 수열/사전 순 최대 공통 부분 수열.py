n = int(input())
s1 = list(map(int, input().split()))
m = int(input())
s2 = list(map(int, input().split()))
com = set(s1) & set(s2)
res = []
while com:
    maxv = max(com)
    max_s1_ind = s1.index(maxv)
    max_s2_ind = s2.index(maxv)
    res.append(maxv)
    s1 = s1[max_s1_ind+1:]
    s2 = s2[max_s2_ind+1:]
    com = set(s1)&set(s2)
print(len(res))
print(*res)
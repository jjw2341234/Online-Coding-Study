n = int(input())
dic = dict()
alpha = []
for _ in range(n):
    alpha.append(input().strip())
for i in range(n):
    for j in range(len(alpha[i])):
        if alpha[i][j] in dic:
            dic[alpha[i][j]] += 10**(len(alpha[i]) - j - 1)
        else:
            dic[alpha[i][j]] = 10**(len(alpha[i]) - j - 1)

val = []
for v in dic.values():
    val.append(v)
val.sort(reverse=True)
num_list = [9-i for i in range(len(val))]
res = 0
for i in range(len(val)):
    res+= num_list[i] * val[i]
print(res)
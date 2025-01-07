import math
n  = list(input())
cnt = 0
for i in range(math.ceil(len(n)/2)):
    if n[i] == n[len(n)-1-i]:
        cnt+=1
if cnt == math.ceil(len(n)/2):
    print(True)
else:
    print(False)
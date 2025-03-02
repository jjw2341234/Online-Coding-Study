n = int(input())
now = 1
stack = []
ans = []
chk = True
for _ in range(n):
    num = int(input())
    while now <= num:
        stack.append(now)
        ans.append('+')
        now+=1
    if stack[-1] == num:
        stack.pop()
        ans.append('-')
    else:
        chk = False
if chk:
    for i in ans:
        print(i)
else:
    print("NO")

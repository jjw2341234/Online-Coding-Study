st = input().rstrip()
stack = []
cnt = 0
for i in range(len(st)):
    if st[i] == "(":
        stack.append("(")
    elif st[i] == ')':
        if st[i-1] == "(":
            stack.pop()
            cnt+= len(stack)
        else:
            stack.pop()
            cnt+=1
print(cnt)
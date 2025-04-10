string = input().rstrip()
stack = []
ans = 0
tmp = 1
for i in range(len(string)):
    if string[i] == '(':
        stack.append(string[i])
        tmp*=2
    elif string[i] == ')':
        if not stack or stack[-1] == '[':
            ans = 0
            break

        if string[i-1] == '(':
            ans+=tmp
        stack.pop()
        tmp//=2
    elif string[i] == '[':
        stack.append(string[i])
        tmp*=3
    else:
        if not stack or stack[-1] == '(':
            ans = 0
            break
        if string[i-1] == '[':
            ans+=tmp
        stack.pop()
        tmp//=3 

if stack:
    print(0)
else:
    print(ans)
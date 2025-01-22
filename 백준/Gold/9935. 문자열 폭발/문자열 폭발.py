str = input().strip()
str1 = input().strip()
stack = []

for i in range(len(str)):
    stack.append(str[i])
    if ''.join(stack[-len(str1):]) == str1:
        for j in range(len(str1)):
            stack.pop()
if len(stack):
    print(''.join(stack))
else:
    print("FRULA")

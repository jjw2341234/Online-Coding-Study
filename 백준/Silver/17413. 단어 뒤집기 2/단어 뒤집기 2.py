import sys
input = sys.stdin.readline
string = input().rstrip() + " "
stack = []
res = ""
tag = 0
for s in string:
    if s == '<':
        tag = 1
        for _ in range(len(stack)):
            res+= stack.pop()
    stack.append(s)
    if s == '>':
        tag = 0
        for _ in range(len(stack)):
            res+= stack.pop(0)
    elif s == " " and not tag:
        stack.pop()
        for _ in range(len(stack)):
            res+= stack.pop()
        res+= " "
print(res)
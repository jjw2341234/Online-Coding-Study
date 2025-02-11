n = int(input())
answer = 0
stack = []
finish = 0
for i in range(n):
    start = i
    value = int(input())
    while stack and stack[-1][1] >=value:
        start, prevalue = stack.pop()
        finish = max(finish, (i-start) * prevalue)
    stack.append([start, value])

while stack:
    start, value = stack.pop()
    finish = max(finish, (n-start) * value)
print(finish)
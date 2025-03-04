s = list(input())
n = int(input())
ind = len(s)
text = []
for _ in range(n):
    a = list(input().split())
    if a[0] == 'L' and s:
        text.append(s.pop())
    elif a[0] == 'D' and text:
        s.append(text.pop())
    elif a[0] == 'B' and s:
        s.pop()
    elif a[0] == 'P':
        s.append(a[1])
print(''.join(s+list(reversed(text))))
import sys

input = sys.stdin.readline
t = int(input())
res = set()
for _ in range(t):
    command = list(input().split())
    if len(command) == 1:
        s = command[0]
    else:
        s,n = command[0], command[1]
        n = int(n)
    if s == 'add':
        res.add(n)
    elif s == 'check':
        if n in res:
            print(1)
        else:
            print(0)
    elif s == 'remove':
        if n in res:
            res.discard(n)
    elif s == 'toggle':
        if n not in res:
            res.add(n)
        else:
            res.discard(n)
    elif s == 'all':
        res = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
    elif s == 'empty':
        res.clear()
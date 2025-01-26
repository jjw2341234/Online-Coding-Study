from collections import deque
import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    commands = input().rstrip()
    n = int(input())
    st = input().rstrip()[1:-1].split(",")
    q =deque(st)
    
    if n == 0:
        q = deque()
    check = 0
    check2 = 0
    for command in commands:
        if command == 'R':
            check2+=1
        elif command == 'D':
            if not q:
                print('error')
                check = 1
                break
            else:
                if check2 % 2 :
                    q.pop()
                else:
                    q.popleft()
    if not check:
        if check2 % 2:
            q.reverse()
        print("[" + ",".join(q) + "]")
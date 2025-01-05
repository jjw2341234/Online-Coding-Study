import sys
input = sys.stdin.readline
n = int(input())
for _ in range(n):
    tmp  = 0
    cnt = 0
    mov = 0
    s,e = map(int, input().split())
    dist = e - s
    while tmp < dist:
        cnt+=1
        if cnt % 2:
            mov+=1
        tmp += mov
    print(cnt)
        


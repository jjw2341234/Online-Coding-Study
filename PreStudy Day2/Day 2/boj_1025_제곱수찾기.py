import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(input().strip()) for _ in range(n)]
res = -1
def sqrt(x):
    x = int(x)
    return int(x ** 0.5) ** 2 == x
for i in range(n):
    for j in range(m):
        for r in range(-n, n):
            for c in range(-m, m):
                x = i
                y = j
                value = ''
                if r == 0 and c == 0: 
                    continue
                while 0<=x<n and 0<=y<m:
                    value+= arr[x][y]
                    if sqrt(value):
                        res = max(res, int(value))
                    x += r
                    y += c
print(res)

import sys

arr = bytearray(2 << 22)
s = ''
while True:
    c = sys.stdin.read(1)
    if c.isnumeric():
        s += c
    else:
        n = int(s)
        d, r = n//8, n%8
        if not (arr[d] & (1 << r)):
            print(n, end=' ')
            arr[d] |= (1 << r)
        s = ""
        if c!= " ":
            break

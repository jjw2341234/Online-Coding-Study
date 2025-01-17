n,m,b = map(int, input().split())
blocks = [list(map(int, input().split())) for i in range(n)]
ans = int(1e9)
glevel = 0
for i in range(0, 257):
    use_block = 0
    take_block = 0
    for x in range(n):
        for y in range(m):
            if blocks[x][y] > i:
                take_block+= blocks[x][y] - i
            else:
                use_block+= i - blocks[x][y]
    if use_block > take_block + b:
        continue

    count = 2* take_block + use_block 
    if ans >= count:
        ans = count
        glevel = i
print(ans, glevel)
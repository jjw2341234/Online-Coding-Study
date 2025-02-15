n,m = map(int, input().split())
paper = []
for _ in range(n):
    paper.append(list(map(int, input().rstrip())))

ans = []
for i in range(1 << n * m):
    total = 0
    for row in range(n):
        row_sum = 0
        for col in range(m):
            idx = m * row + col
            if i & (1 << idx) != 0:
                row_sum= row_sum * 10 + paper[row][col]
            else:
                total+= row_sum
                row_sum = 0
        total+= row_sum

    for col in range(m):
        col_sum = 0
        for row in range(n):
            idx = m*row + col
            if i& (1<<idx) == 0:
                col_sum = col_sum * 10 + paper[row][col]
            else:
                total+= col_sum
                col_sum = 0
        total+= col_sum
    ans.append(total)
print(max(ans))
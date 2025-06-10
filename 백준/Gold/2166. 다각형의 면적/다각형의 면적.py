n = int(input())
moi = lambda: map(int, input().split())
dots = [tuple(moi()) for _ in range(n)]
dots.append(dots[0])
res = 0
for i in range(n):
    res += (dots[i][0] * dots[i+1][1] - dots[i][1] *  dots[i+1][0])
print(round(abs(res) / 2, 2))
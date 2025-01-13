n = int(input())
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    iteration = int(input())
    cnt = 0
    for _ in range(iteration):
        rx, ry, r = map(int, input().split())
        distsr = (x1-rx)**2 + (y1 - ry) ** 2
        dister = (x2-rx)**2 + (y2 - ry) ** 2
        distr = r**2
        if distsr < distr and dister < distr:
            pass
        elif distsr < distr or dister < distr:
            cnt+=1
    print(cnt)

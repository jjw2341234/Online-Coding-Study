n = int(input())
for i in range(int(n//2), n):
    if i + sum(list(map(int, str(i)))) == n:
        print(i)
        break
else:
    print(0)
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
common = set(a) & set(b)
res = []
while common:
    max_value = max(common)

    ind1 = a.index(max_value)
    ind2 = b.index(max_value)
    res.append(max_value)
    a = a[ind1+1:]
    b = b[ind2+1:]
    common = set(a) & set(b)
print(len(res))
print(' '.join(map(str, res)))
from collections import defaultdict
from itertools import product
target = int(input())
n = int(input())
if n:missing = list(map(int, input().split()))
else:missing = []
min_press = abs(target - 100)
for length in range(1, 7):#1~6의 자리까지 값이 나올수 있음.
    for cam in product([str(i) for i in range(10) if i not in missing], repeat=length):
        num = int(''.join(cam))
        min_press = min(abs(target - num) + length, min_press)
print(min_press)
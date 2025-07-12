from collections import defaultdict
from bisect import bisect_left
import sys
input = sys.stdin.readline

A = input().strip()
B = input().strip()

a_cur = a_min = 0
a_count = defaultdict(int)
for ch in A:
    a_cur += 1 if ch == '(' else -1
    a_min = min(a_min, a_cur)
    if a_min >= 0:
        a_count[a_cur] += 1

b_cur = b_min = 0
b_groups = defaultdict(list)
for ch in B:
    b_cur += 1 if ch == '(' else -1
    b_min = min(b_min, b_cur)
    b_groups[b_cur].append(b_min)

b_index = {}
for b_val, mins in b_groups.items():
    mins.sort()
    b_index[b_val] = mins  

ans = 0
for a_bal, a_cnt in a_count.items():
    b_target = -a_bal
    threshold = -a_bal
    if b_target in b_index:
        mins = b_index[b_target]
        idx = bisect_left(mins, threshold)
        ans += (len(mins) - idx) * a_cnt

print(ans)

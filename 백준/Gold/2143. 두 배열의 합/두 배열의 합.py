import bisect

target = int(input())

n = int(input())

arr1 = list(map(int, input().split()))

m = int(input())

arr2 = list(map(int, input().split()))

dp1 = []
dp2 = []

for i in range(n):
    for j in range(i+1, n+1):
        dp1.append(sum(arr1[i:j]))

for i in range(m):
    for j in range(i+1, m+1):
        dp2.append(sum(arr2[i:j]))


dp1 = sorted(dp1)
dp2 = sorted(dp2)

#이제 가장 처음 나오는 값과 끝에 나오는 값을 찾아야 한다.
ans = 0
for i in range(len(dp1)):
    sec_target = target - dp1[i]
    l = bisect.bisect_left(dp2, sec_target)
    r = bisect.bisect_right(dp2, sec_target)
    ans += (r-l)
print(ans)
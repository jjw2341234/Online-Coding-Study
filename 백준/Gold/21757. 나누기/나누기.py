n = int(input())
arr = list(map(int, input().split()))
prefix_sum = 0
cnt1 = 0
cnt2 = 0
ans = 0

targert = sum(arr)//4


if sum(arr) % 4:
    print(0)
    exit()

for i in range(len(arr)-1):
    prefix_sum+= arr[i]
    if prefix_sum == targert * 3: ans+=cnt2 #마지막의 경우, 그전의 값들의 갯수에 따라 달라질수 밖에 없다.
    if prefix_sum == targert * 2: cnt2+=cnt1
    if prefix_sum == targert: cnt1+=1

print(ans)

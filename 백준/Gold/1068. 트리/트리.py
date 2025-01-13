import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
m = int(input())

def dfs(num):
    arr[num] = -100
    for i in range(len(arr)):
        if num == arr[i]:
            dfs(i)

dfs(m)
cnt = 0
for i in range(len(arr)):
    if arr[i] != -100 and i not in arr:
        cnt+=1
print(cnt)
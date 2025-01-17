#다시 풀기


n = int(input())
arr = list(map(int, input().split()))
dic = {}
l = 0
count = 0
ans = -10000
for r in range(n):
    if arr[r] not in dic:
        dic[arr[r]] = 1
        count+=1
    else:
        dic[arr[r]]+=1
    if count > 2:
        dic[arr[l]]-=1
        if not dic[arr[l]]:
            del dic[arr[l]]
            count-=1
        l+=1
    ans = max(ans, r-l+1)
print(ans)
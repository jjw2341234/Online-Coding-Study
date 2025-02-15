n = int(input())
arr = list(input().rstrip())
res = int(-1e9)
def cal(v,a,b):
    if b == '+':
        return int(a) + int(v)
    if b == '-':
        return int(v) - int(a)
    if b == '*':
        return int(v) * int(a)


def dfs(idx, val):
    global res
    if idx == n-1:
        res = max(res, val)
        return
    if idx + 2 < n:
        new_val = cal(val, arr[idx+2], arr[idx+1])
        dfs(idx+2, new_val)
    if idx +4 < n:
        new_val = cal(val, cal(arr[idx+2], arr[idx+4], arr[idx+3]), arr[idx+1])
        dfs(idx+4, new_val)

dfs(0, int(arr[0]))
print(res)
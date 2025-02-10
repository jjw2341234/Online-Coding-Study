n = int(input())
op = list(map(str, input().split()))
nums = [i for i in range(10)]

def check(x,y,op):
    if op == '>' and x < y:
        return False
    if op == '<' and x > y:
        return False
    return True

res = []
res1 = []
def dfs(level):
    if level == n+1:
        res1.append(''.join(map(str, res)))
        return
    for i in range(10):
        if i not in res and (len(res) == 0 or check(res[level -1], i, op[level-1])):
            res.append(i)
            dfs(level+1)
            res.pop()
dfs(0)
print(res1[-1])
print(res1[0])
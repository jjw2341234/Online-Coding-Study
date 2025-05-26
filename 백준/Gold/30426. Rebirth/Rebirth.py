import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
moi = lambda: map(int, input().split())
n,m,k = moi()
dp = [[0] * n for _ in range(k)]
def dfs(s,e):
    if s == k:
        if e == 0:return 1
        return -1
    
    if dp[s][e]:return dp[s][e]
    
    cor = (e+move[s][0]) % n
    wro = (e+move[s][1]) % n

    if not wrongspace[cor]:
        if dfs(s + 1, cor) == 1:
            dp[s][e] = 1
            return 1

    if not wrongspace[wro]:
        if dfs(s + 1, wro) == 1:
            dp[s][e] = 1
            return 1

    dp[s][e] = -1
    return -1


move = [list(moi()) for _ in range(k)]
L = int(input())
wrongspace = [0] * n

for _ in range(L):
    wrong = int(input())
    wrongspace[wrong] = 1

result = dfs(0, m)
print("utopia" if result == 1 else "dystopia")

import sys
sys.setrecursionlimit(10000)

def picking(l,r, turn):
    if l>r:return 0

    if dp[l][r]:
        return dp[l][r]
    
    if turn:
        dp[l][r]  = max(picking(l+1,r, 0) + cards[l], picking(l, r-1 , 0) + cards[r])
        return dp[l][r]
    else:
        dp[l][r]  = min(picking(l+1,r, 1) , picking(l, r-1 , 1))
        return dp[l][r]

t = int(input())
for _ in range(t):
    n = int(input())
    cards = list(map(int, input().split()))
    dp = [[0] * n for _ in range(n)]
    picking(0, n-1, 1)
    print(dp[0][n-1])
                       

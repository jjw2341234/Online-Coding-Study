t = int(input())
for _ in range(t):
    n = int(input())
    lista = list(map(int, input().split()))
    listb = list(map(int, input().split()))
    dp = [[0] * n for _ in range(2)]
    dp[0][0]= lista[0]
    dp[1][0]= listb[0]
    
    if n == 1:
        print(max(dp[0][0], dp[1][0]))
        continue
    dp[0][1]= lista[1] + listb[0]
    dp[1][1]= lista[0] + listb[1]

    if n == 2:
        print(max(dp[0][1], dp[1][1]))
        continue
    
    for i in range(2, n):
        dp[0][i] = max(dp[1][i-2], dp[1][i-1]) + lista[i]
        dp[1][i] = max(dp[0][i-2], dp[0][i-1]) + listb[i]
    print(max(dp[0][-1], dp[1][-1]))

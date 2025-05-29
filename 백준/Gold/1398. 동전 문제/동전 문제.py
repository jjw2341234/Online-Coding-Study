n = int(input())
coins = [1, 10, 25] # 해당 구간을 기준으로 100만 곱하면, 구간이 완성됨.
for _ in range(n):
    target = int(input())
    dp = [10 **15 + 1 for _ in range(100)] #100까지가 가능.
    dp[0] = 0
    ans = 0
    for c in coins:
        for i in range(c, 100):dp[i] = min(dp[i], dp[i-c] + 1)
    while target:
        ans += dp[target%100]
        target//=100
    print(ans)
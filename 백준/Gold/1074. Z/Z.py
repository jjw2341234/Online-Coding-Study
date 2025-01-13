n, r, c = map(int, input().split())
ans = 0
#그전의 값들을 빼누는 방식으로 구하면 더 쉽게 구한다.
while n!= 0:
    n-=1
    N = 2**n
    if r < N and c < N: #2사분면
        pass
    elif r < N and c >= N: # 1사분면
        ans+= N**2
        c-= N
    elif r>= N and c < N: #3사분면
        ans+= 2 * N**2
        r -=N
    else: #4사분면
        ans+= 3 * N**2
        r-=N
        c-=N
print(ans)
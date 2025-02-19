def dfs(n, alst, blst):
    global ans

    # 한 팀이 절반을 초과하면 더 탐색할 필요 없음 (백트래킹)
    if len(alst) > N // 2 or len(blst) > N // 2:
        return

    if n == N:
        if len(alst) == len(blst):  # 두 팀의 인원이 같을 때만 점수 계산
            asm = bsm = 0
            for i in range(len(alst)):  
                for j in range(len(alst)):
                    asm += arr[alst[i]][alst[j]]
                    bsm += arr[blst[i]][blst[j]]

            ans = min(ans, abs(asm - bsm))  # 정답 갱신
        return

    dfs(n + 1, alst + [n], blst)  # A팀 선택
    dfs(n + 1, alst, blst + [n])  # B팀 선택

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = int(1e9)
dfs(0, [], [])
print(ans)

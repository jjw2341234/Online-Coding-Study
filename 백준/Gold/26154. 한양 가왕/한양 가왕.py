import sys

input = sys.stdin.readline

def move(n, m, score):
    move_cnt = m if m <= n else n + (m % n)
    
    for _ in range(move_cnt):
        first_move_idx = 1 if score[0][0] > score[0][1] else 0
        move_idx = 2
        
        for j in range(1, n):
            if score[j][0] > score[j][1]:
                score[j - 1][move_idx] = score[j][0]
                move_idx = 0
            else:
                score[j - 1][move_idx] = score[j][1]
                move_idx = 1
        
        score[n - 1][move_idx] = score[0][first_move_idx]
        score[0][first_move_idx] = score[0][2]

# 입력 처리
n, m = map(int, input().split())
score = [list(map(int, input().split())) + [0] for _ in range(n)]

# 연산 수행
move(n, m, score)

# 결과 출력
for a, b, _ in score:
    print(min(a, b), max(a, b))

a, b = map(int, input().split())  # 가로(a), 세로(b)

n, m = map(int, input().split())  # 로봇 개수(n), 명령 개수(m)

rob = []  # 로봇의 위치 및 방향 저장
brd = [[0] * a for _ in range(b)]  # 보드에 로봇 배치

NESW_dic = {'N': 0, 'E': 1, 'S': 2, 'W': 3}
NESW_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # N, E, S, W 방향 이동값

flag = False  # 충돌 여부 체크

# 로봇 초기 배치
for i in range(n):
    y, x, dir = input().split()
    r = b - int(x)  # 입력 좌표 변환
    c = int(y) - 1
    rob.append([r, c, NESW_dic[dir]])  # 로봇 정보 저장
    brd[r][c] = i + 1  # 보드에 로봇 번호 저장

# 명령 실행
for _ in range(m):
    ind, com, rep = input().split()
    ind = int(ind)
    rep = int(rep)

    r, c, d = rob[ind - 1]  # 해당 로봇의 정보 가져오기

    if com == 'L':  # 왼쪽(반시계) 회전
        d = (d - rep) % 4
    elif com == 'R':  # 오른쪽(시계) 회전
        d = (d + rep) % 4
    else:  # 'F' (전진)
        dr, dc = NESW_list[d]

        for _ in range(rep):
            nr, nc = r + dr, c + dc  # 다음 위치 계산

            # 벽과 충돌 확인
            if not (0 <= nr < b and 0 <= nc < a):
                flag = True
                print(f'Robot {ind} crashes into the wall')
                break

            # 다른 로봇과 충돌 확인
            if brd[nr][nc]:
                flag = True
                print(f'Robot {ind} crashes into robot {brd[nr][nc]}')
                break

            # 이동
            brd[r][c] = 0  # 기존 위치 제거
            r, c = nr, nc  # 새로운 위치 갱신
            brd[r][c] = ind  # 새로운 위치에 로봇 배치

    # 로봇 정보 업데이트
    rob[ind - 1] = [r, c, d]

    # 충돌 발생 시 즉시 종료
    if flag:
        break

if not flag:
    print('OK')

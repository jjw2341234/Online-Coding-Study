from collections import deque

n = int(input())
def flip(nums, arr):
    for num in nums:
        arr[num] = '0' if arr[num] == '1' else '1'
    return arr

def solution(board):
    cases = [(0,1,2), (0,3,6), (1,4,7), (2,5,8), (6,7,8), (3,4,5), (0,4,8), (2,4,6)]
    visit = [0] * 512 # 최대, 최소가 0~ 511임.
    q = deque([(int(''.join(board), 2) , 0)])
    while q:
        arrbin, cnt = q.popleft()
        if arrbin == 0 or arrbin == 511:
            return cnt
        
        for nums in cases:
            newarr = flip(nums, list(bin(arrbin)[2:].zfill(9)))
            vs = int(''.join(newarr), 2)
            if not visit[vs]:
                visit[vs] = 1
                q.append((int(''.join(newarr), 2), cnt+1))
    
    return -1
for _ in range(n):
    board = [list(map(str, input().split())) for i in range(3)]
    board = ['1' if board[i][j] == 'H' else '0' for i in range(3) for j in range(3)]
    print(solution(board))
def solution(n):
    answer = 0
    r1 = bin(n)[2:]
    cnt = r1.count("1")
    print(cnt)
    for i in range(n+1, 1000001):
        r2 = bin(i)[2:]
        if r2.count("1") == cnt:
            answer = i
            break
    return answer
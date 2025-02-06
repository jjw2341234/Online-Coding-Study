def solution(n):
    answer = 1
    res = []
    if n <=2:
        return answer
    else:
        for i in range(1, n//2+2):
            res.append(i)
            while sum(res) > n:
                res.pop(0)
            if sum(res) == n:
                answer+=1
    return answer
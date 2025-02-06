def solution(s):
    answer = -1
    tmp = []
    for i in s:
        if len(tmp) == 0:
            tmp.append(i)
        elif tmp[-1] == i:
            tmp.pop()
        else:
            tmp.append(i)
    t = ''.join(tmp)
    if t == "":
        answer = 1
    else:
        answer = 0
    return answer
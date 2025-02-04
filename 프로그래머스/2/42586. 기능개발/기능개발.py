def solution(progresses, speeds):
    answer = [1]
    res = 0
    cnt = 1
    temp = []
    for i in range(len(progresses)):
        if (100 - progresses[i]) % speeds[i]:
            tmp = ((100 - progresses[i])//speeds[i] + 1)
        else:
            tmp = (100 - progresses[i]) // speeds[i]
        res = max(res, tmp)
        temp.append(res)
    ind = temp[0]
    for i in range(1, len(temp)):
        if temp[i] == ind:
            answer[-1]+=1
        else:
            answer.append(1)
            ind = temp[i]
    return answer
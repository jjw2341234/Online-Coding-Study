def solution(clothes):
    dic = dict()
    for x,y in clothes:
        if y not in dic:
            dic[y]  = 1
        else:
            dic[y]+=1
    answer = 1
    for d in dic.values():
        answer*=(d+1)
    answer-=1
    return answer
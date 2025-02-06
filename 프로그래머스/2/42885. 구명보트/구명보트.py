def solution(people, limit):
    answer = 0
    people.sort()
    l,e = 0, len(people)-1
    while l<=e:
        if people[l] + people[e] <= limit:
            answer+=1
            l+=1
            e-=1
        else:
            answer+=1
            e-=1
    return answer
def solution(genres, plays):
    answer = []
    lists = [[genres[i], plays[i], i] for i in range(len(genres))]
    lists = sorted(lists, key = lambda x: (x[0], -x[1], x[2]))
    total_gen = {}
    print(lists)
    for l in lists:
        if l[0] not in total_gen:
            total_gen[l[0]] = l[1]
        else:
            total_gen[l[0]] += l[1]
    total_gen = sorted(total_gen.items(), key = lambda x: -x[1])
    for i in total_gen:
        count = 0
        for j in lists:
            if i[0] == j[0]:
                count+=1
                if count > 2:
                    break
                else:
                    answer.append(j[2])
    print(total_gen)
    return answer
def solution(brown, yellow):
    answer = []
    mul = brown+yellow
    x = []
    y = []
    for i in range(1, int(yellow ** 0.5)+1):
        if yellow % i == 0:
            x.append(int(yellow//i))
            y.append(i)
    for i in range(len(x)):
        if (x[i]+2) * (y[i]+2) == mul:
            answer.append(x[i]+2)
            answer.append(y[i]+2)
            
    return answer
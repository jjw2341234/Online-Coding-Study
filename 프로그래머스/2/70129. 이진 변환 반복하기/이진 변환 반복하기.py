def solution(s):
    answer = []
    cnt = 0
    z_cnt = 0
    while True:
        if s == '1':
            break
        z_cnt+=s.count("0")
        s = s.replace("0", "")
        s = bin(len(s))[2:]
        cnt+=1
    return [cnt, z_cnt]
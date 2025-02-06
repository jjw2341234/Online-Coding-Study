def solution(s):
    arr = list(map(str, s.split()))
    answer = ''
    cnt = 0
    for i in range(len(s)):
        if s[i] == ' ':
            answer+= s[i]
            cnt = 0
        elif s[i].isalpha():
            if cnt == 0:
                cnt+=1
                answer+= s[i].upper()
            else:
                answer+= s[i].lower()
        elif s[i].isdigit():
            answer+=s[i]
            cnt+=1
    return answer
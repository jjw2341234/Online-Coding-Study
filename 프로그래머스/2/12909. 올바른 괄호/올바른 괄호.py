def solution(s):
    answer = False
    cnt = 0
    ind = 0
    while ind < len(s):
        
        if cnt < 0:
            break
        
        if s[ind] == '(':
            cnt+=1
        elif s[ind] == ')':
            cnt-=1
        ind+=1
    if cnt:
        return False
    else:
        return True
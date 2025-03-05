#index에 따라서 스택을 순회하는 방식을 골려야 하는 문제
s = list(input())
res = len(s)
for i in range(len(s)):        
    if s[i::] == s[i::][::-1]:
        res+=i
        break
print(res)
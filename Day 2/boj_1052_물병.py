n, m = map(int, input().split())
cnt = 0
while bin(n).count('1') > m:
    n+=1
    cnt+=1
print(cnt)

#이진수 변환을 이용한 방식.

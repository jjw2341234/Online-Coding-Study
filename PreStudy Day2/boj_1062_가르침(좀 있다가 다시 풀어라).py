import sys


n, m = map(int, input().split())
if m< 5:
    print(0)
    exit(0)
elif m >=26:
    print(n)
    exit(0)
bases = [0] * 26
for b in ['a', 'n', 't', 'i', 'c']:
    bases[ord(b) - ord('a')] +=1
words = [set(sys.stdin.readline().rstrip()) for _ in range(n)]

answer = 0
def dfs(idx, cnt):
    global answer 
    if cnt == m-5:
        readcnt = 0
        for word in words:
            check = True
            for w in word:
                if not bases[ord(w) - ord('a')]:
                    check = False
                    break
            if check:
                readcnt+=1
        answer = max(answer, readcnt)
        return 
    
    for i in range(idx, 26):
        if not bases[i]:
            bases[i]+=1
            dfs(i, cnt+1)
            bases[i]-=1
dfs(0,0)
print(answer)  
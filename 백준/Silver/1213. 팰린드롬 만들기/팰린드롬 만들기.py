from collections import Counter
s = list(input().rstrip())
counter = Counter(s)
cnt = 0
res = ""
mid = ""
for key, value in counter.items():
    if value % 2:
        cnt+=1
        mid = key
        if cnt >1:
            print("I'm Sorry Hansoo")
            exit()
for k,v in sorted(counter.items()):
    res += k * (v//2)
print(res + mid + res[::-1])
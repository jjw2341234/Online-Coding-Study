team = int(input())
for _ in range(team):
    n = int(input())
    strings  = [input().strip() for _ in range(n)]
    strings.sort()
    chk = True
    for i in range(n-1):
        if strings[i+1].startswith(strings[i]):
            chk = False
            print("NO")
            break
    if chk:
        print("YES")
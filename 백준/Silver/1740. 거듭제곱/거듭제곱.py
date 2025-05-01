n = bin(int(input()))[2:]
ans = 0
for i in range(len(n)):
    if int(n[i]):ans+= 3**(len(n)-1-i)
print(ans)
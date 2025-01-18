def Find(x):
    if x != parent[x]:
        parent[x] = Find(parent[x])
    return parent[x]

def Union(a,b):
    a = Find(a)
    b = Find(b)

    if a in know and b in know:
        return
    if a in know:
        parent[b] = a
    elif b in know:
        parent[a] = b
    else:
        if a < b:
            parent[b] = a
        else:
            parent[a] = b


n,m =map(int, input().split())
parent = list(range(n+1))
know = list(map(int, input().split()))[1:]
parties = []
for _ in range(m):
    party_info = list(map(int, input().split()))
    party_len  = party_info[0]
    party_ele = party_info[1:]

    for i in range(party_len-1):
        Union(party_ele[i], party_ele[i+1])
    parties.append(party_ele)

ans = 0
for party in parties:
    for i in range(len(party)):
        if Find(party[i]) in know:
            
            break
    else:
        ans+=1
print(ans)
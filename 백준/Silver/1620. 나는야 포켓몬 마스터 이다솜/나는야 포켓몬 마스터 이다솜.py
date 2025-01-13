n,m = map(int, input().split())
pokedex = dict()
pokedex2= dict()
for _ in range(1, n+1):
    pokemon = input()
    pokedex[pokemon] = _
    pokedex2[_] = pokemon
for _ in range(m):
    q = input()
    if q.isdigit():
        print(pokedex2[int(q)])
    else:
        print(pokedex[q])
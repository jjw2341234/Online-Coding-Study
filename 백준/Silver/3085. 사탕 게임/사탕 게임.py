n = int(input())
graph = [list(input().rstrip()) for _ in range(n)]
res = 1
def bomb():
    global res
    for i in range(n):
        cnt = 1
        for j in range(n-1):
            if graph[i][j] == graph[i][j+1]:
                cnt+=1
                res = max(res, cnt)
            else:
                cnt = 1
    for i in range(n):
        cnt = 1
        for j in range(n-1):
            if graph[j+1][i] == graph[j][i]:
                cnt+=1
                res = max(res, cnt)
            else:
                cnt = 1
    

for i in range(n):
    for j in range(n-1):
        graph[i][j+1], graph[i][j] = graph[i][j], graph[i][j+1]
        bomb()
        graph[i][j], graph[i][j+1] = graph[i][j+1], graph[i][j]

        graph[j+1][i], graph[j][i] = graph[j][i], graph[j+1][i]
        bomb()
        graph[j][i], graph[j+1][i] = graph[j+1][i], graph[j][i]
print(res)
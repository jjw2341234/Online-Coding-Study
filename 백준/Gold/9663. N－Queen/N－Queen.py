n = int(input())
chess = [0] * n
ans = 0

def check_validity(x):
    for i in range(x):
        if chess[x] == chess[i] or abs(chess[i] - chess[x]) == abs(i-x):
            return False
    return True

def n_queens(x):
    global ans
    if x == n:
        ans+=1
        return 
    else:
        for i in range(n):
            chess[x] = i
            if check_validity(x):
                n_queens(x+1)
n_queens(0)
print(ans)

def factorial(n):
    tmp = 1
    for i in range(1,n+1):
        tmp*= i
    return tmp

n = int(input())
for _ in range(n):
    n,m = map(int, input().split())
    print(factorial(m)//factorial(m-n) //factorial(n))
    

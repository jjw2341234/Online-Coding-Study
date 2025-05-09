def add(dic, arr):
    if not arr:
        return
    if arr[0] not in dic:
        dic[arr[0]] = {}
    add(dic[arr[0]], arr[1:])
def printTree(dic, leng):
    for i in sorted(dic.keys()):
        print("--"*leng+i)
        printTree(dic[i], leng+1)

n = int(input())
a = [list(map(str, input().split())) for _ in range(n)]
dic = {}
for i in a:
    i =  i[1:] #갯수 제외 이런식으로
    add(dic, i)
printTree(dic, 0)
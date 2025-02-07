start = input()
end = input()

def dfs(end):
    if end == start:
        print(1)
        exit()
    if len(end) == 0:
        return 
    if end[0] == 'B':
        dfs(end[1:][::-1])
    if end[-1] == 'A':
        dfs(end[:-1])
dfs(end)
print(0)
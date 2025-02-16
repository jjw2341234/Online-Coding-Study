a = input().strip()
b = input().strip()
index_b = 0
ans  = 0

while index_b < len(b):
    max_value, temp, index_a = 0,0,0
    while index_a  < len(a)  and index_b + temp < len(b):
        if b[index_b+temp] == a[index_a]:
            temp+=1
            max_value = max(max_value, temp)
        else:
            temp = 0
        index_a+=1
    index_b+= max_value
    ans+=1
print(ans)
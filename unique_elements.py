n =int(input())
lst =list(map(int,input().split()))
x=[]
for i in range(len(lst)): 
    if lst[i] not in x: 
        x.append(lst[i])
print(*x)
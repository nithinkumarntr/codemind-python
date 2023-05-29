a,b = map(int,input().split())
lst=[list(map(int,input().split())) for i in range(a)]
e=0
o=0
for i in range(a):
    for j in range(b):
        if lst[i][j]%2==0:
            e+=lst[i][j]
        else:
            o+=lst[i][j]
print(e,o)
n = int(input())
arr= list(map(int,input().split()))
c=[]
x=[]
t=[]
for  i  in arr:
    if i%2 !=0:
        c.append(i)
    else:
        x.append(i)
t.extend(c)
t.extend(x)
print(*t)
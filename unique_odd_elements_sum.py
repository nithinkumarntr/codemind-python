n = int(input())
l=list(map(int,input().split()))
c=[]
for i in l:
    if i%2!=0:
        if i not in c:
            c.append(i)
print(sum(c))
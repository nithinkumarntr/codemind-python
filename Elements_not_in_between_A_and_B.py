n = int(input())
m = list(map(int,input().split()))
a,b = map(int,input().split())
c=[]
for i in m:
    if i<a or i>b:
        c.append(i)
if len(c)==0: 
    print("-1")
else:
    print(*c)
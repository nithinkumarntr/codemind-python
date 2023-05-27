a,b=map(int,input().split())
lst=[list(map(int,input().split())) for i in range(a)]
s =[]
for i in lst:
    s.append(sum(i))
print(sum(s))
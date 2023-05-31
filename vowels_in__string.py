n = input()
a=['a','e','i','o','u','A','E','I','O','U']
l=[]
for i in n:
    if i in a and i not in l:
        l.append(i)
if len(l)==0:
    print('-1')
print(*l,end=" ")
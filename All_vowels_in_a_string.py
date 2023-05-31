n = input()
a=['a','e','i','o','u']
b=['A','E','I','O','U']
l=[]
k=[]
for i in n:
    if i not in l and  i in a:
        l.append(i)
    elif i not in k and i in b:
        k.append(i)
if len(l)==5:
    print("True")
elif len(k)==5:
    print("True")
else:
    print("False")
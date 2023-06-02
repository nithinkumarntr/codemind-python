s = input()
l=[]
a =(list(s.split())[-1::-1])
for i in a:
    l.append(i)
print(" ".join(l))
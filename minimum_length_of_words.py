n = input()
l=n.split()
m=[]
for i in l:
    m.append(len(i))
print(min(m))
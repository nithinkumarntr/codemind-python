n = input()
l = n.split()
for  i in l:
    nw=[]
    a=i[::-1]
    nw.append(a)
    print(*nw,end=' ')
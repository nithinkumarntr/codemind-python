n = int(input())
lst = list(map(int,input().split()))
so = []
se = []
for i in lst:
    if i%2 ==0:
        se.append(i)
    else:
        so.append(i)
p = sum(se)
q = sum(so)
print(abs(p-q))

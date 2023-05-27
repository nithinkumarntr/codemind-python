n =int(input())
lst = list(map(int,input().split()))
c=0
for i in range(len(lst)):
    if lst[i]%2!=0 and i%2==0:
        c=1
        break
if c==1:
    print(False)
else:
    print(True)
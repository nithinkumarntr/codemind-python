n = int(input())
l=list(map(int,input().split()))
s=[]
for i in l:
    if i%2!=0 and i not in s:
        s.append(i)
print(len(s))
            
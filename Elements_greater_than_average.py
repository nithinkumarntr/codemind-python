n = int(input())
arr = list(map(int,input().split()))
a=[]
average=sum(arr)//len(arr)
for i in arr:
    if i>=average:
        a.append(i)
print(len(a))
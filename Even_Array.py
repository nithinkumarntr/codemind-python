n = int(input())
arr = list(map(int,input().split()))
a=[]
b=[]
for i in arr: 
    if i%2==0: 
        a.append(i)
    else: 
        b.append(i)
if len(arr)==len(a): 
    print("True")
else: 
    print("False")
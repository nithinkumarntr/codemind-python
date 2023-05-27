a,b = map(int,input().split())
arr=[list(map(int,input().split()))for i in range(a)]
s=0
for i in range(a-1):
    for j in range(b-1):
        if i!=0 and j!=0 and i!=a and j!=b:
            s+=arr[i][j]
print(s)
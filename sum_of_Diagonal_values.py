a,b = map(int,input().split())
arr=[list(map(int,input().split()))for i in range(a)]
s=0
for i in range(a):
    for j in range(b):
        if i==j or i==b-j-1:
            s+=arr[i][j]
print(s)
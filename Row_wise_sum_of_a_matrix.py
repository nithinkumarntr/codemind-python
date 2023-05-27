a,b = map(int,input().split())
lst=[list(map(int,input().split()))for i in range(a)]
for i in lst:
    print(sum(i),end=" ")
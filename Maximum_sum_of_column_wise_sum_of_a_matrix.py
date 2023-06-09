n,m=map(int,input().split())
mat=[list(map(int,input().split())) for i in range(n)]
maxsum=0
for i in range(m):
    sum=0
    for j in range(n):
        sum+=mat[j][i]
    if sum>maxsum:
        maxsum=sum
print(maxsum)

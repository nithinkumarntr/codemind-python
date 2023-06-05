n = int(input())
l = []
while n!=0:
    k=n%10
    n=n//10
    l.append(k)
print(max(l))
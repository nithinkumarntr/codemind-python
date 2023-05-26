n = int(input())
a = list(map(int,input().split()))
average = sum(a)//len(a)
if average in a:
    print("True")
else:
    print("False")
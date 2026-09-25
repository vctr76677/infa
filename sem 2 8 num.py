n=int(input())
a=input().split()
for x in a:
    if sum(1 for i in a if i<x )==n//2:
        print(x)
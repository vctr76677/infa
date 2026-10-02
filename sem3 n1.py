n=int(input())
res=0
s1=0
s2=1
for i in range(2,n+1):
    s1, s2=s2, s1+s2
print(s2)

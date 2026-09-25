a=int(input())
b=int(input())
c=int(input())
n=int(str(a),b)
res=''
while n>0:
    s=str(n%c)
    res=s+res
    n=n//c
print(res)


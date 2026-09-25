with open('inputx.txt', 'r') as f:
    l = f.readlines()
    sys=int(l[2].strip())
    m=list(l[0].split())

    a=int(m[0],sys)
    b=int(m[1],sys)
    c=int(m[2],sys)
    d=l[1]
    n=a+b+c
    res=""
    while n>0:
        s=str(n%c)
        res=s+res
        n=n//c
print(res)

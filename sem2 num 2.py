a=int(input())
s=input().strip()
l=len(s)//a
result=''
for i in range(0,len(s),l):
    group=s[i:i+l]
    result+=group[::-1]
print(result)
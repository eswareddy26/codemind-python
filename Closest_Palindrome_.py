def cp(n):
    t=n
    s=0
    while t>0:
        r=t%10
        s=s*10+r
        t//=10
    if s==n:
        l.append(s)
def cp1(n):
    t1=n
    s1=0
    while t1>0:
        c=t1%10
        s1=s1*10+c
        t1//=10
    if s1==n:
        l1.append(s1)
l=[]
l1=[]
n=int(input())
for i in range(1,n,1):
    cp(i)
for j in range(n+1,n**2,1):
    cp1(j)
a=n-max(l)
b=min(l1)-n
if a<b:
    print(max(l))
elif a>b:
    print(min(l1))
else:
    print(max(l),min(l1))
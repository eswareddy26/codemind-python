def p(n):
    s=True
    for i in range(2,n):
        if n%i==0:
            s=False
            break
    return s
n=int(input())
b=p(n)
while n>0:
    r=n%10
    if r==1:
        a=False
    else:
        a=p(r)
    if a==False:
        break
    else:
        n//=10
if b==True and a==True:
    print("Mega Prime")
else:
    print("Not Mega Prime")
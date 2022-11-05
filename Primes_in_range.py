def pin(n):
    s=True
    if n==1:
        s=False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            s=False
            break
    return s
m=int(input())
n=int(input())
c=0
for i in range(m,n+1):
    if pin(i)==True:
        c+=1
print(c)
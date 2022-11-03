def nfc(n):
    a=0
    b=1
    while True:
        if n<=a or n<=b:
            break
        a=a+b
        b=a+b
    if n==a or n==b:
        l.append(n)
def nfc1(n):
    a=0
    b=1
    while True:
        if n<=a or n<=b:
            break
        a=a+b
        b=a+b
    if n==a or n==b:
        l1.append(n)
n=int(input())
l=[]
l1=[]
for i in range(1,n+1):
    nfc(i)
for j in range(n,n*2,1):
    nfc1(j)
a=n-max(l)
b=min(l1)-n
if a<b:
    print(max(l))
elif a>b:
    print(min(l1))
else:
    print(max(l),min(l1))
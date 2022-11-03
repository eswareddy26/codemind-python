n=int(input())
c=0
s=n*n
while s>0:
    r=s%10
    c+=r
    s//=10
if c==n:
    print("Neon Number")
else:
    print("Not Neon Number")
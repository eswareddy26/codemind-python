n=int(input())
c1=0
c=0
for i in range(1,n+1,1):
    if n%i==0:
        for j in range(1,i+1,1):
            if i%j==0:
                c+=1
        if c>2:
            c1+=1
            c=0
        else:
            c=0
print(c1+1)
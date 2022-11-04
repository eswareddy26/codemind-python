n1=int(input())
n2=int(input())
s=0
for i in range(n1,n2+1):
    for j in range(1,i+1):
        if i%j==0:
            s+=1
    if s==2:
        print(i)
        s=0
    else:
        s=0
n=int(input())
c=0
c1=0
for i in str(n):
    if int(i)%2==0:
        c+=1
    else:
        c1+=1
if c1==0:
    print('Even')
elif c==0:
    print('Odd')
else:
    print('Mixed')
n=int(input())
s=0
l=[]
while n>0:
    r=n%10
    l.append(r)
    n//=10
l.reverse()
for i in range(len(l)):
    if l[i]==6:
        l[i]=9
        break
for j in l:
    s=s*10+j
print(s)
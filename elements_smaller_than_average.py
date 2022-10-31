n=int(input())
l=list(map(int,input().split()))
s=0
c=0
t=0
for i in l:
    s+=i
c=s//n
for i in l:
    if i<=c:
        t+=1
print(t)
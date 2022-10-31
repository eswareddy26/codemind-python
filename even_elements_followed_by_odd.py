n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in l:
    if i%2==0:
        l1.append(i)
for i in l:
    if i%2!=0:
        l1.append(i)
print(*l1)
n=int(input())
l=list(map(int,input().split()))
s=True
for i in l:
    if i%2!=0:
        x=l.index(i)
        if x%2==0:
            s=False
            break
print(s)
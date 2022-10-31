n=int(input())
l=list(map(int,input().split()))
s=True
for i in l:
    if i>1:
        s=False
print(s)
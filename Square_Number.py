n=int(input())
s=True
for i in range(1,n):
    if i*i==n:
        s=False
        break
if s==False:
    print('True')
else:
    print('False')
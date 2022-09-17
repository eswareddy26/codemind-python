n = int(input())
s=1
t=0
for i in str(n):
    s*=int(i)
    t+=int(i)
if t==s:
    print('Spy Number')
else:
    print('Not Spy Number')
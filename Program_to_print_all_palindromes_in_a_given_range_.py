def palindrome(n):
    a=n
    s=0
    while a>0:
        r=a%10
        s=s*10+r
        a//=10
    if s==n:
        l.append(s)
l=[]
n=int(input())
m=int(input())
for i in range(n,m):
    palindrome(i)
print(*l)
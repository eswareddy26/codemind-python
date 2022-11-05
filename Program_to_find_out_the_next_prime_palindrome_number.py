def prime(n):
    s=True
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            s=False
            break
    return s
def palindrome(n):
    s=0
    while n>0:
        r=n%10
        s=s*10+r
        n//=10
    return s
n=int(input())
n+=1
while True:
    if prime(n)==True and palindrome(n)==n:
        print(n)
        break
    else:
        n+=1
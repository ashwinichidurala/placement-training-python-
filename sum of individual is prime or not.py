#check sum of the digits is prime or not if not add one number and print next prime number

"""num=int(input())

s=0

while(num>0):
    rem=num%10
    s+=rem
    num=num//10
#print(s)
    

count=0
for i in range(2,(s//2)+1):
    if(s%i==0):
        count=count+1
        break
if(count==0):
    print(num)
    
else:
    num=num+1"""

def add(n):
    s=0
    while(n):
        s=s+(n%10)
        n=n//10
    return s
def pnp(x):
    if(n in [2,3,5,7]):
        return m
    else:
        return m+1
n=int(input())
m=n
if(n<10):
    print(pnp(n))
else:
    while(1):
        n=add(n)
        if(n<10):
            break
    print(pnp(n))
    
    
    

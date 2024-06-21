#second greatest factor of a number
n=int(input())
x=[]
for i in range(1,n):
    if n%i==0:
        x.append(i)
for i in x:
    print(n[-2])
    

#using recursion  add all even nums in alist and all odd numbers in blist
def fun(a,b):
    c1=0
    c2=0
    for i in a:
        if i%2==0:
            c1+=i
            return c1
    for i in b:
        if i%2!=0:
            c2+=1
            return c2
a=[5,9,1,2]
b=[3,1,8,3]

print(fun(a,b))
            

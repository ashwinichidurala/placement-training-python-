#if input is 10 find sum of all even numbers from one to 10
#recursion 
def sum(x):
    su=0
    if x==0:
        return 0
    return x+sum(x-2)
print(sum(10))

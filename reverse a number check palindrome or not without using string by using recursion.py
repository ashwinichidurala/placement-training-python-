#reverse the given number using recursion and check whether it is palindrome or not
num=int(input())
reversed_num = 0

while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10
def ispalindrome(reversed_num):
    if len(reversed_num) < 2: return True
    if reversed_num[0] != reversed_num[-1]: return False
    return ispalindrome(reversed_num[1:-1])
def fun(x,re):
    if(x==0):
        return re
    re=re*10+(x%10)
    return fun(x//10,re)
n=int(input())
if(n==fun(n,0)):
    

    



#check prime or not if not print next prime number
num=int(input())

while(1):
    count=0
    for i in range(2,(num//2)+1):
        if(num%i==0):
            count=count+1
            break
    if(count==0):
        print(num)
        break
    else:
        num=num+1

        

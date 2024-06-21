#return the element from the list whose frequency is more than half length of the list
n=[4,8,2,4,4,8,4]
p1=n[0]
p2=n[-1]

c=0
for i in range (len(n)):
    count=count(n[i])
    if (count>=len(n//2)):
        print(i)
    else:
        print(1)
    

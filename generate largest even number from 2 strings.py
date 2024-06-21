#take 2 input strings with numbers and letters take unique numbers from both inputs and form largest even number tu5g2k1h8
#g5g8gd6h3
"""s1=input()
s2=input()
z=[]
x=set(s1+s2)
for i in  x:
    if i.isdigit():
        i=int(i)
        z.append(i)
       
        z.sort(reverse=True)
for i in z:
    print(i)"""
a=input()
b=input()
c=set()
for i in a:
    if(i.isdigit()):
        c.add(i)
for i in b:
    if(i.isdigit()):
        c.add(i)
d=list(sorted(c,reverse=True))
if(int(d[-1])%2==0):
   print(''.join(d))
else:
    for i in range(len(d)-2,-1,-1):
        if(int(d[i])%2==0):
           d.append(d.pop(i))
           print(''.join(d))
           break
        else:
            print(i)

    
    
        
        
    
        
        

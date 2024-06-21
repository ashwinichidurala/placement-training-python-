#given a number take that bumber of inputs and a string check wether string contains other string combinations or not if not there print no and also repeated no else print yes

#ip:
"""3
xyz
pqr
abc
#"ÿraxpazr"
op:yes"""

n=int(input())
m=[]
for i in range(n):
    m.append(input())
s=input()
for i in range(len(s)):
    if (s[i] in m[i%n]):
        print("no")
        f=1
        break
    else:
        m[i].remove(s[i])
if(f==0):
    print("yes")
    
    


#longest sequence in a string
a=input()
c=1
m=0
for i in range(len(a)-1):
    if(ord(a[i])==ord(a[i+1])-1):
        c=c+1
    else:
        if(c>m):
            m=c
        c=1
if(c>m):
    m=c
print(m)

    
        
    
    


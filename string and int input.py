#ip:"hello:5438,car:214,book:8799,apple:2187"
#op:oaxp

"""b=input().split(",")
s=[]
for i in range(len(b)):
    s.append(b[i].split(":"))


for i in range(len(s)):
    
    k= str(len(s[i][0]))
    
    if k in s[i][1]:
        print(s[i][0][int(k)-1],end='')
        continue
        
    j=str(int(k)-1)
    ch=int(j)
    
    while(ch):
        if str(ch) in s[i][1]:
            print(s[i][0][int(ch)-1],end='')
            break
        ch-=1
        
    if ch==0:
        print('x',end='')"""
a=input().split(',')
s=''
for i in a:
    b=i.split(":")
    l=len(b[0])
    if(str(l) in b[1]):
        s=s+b[0][-1]
    else:
        for i in range(l-1,0,-1):
            if(str(i) in b[1]):
               s=s+b[0][i-1]
               break
        else:
               s=s+'x'
print(s)
        
    

    
    
    
        
        

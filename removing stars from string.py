#star removal in string
s="leet**co*de"
b=[]
for i in s:
    if (i !='*'):
        b.append(i)
    else:
        b.pop()
print(''.join(b))
        

        
       
    

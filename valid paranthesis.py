#valid paranthesis
a =input()
if len(a)%2==1:
        print('not balanced')
else:        
    b=[]
    k=1
1    if a[0]==')' or a[0]=='}' or a[0]==']':
        print('no')
    for i in a:
        if i=='(' or i =='[' or i=='{':
            b.append(i)
        elif i==')' or i==']' or i=='}' and len(b)!=0:
            if i==')'and b[-1]=='('and len(b)!=0:
                b.pop()
            elif i==']' and b[-1] =='['and len(b)!=0:
                b.pop()
            elif i=='}' and b[-1]=='{' and len(b)!=0:
                b.pop()
            else:
                k=2
    if k==2:
        print('not balanced')
    elif len(b)!=0:
        print('not balanced')
    else:
        print('-1')
            

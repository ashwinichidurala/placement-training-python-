#count of vowels lowercase uppercase vowels
a="f46feLK9y56u#@&56hIjbn6KhA"
uv,uc,lv,lc,d,s=0,0,0,0,0,0
for i in a:
    if(i.islower()):
        if(i in 'AEIOU'):
            uv=uv+1
        else:
            uc=uc+1
    elif(i.isupper()):
        if(i in 'aeiou'):
            lv=lv+1
        else:
            lc=lc+1
    elif(i.isdigit()):
        d=d+1
    elif(i.is alnum()):
        s=s+1

        
    
    


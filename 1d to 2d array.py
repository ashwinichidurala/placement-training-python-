# 1d to 2d list
#ip:[1,2,3,4,1,2,3,1,2]
#op"[[1 2 3 4],[1 2 3],[1 2]]
"""n=list(map(int,input().split()))
k=[]
l=[]
for i in n:
    if i not in k:
        k.append(i)
        l.append(k)
          
    if i in k:
        l.append(i)
print(l)"""

#--------------------1 st method------------------------------------------------------
"""a=list(map(int,input().split()))
m=[]
c=0
while(c!=len(a)):
    r=[]
    for i in range(len(a)):
        if(not str(a[i]).isalpha()):
            if(a[i] not in r):
                c=c+1
                r.append(a[i])
                a[i]='a'

    m.append(r)
print(m)"""
#---------------------------using dictionary 2nd method-------------------------------------------
a=[2,3,4,1,3,2,4,2,1,3]
d={}
m=[]
c=0
for i in a:
    if(i not in d):
        d[i]=1
    else:
        d[i]=d[i]+1
while(c!=len(a)):
    r=[]
    for i in d:
        if(d[i]!=0):
            d[i]=d[i]-1
            c=c+1
            r.append(i)
    m.append(r)
print(m)



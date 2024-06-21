#tcs codevita rotation of string
#ip:school
#3
#L2 --->hoolsc
#R3 ---->oolsch
#L1 ----->chools
#hoc op: yes
"""def combination(l,k):
    def fun(curr,start):
        if len(curr)==k:
            print(curr)
            return
        for i in range(start,len(l)):
            b=fun(curr+[l[i]],i+1)
        
        
        return
    fun([],0)
a="school"
k=3
an="hoc"
combination(a,k)"""
"""def generate_triplets(s, start, triplet, result):
    if len(triplet) == 3:
        result.append(triplet)
        return

    for i in range(start, len(s)):
        generate_triplets(s, i + 1, triplet + s[i], result)

def find_triplets(s, patterns):
    result = []
    generate_triplets(s, 0, "", result)
    for triplet in result:
        if triplet in patterns:
            print("yes")
            return
    print("no")

input_string = "school"
patterns = ["hoc", "cho", "hoo", "ool"]  
find_triplets(input_string,patterns)"""
#solution
a=input()
n=int(input())
str=[]
for i in range(n):
    b=input()
    if(b[0]=='L'):
        str.append(a[int(b[2])])
    else:
        str.append(a[-int(b[2])])
str.sort()
b=[]
for i in range(len(a)-n+1):
    t=sorted(list(a[i:n+i]))
    b.append(t)
print(b)
print(str)
for i in b:
    if(i==str):
        print("yes")
        break
else:
    print("no")


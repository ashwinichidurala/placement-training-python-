#print all possible 3 pairs in a list
"""def print_triplets(lst):
    n = len(lst)
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                print((lst[i], lst[j], lst[k]))


my_list = list(map(int,input().split()))
print_triplets(my_list)"""

#using recursion
def combination(l,k):
    def fun(curr,start):
        if len(curr)==k:
            print(curr)
            return
        for i in range(start,len(l)):
            fun(curr+[l[i]],i+1)
        return
    fun([],0)
a=[3,5,1,6]
k=3
combination(a,k)
    
    
    
    

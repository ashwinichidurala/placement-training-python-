#sort 3 3 numbers in ascending order in a list
"""nums =list(map(int,input().split()))
for i in range(3):
        for j in range(i+1, 3):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
print(nums)"""
#input:4 9 8 2 14 3 5 6

#output:[4, 2, 8, 3, 5, 6, 9, 14]
a=list(map(int,input().split()))
for i in range(len(a)-2):
    if(a[i]>a[i+1]):
        a[i],a[i+1]=a[i+1],a[i]
    if(a[i+1]>a[i+2]):
        a[i+1],a[i+2]=a[i+2],a[i+1]
    if(a[i]>a[i+1]):
        a[i],a[i+1]=a[i+1],a[i]
print (a)
    
    
    
    
    

""""def max_sum(arr, i):
    if i <= 0:
        return arr[0]
    elif i == 1:
        return max(arr[0], arr[1])
    else:
        incl = arr[i] + max_sum(arr, i - 2)
        excl = max_sum(arr, i - 1)
        return max(incl, excl)

def max_sum_no_consecutive(arr):
    return max_sum(arr, len(arr) - 1)


arr = list(map(int, input().split()))
print( max_sum_no_consecutive(arr))"""

def fun(l):
    if(len(l)==0):
        return 0
    if(len(l)==1):
        return 1[0]
    if(len(l)==2):
        return max(1)
    
    le=l[0]+fun(1[2:])
    ri=l[1]+fun(1[3:])
    return max(le,ri)
print(fun([13,9,4,10,5,7]))

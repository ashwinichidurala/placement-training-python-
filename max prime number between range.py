#largest prime number between a range
#input 4 8 14 22 36 68
#output 7 13 19 31 67 
nums =list(map(int,input().split()))

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

for i in range(len(nums) - 1):
    max_prime = 0
    for j in range(nums[i], nums[i + 1]):
        if is_prime(j):
            max_prime = j
    print(max_prime, end=' ')

#using sliding window

        
        
    
    
    

#creating valid password
"""n=input()
l=0
miss1,miss2,miss3=0,0,0
for i in n:
    if len(n)>=8 or i in range(65,90) or i in range(97,112) or i in "@!$%&*":
        break
        print(-1)
    elif len(n)<8:
        l=8-len(n)
        print(int(l))
    elif i not in range(65,90):
            miss1=1
    elif i not in range(97,112):
            miss2=1
    elif i not in "@#!$%*":
            miss3=1

tm=miss1+miss2+miss3
print(tm)"""
            
#***********************************************************************************************************************************
#2nd method without ascii
n = input()
length = len(n)

# Initialize missing character types
missing_upper = 1
missing_lower = 1
missing_digit = 1
missing_special = 1

# Check for each character type in the password
for char in n:
    if char.isupper():
        missing_upper = 0
    elif char.islower():
        missing_lower = 0
    elif char.isdigit():
        missing_digit = 0
    elif char in "@#!$%*":
        missing_special = 0

# Total missing character types
total_missing = missing_upper + missing_lower + missing_digit + missing_special

# Check the length of the password
if length < 8:
    print(8 - length)
else:
    print(total_missing)
#*********************************************************************************************************************************************

#METHOD 3


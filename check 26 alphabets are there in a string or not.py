# check wether 26 alphabets are there or not in a string
"""n=input()
n=set()
if len(k)==27:
    print("yes")
else:
    print("no")"""

#uppercase lowercase numbers
n=input()
for i in range(97,123):
    if (chr(i) not in n):
        print("no")
        break
else:
    print("no")

#longest length of substring without non repeating characters
#ip:"abfgresagtyuiofde"
#op:12
"""s = input()  
subs = []
lens = []  
curr_sub = []

for c in s:
    if c in curr_sub:
        
        subs.append(''.join(curr_sub))
        lens.append(len(curr_sub))
        
        idx = curr_sub.index(c)
        curr_sub = curr_sub[idx + 1:]
    
    curr_sub.append(c)


if curr_sub:
    subs.append(''.join(curr_sub))
    lens.append(len(curr_sub))


max_length = max(lens) if lens else 0


print(max_length)"""





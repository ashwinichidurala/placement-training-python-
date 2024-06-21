#height of buildings


heights = list(map(int, input().split()))

max_h = 0
count_m = 0


for h in heights:
    if h > max_h:
        count_m += 1
        max_h = h


max_h = 0
count_e = 0


heights.reverse()
for h in heights:
    if h > max_h:
        count_e += 1
        max_h = h


print("Count in the morning:", count_m)
print("Count in the evening:", count_e)



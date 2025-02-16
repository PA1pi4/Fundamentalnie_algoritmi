arr = [9, 7, 3, 2, 5, 254, 6,7]
min = arr[0]  # 9
min_old = min  # 9

for x in arr:  # 7
    if x < min < min_old:  # 7| < 9 < 9
        min_old = min # 14
        min = x # 6
    elif min < x < min_old: # 9 < 7| < 9
        min = min
        min_old = x
    elif min < min_old < x: # 9 < 9 < |7
        min = min #
        min_old = min_old #
    else:
        min_old = x # 9

print(min_old)
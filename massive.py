arr = [1, 2, 3, 4, 5, 6, 7] # Оригинальный массив

min = arr[0]
min_old = min

for x in arr:
    if x < min <= min_old:
        min_old = min
        min = x
    elif min < x < min_old:
        min = min
        min_old = x
    elif min < min_old < x:
        min = min
        min_old = min_old
    else:
        min_old = x

print(min_old)
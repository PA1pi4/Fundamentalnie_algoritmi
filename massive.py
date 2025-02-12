arr = [1, 2, 3, 4, 5, 6, 7]
min = arr[0]
min_old = min
for x in arr:
    if min > x:
        min_old = min
        min = x
print(min_old)

import random
n = random.randint(10, 15)
arr = []
for i in range(1, n):
    arr.append(random.randint(0, 200)) # Добавил рандомный генератор массива для проверки

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

print(arr)
print(min_old)
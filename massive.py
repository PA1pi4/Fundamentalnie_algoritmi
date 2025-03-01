import random

n = random.randint(5, 15)  # генерация знаяения длины массива
arr = []  # инициализация пустого массива
for i in range(1, n):
    arr.append(random.randint(0, 200))  # Добавление рандомного генератора массива
# Преобразует список arr во множество, где все дубликаты автоматически удаляются
unique = len(set(arr))  # Возвращает количество элементов, равное количеству уникальных значений в исходном списке.
min = arr[0]  # инициализация минимума
min_old = min  # инициализация второго минимума

for x in arr:
    if x < min <= min_old:
        min_old = min
        min = x
    elif x <= min < min_old:
        min = x
    elif min < x <= min_old:
        min_old = x
    elif min < min_old < x:
        min = min
        min_old = min_old
    else:
        min_old = x
if unique < 3:
    print("Ошибка: массив должен содержать более двух отличных друг от друга значений.")
else:
    print(arr)
    print(min_old)
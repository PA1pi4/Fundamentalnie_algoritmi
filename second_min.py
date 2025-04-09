import random
import timeit
import time


def second_min(n, arr):

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


# Пример использования
n = 15  # генерация значения длины массива
arr = []  # инициализация пустого массива

time_start = timeit.default_timer()
print("The start time for second_min is :", time_start)
time.sleep(1)

second_min(n, arr)

print("The difference of time for second_min is :", timeit.default_timer() - time_start - 1)
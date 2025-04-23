import timeit  # подключение библиотек
import random
import time

leng = 14  # определение длины массива
arr = []  # инициализация пустого массива
for i in range(0, leng):
    arr.append(random.randint(100, 800))  # заполнение массива случайными числам
    arr.sort()  # сортировка массива
target = random.choice(arr)  # выбор значения из массива, которое необходимо будет найти
print(target)  # вывод искомого значения
print(arr)  # вывод массива


def fun():  # инициализация функции
    it = 0  # инициализация переменной количества итераций до нахождения искомого значения
    left, right = 0, len(arr) - 1  # обозначение границ массива кортежем
    while left <= right:
        mid = left + (right - left) // 2
        it += 1
        if arr[mid] == target:
            return it, mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


time_start = timeit.default_timer()  # запуск таймера
print("The start time for binomial_search is :", time_start)
time.sleep(1)

it, result = fun()  # запуск функции
if result != -1:
    print(f"Target found at index {result}")  # вывод искомого значения
else:
    print("Target not found")  # вывод об отсутствии искомого значения

print("The difference of time for binomial_search is :", timeit.default_timer() - time_start - 1)
print(f"The amount of iterations is {it}")  # вывод понадобившегося числа итераций


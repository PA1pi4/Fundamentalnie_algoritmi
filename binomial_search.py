import timeit
import random


def fun():
    return random.randint(100, 800)


start = timeit.default_timer()
print("The start time is :", start)
fun()
print("The difference of time is:", timeit.default_timer() - start)
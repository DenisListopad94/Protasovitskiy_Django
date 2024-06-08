# 1) Создайте собственную функцию для вычисление факториала числа.
# Создайте словарь CACHE_FACTORIAL. В качестве ключа используйте число а в качестве значения его факториал.
# Покажите работу кэша добавив нагрузку в виде задержки в 3 секунды при вычислении факториала,
# если числа нет в вашем словаре.

from time import sleep
from functools import lru_cache

CACHE_FACTORIAL = {}


def factorial(n: int) -> int:
    """
    Calculates the factorial of n using caching
    :param n: int
    :return: int
    """
    if n < 0:
        raise ValueError("The number can't be negative")
    if n in CACHE_FACTORIAL:
        print(n)
        return CACHE_FACTORIAL[n]
    else:
        print(n)
        sleep(3)
        if n == 0 or n == 1:
            result = 1
        else:
            result = n * factorial(n - 1)
        CACHE_FACTORIAL[n] = result
        return result


print(factorial(5))
print(factorial(5))


# 2)С помощью декоратора @lru_cache закешируйте функцию которая рекурсивно считает сумму положительных чисел списка.

@lru_cache()
def recursive_sum(some_lst: list) -> int:
    """
    Recursively calculates sum of positive numbers in list using caching
    :param some_lst: list
    :return: int
    """
    if not some_lst:
        return 0
    return some_lst[0] + recursive_sum(tuple(some_lst[1:]))


print(recursive_sum((1, 2, 3, 4, 5)))
print(recursive_sum((1, 2, 3, 4, 5, 6)))
print(recursive_sum((1, 2, 3, 4, 5)))

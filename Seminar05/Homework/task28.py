'''
Задача 28:
Напишите рекурсивную функцию sum(a, b), возвращающую сумму
двух целых неотрицательных чисел. Из всех арифметических операций
допускаются только +1 и -1. Также нельзя использовать циклы.
Input: 2 2
Output: 4
'''


def recursive_sum(a: int, b: int) -> int:
    if b == 0:
        return a
    return recursive_sum(a + 1, b - 1)


print(recursive_sum(2, 2))
print(recursive_sum(5, 10))
print(recursive_sum(10, 5))
print(recursive_sum(0, 0))

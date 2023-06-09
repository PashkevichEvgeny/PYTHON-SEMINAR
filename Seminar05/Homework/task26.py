'''
Задача 26:
Напишите программу, которая на вход принимает два числа A и B,
и возводит число А в целую степень B с помощью рекурсии.
A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8
'''


def power(a: int, b: int) -> int:
    if b == 0:
        return 1
    if b == 1:
        return a
    return a * power(a, b - 1)


a = int(input('Число A: '))
b = int(input('Число B: '))
print(f'{a} в степени {b} - это {power(a, b)}')
print(f'3⁵ = {power(3, 5)}')
print(f'2³ = {power(2, 3)}')

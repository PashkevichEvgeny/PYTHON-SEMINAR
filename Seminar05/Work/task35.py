'''
Задача №35.
Напишите функцию, которая принимает одно число и проверяет, является
ли оно простым. Напоминание: Простое число - это число, которое
имеет 2 делителя: 1 и n(само число)
Input: 5
Output: yes
'''


# def prime(num):
#     amount = 0
#     for i in range(1, num):
#         if num % i == 0:
#             amount += 1
#     return amount


# print(prime(5))


def prime(number, n=2):
    if n >= number:
        return "yes"
    if number % n == 0:
        return "no"
    return prime(number, n + 1)


print(prime(10))
for i in range(100):
    if prime(i) == 'yes':
        print(i, end=' ')

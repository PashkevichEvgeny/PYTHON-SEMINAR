'''
Задача 11.
Решение в группах
Дано натуральное число A > 1. Определите, каким по
счету числом Фибоначчи оно является, то есть
выведите такое число n, что φ(n)=A. Если А не
является числом Фибоначчи, выведите число -1.
5 -> 6
'''

n = int(input("Число: "))
first, second = 1, 1
position = 3

while n > second:
    position += 1
    first += second
    first, second = second, first

if n == 0:
    print(1)
elif n == 1:
    print(2, 3)
elif second == n:
    print(position)
else:
    print(-1)

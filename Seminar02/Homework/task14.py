'''
Задача 14:
Требуется вывести все целые степени двойки (т.е. числа вида 2k ),
не превосходящие числа N.
10 -> 1 2 4 8
'''

n = int(input("Число: "))
power_of_two = 1
while power_of_two < n:
    print(power_of_two, end=' ')
    power_of_two *= 2

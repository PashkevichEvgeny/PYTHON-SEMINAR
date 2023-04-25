'''
Задача №39.
Даны два массива чисел. Требуется вывести те элементы первого массива
(в том порядке, в каком они идут в первом массиве), которых нет во
втором массиве. Пользователь вводит число N - количество элементов
в первом массиве, затем N чисел - элементы массива. Затем число M - количество
элементов во втором массиве. Затем элементы второго массива
Input:
7
3 1 3 4 2 4 12
6
4 15 43 1 15 1
Output:
3 3 2 12
(каждое число вводится с новой строки)
'''


def not_in_second(first: list, second: list) -> list:
    return [i for i in first if i not in second]


f = list(map(int, input("Значения через пробел: ").split()))
s = list(map(int, input("Значения через пробел: ").split()))
print(not_in_second(f, s))

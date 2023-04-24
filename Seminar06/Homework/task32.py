'''
Задача 32:
Определить индексы элементов массива (списка), значения которых принадлежат
заданному диапазону (т.е. не меньше заданного минимума и не больше заданного
максимума)
Не хватает диапазона, предположительно [7: 10]
Input: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
         0  1  2  3   4   5  6  7   8   9 10 11  12 13  14  15 16  17  18 19
            9                          10            8  10                 7
Output: [1, 9, 13, 14, 19]
'''


def in_diapason(lst: list, start: int, end: int) -> list:
    new_lst = list()
    for i in lst:
        if i in range(start, end + 1):
            new_lst.append(lst.index(i))
    return new_lst


user_list = list(map(int, input(
    "Введите список чисел: ").split(", ")))
print(user_list)
start, end = list(map(int, input(
    "Введите начало и конец диапазона: ").split()))
print(start, end)
print(in_diapason(user_list, start, end))

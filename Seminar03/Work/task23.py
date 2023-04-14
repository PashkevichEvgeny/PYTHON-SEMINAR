'''
Задача 23.
Дан массив, состоящий из целых чисел. Напишите программу,
которая подсчитает количество элементов массива, больших предыдущего
(элемента с предыдущим номером)
Input: [0, -1, 5, 2, 3]
Output: 2 (-1 < 5, 2 < 3)

Примечание:
Пользователь может вводить значения списка или список задан изначально.
'''


def user_list():
    lst = list()
    while True:
        item = input("Для добавление введите число, для выхода букву: ")
        if item.isalpha():
            break
        lst.append(int(item))
    return lst


lst = [0, -1, 5, 2, 3, 5, 6, 1]
bigger_than_previous = 0
for i in range(1, len(lst)):
    if lst[i - 1] < lst[i]:
        bigger_than_previous += 1
print(bigger_than_previous)

print(len([i for i in range(1, len(lst)) if lst[i - 1] < lst[i]]))

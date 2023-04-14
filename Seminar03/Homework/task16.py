'''
Задача 16:
Требуется вычислить, сколько раз встречается некоторое
число X в массиве A[1..N]. Пользователь в первой строке вводит
натуральное число N – количество элементов в массиве. В последующих
строках записаны N целых чисел Ai . Последняя строка содержит число X
Input:
5
1 2 3 4 5
3
Output:
1
'''

# Too long list comprehension
# print([int(input("Введите число: ")) for _ in range(
#        int(input('Длина списка: ')))].count(
#        int(input("Какое число ищем: "))))

# Более классический способ
lst = []
length = int(input("Введите длину списка:"))
for _ in range(length):
    digit = int(input("Введите число: "))
    lst.append(digit)
desired_number = int(input("Введите искомое число: "))
print(lst.count(desired_number))

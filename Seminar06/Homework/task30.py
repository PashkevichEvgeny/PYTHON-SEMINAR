'''
Задача 30:
Заполните массив элементами арифметической прогрессии.
Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
Формула для получения n-го члена прогрессии: aₙ = a₁ + (n-1) * d.
Каждое число вводится с новой строки.
Ввод: 7 2 5
Вывод: 7 9 11 13 15
'''


def progression(first: int, diff: int, amount: int) -> list:
    n = range(first, first + diff * amount, diff)
    return [i for i in n]


first = int(input("Первый элемент: "))
diff = int(input("Разность: "))
amount = int(input("Количество: "))
print(*progression(first, diff, amount))

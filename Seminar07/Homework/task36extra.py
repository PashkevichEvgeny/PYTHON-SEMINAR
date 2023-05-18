'''
Задача 36 дополнительная:
Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру
строки и столбца. Аргументы num_rows и num_columns указывают число строк и
столбцов таблицы, которые должны быть распечатаны. Нумерация строк и столбцов
идет с единицы (подумайте, почему не с нуля). Примечание: бинарной операцией
называется любая операция, у которой ровно два аргумента, как, например, у
операции умножения.
Input:
print_operation_table(lambda x, y: x * y)
Output:
1  2  3  4  5  6
2  4  6  8  10 12
3  6  9  12 15 18
4  8  12 16 20 24
5  10 15 20 25 30
6  12 18 24 30 36
'''


def print_operation_table(operation, num_columns=6, num_rows=6):
    # Создаю диапазоны от 1 до конца + 1
    cols, rows = map(lambda x: range(1, x + 1), (num_columns, num_rows))
    [print(                        # Распечатываю получившиеся строки
        *[''.join(str(             # Соединяю в выровненную строку
            operation(col, row)    # Применение заданной функции
            ).ljust(2))
            for row in rows])      # Перебор значений по горизонтали
        for col in cols            # Перебор значений по вертикали
     ]


print_operation_table(lambda x, y: x * y)
print()
print_operation_table(lambda x, y: x - y)

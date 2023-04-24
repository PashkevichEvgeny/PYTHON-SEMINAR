'''
Задача №45.
Два различных натуральных числа n и m называются дружественными, если сумма
делителей числа n (включая 1, но исключая само n) равна числу m и наоборот.
Например, 220 и 284 – дружественные числа. По данному числу k выведите все
пары дружественных чисел, каждое из которых не превосходит k. Программа
получает на вход одно натуральное число k, не превосходящее 10⁵. Программа
должна вывести все пары дружественных чисел, каждое из которых не
превосходит k. Пары необходимо выводить по одной в строке, разделяя пробелами.
Каждая пара должна быть выведена только один раз (перестановка чисел новую
пару не дает).
Дружественные числа были открыты последователями Пифагора; правда, им удалось
найти только одну пару дружественных чисел — 220 и 284.
Список делителей для 220:
1, 2, 4, 5, 10, 11, 20, 22, 44, 55 и 110, — их сумма равна 284.
Список делителей для 284:
1, 2, 4, 71 и 142, — и сумма равна 220.
Пары дружественных чисел, меньших 100 000.
220 284 (Пифагор, ~500 до н.э.)   17296  18416 (Ибн ал-Банна, ~1300)
1184  1210  (Паганини, 1860)      63020  76084 (Эйлер, 1747)
2620  2924  (Эйлер, 1747)         66928  66992 (Эйлер, 1750)
5020  5564  (Эйлер, 1747)         67095  71145 (Эйлер, 1747)
6232  6368  (Эйлер, 1750)         69615  87633 (Эйлер, 1747)
10744 10856 (Эйлер, 1747)         79750  88730 (Рольф, 1964)
12285 14595 (Браун, 1939)
---------------------------------------
Input: 300   -> Output: 220 284
'''

n = []
for i in range(1, 10000):
    digit = sum([k for k in range(1, i // 2 + 1) if i % k == 0])
    if digit != 1 and digit > i // 2:
        n.append((i, digit))
print(n)
print(*(k for (k, kk) in n if (kk, k) in n and k != kk))
# n2 = [(i, sum([k for k in range(
#     1, i // 2 + 1) if i % k == 0])) for i in range(100, 90000)]
# print(*(k for (k, kk) in n2 if (kk, k) in n2 and k != kk))

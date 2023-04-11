'''Задача 10:
На столе лежат n монеток. Некоторые из них лежат вверх
решкой, а некоторые – гербом. Определите минимальное число
монеток, которые нужно перевернуть, чтобы все монетки были
повернуты вверх одной и той же стороной. Выведите минимальное
количество монет, которые нужно перевернуть.
5 -> 1 0 1 0 1
2
'''

eagle = 0
amount_coin = int(input("Количество монет: "))
for _ in range(amount_coin):
    coin = int(input("Монета: "))
    if coin % 2:
        eagle += 1
if amount_coin - eagle > eagle:
    print(eagle)
else:
    print(f"Перевернуть нужно {amount_coin - eagle}")
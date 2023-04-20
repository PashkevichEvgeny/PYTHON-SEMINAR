'''
Задача №31.
Последовательностью Фибоначчи называется последовательность чисел
a₀, a₁,..., aₙ, где a₀ = 0, a₁ = 1, aₖ = aₖ₋₁ + aₖ₋₂ (k > 1).
Требуется найти N-е число Фибоначчи
Input: 7
Output: 21
Задание необходимо решать через рекурсию
'''


def fib(number):
    if number == 0:
        return 0
    if number in (1, 2):
        return 1
    return fib(number - 1) + fib(number - 2)


print(fib(int(input("Число: "))))

# 1 2 3 4 5 6 7 8 9     Позиция
# 0 1 1 2 3 5 8 13 21   Значение
print(*(i for i in range(1, 9)))
for i in range(8):
    print(fib(i), end=' ')

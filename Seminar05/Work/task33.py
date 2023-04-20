'''
Задача №33.
Хакер Василий получил доступ к классному журналу и хочет заменить все
свои минимальные оценки на максимальные. Напишите программу, которая
заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
Input: 5 -> 2 3 4 3 4 4 2
Output: 1 3 3 3 1
'''

lst = list(map(int, input("list: ").split()))


def downgrade(some_list, max_grade, min_grade):
    if max_grade not in lst:
        return some_list
    ind = lst.index(max_grade)
    lst[ind] = min_grade
    return downgrade(some_list, max_grade, min_grade)


print(downgrade(lst, max(lst), min(lst)))

'''
Задача 21.
Напишите программу для печати всех уникальных значений в словаре.
Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
{"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

Примечание:
Пользователь может вводить значения списка или список задан изначально.
'''


def user_list():
    length = int(input("Длина списка: "))
    return [{input("Введите ключ: "): input("Введите значение: ")}
            for _ in range(length)]


d = [{"V": "S001"}, {"VI": "S001"}, {"V": "S002"}, {"VII": "S005"},
     {"V": "S009"}, {"VI": "S005"}, {"VIII": "S007"}]
new_set = set()
for i in d:
    for k in i.values():
        new_set.add(k)
print(new_set)


print(set((list(i.values())[0]) for i in d))

# print(                                     ) печать
#       set(                      for i in d)  генератор множества
#           (                [0])              извлечение нулевого элемента
#            list(          )                  преобразование словаря в список
#                 i.values()                   извлечение словаря из списка
path = r'Seminar08\book.txt'


def show_data() -> None:
    """Выводит информацию из справочника"""
    with open(path, 'r', encoding='utf-8') as inf:
        for line in inf.readlines()[1:]:
            print(line.replace('| ', 'тел.').rstrip())


def add_data() -> None:
    """Добавляет информацию в справочник."""
    with open(path, 'a', encoding='utf-8') as inf:
        fio = input('Введите ФИО: ').split()
        while len(fio) != 3:
            fio = input('Фамилия Имя Отчество: ').split()
        fio = ' '.join(map(lambda x: x.capitalize(), fio))
        phone = input(f'Телефон {fio}: ')
        inf.write(f'{fio} | {phone}\n')
    print(f'Запись: {fio} тел.{phone} добавлена')


def find_data() -> None:
    """Печатает результат поиска по справочнику."""
    find = search(path, input('Кого ищем? '))
    if find:
        with open(path, 'r', encoding='utf-8') as inf:
            data = inf.readlines()
        [print(data[i].replace('| ', 'тел.').rstrip()) for i in find]
    else:
        print('Не найдено')


def search(book: str, info: str) -> list:
    """Возвращает список с индексами строк, которые подходят под запрос"""
    indexes_found_fio = list()
    with open(book, 'r', encoding='utf-8') as inf:
        for k, line in enumerate(inf.readlines()):
            if f' {info} '.lower() in f' {line} '.lower():
                indexes_found_fio.append(k)
    return indexes_found_fio


def edit_data() -> None:
    """Редактирует найденные записи в списке по запросу"""
    indexes_found_fio = search(path, input('Кого изменить? '))
    if indexes_found_fio:
        if rewrite_data(indexes_found_fio, '1. редактировать эту запись: '):
            add_data()
        else:
            print('Больше подходящих записей нет')
    else:
        print('Не найдено')


def delete_data() -> None:
    """Удаляет найденные по запросу записи из списка"""
    indexes_found_fio = search(path, input('Кого удалить? '))
    if indexes_found_fio:
        if rewrite_data(indexes_found_fio, '1. удалить этого человека'):
            print('Запись удалена')
        else:
            print('Больше подходящих записей нет')
    else:
        print('Не найдено')


def rewrite_data(indexes_found_fio: list, prompt: str) -> bool:
    """Получает индексы строк, которые подходят под запрос и
    подсказку, какое действие можно выполнить. Дает пользователю выбрать,
    какую строку удалить или редактировать, удаляет её и перезаписывает файл.
    Если файл был изменен, возвращает истину"""
    with open(path, 'r+', encoding='utf-8') as inf:
        data = inf.readlines()
        for i in indexes_found_fio:
            print(f"Найдена запись: {data[i].replace('| ', 'тел.').rstrip()}")
            if input(f'0. искать дальше, {prompt} ') == '1':
                del data[i]
                inf.seek(0)
                inf.truncate()
                inf.writelines(data)
                return 1
    return 0

def print_file(line):
    print('id | Имя | Фамилия | Дата рождения | Должность')
    for i in line:
        print(i)


def print_menu():
    return input('''
    1. Показать файл
    2. Добавить запись
    0. Выйти
    : ''')


def input_data():
    data = ''
    data += input('Введите id: ') + ';'
    data += input('Введите Имя: ') + ';'
    data += input('Введите Фамилию: ') + ';'
    data += input('Введите Дату рождения: ') + ';'
    data += input('Введите Должность: ') + ';'
    return data

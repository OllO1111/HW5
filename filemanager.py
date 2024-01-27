import os, shutil, sys
import victory
import use_functions

# Пререквизиты
acc_all = 1000  # Начальный счет
history_acc_purchase = {}  # История покупок
# Главное меню
main_menu = {1: 'создать папку',
             2: 'удалить (файл/папку)',
             3: 'копировать (файл/папку)',
             4: 'просмотр содержимого рабочей директории',
             5: 'посмотреть только папки',
             6: 'посмотреть только файлы',
             7: 'просмотр информации об операционной системе',
             8: 'создатель программы',
             9: 'играть в викторину',
             10: 'мой банковский счет',
             11: 'смена рабочей директории',
             12: 'выход'}


def new_dir(folder):
    """
    Функция  1. создать папку
    :param folder: Имя новой папки
    :return: Результат операции создания новой папки
    """
    if not os.path.isdir(folder):
        os.mkdir(folder)
        return f'Папка {folder} создана'
    else:
        return f'Папка {folder} уже есть'


def del_file_dir(file_dir):
    """
    Функция  2. удалить (файл/папку)
    :param file_dir: имя удаляемой папки или файла
    :return: Результат операции удаления папки или файла
    """
    if os.path.isfile(file_dir):
        os.remove(file_dir)
        return f'Файл {file_dir} удален'
    elif os.path.isdir(file_dir):
        if len(os.listdir(file_dir)) == 0:
            os.rmdir(file_dir)
            return f'Директория {file_dir} удалена'
        else:
            if input(f'Директория {file_dir} не пустая! Действитеьно ее удалить?: ') == 'Да':
                os.removedirs(file_dir)
                return f'Директория {file_dir} удалена со всем содержимым'
    else:
        return f'Файла/Директории {file_dir} не существует'


def copy_file_dir(file_dir_name_old, file_dir_name_new):
    """
    Функция  3. копировать (файл/папку)
    :param file_dir_name_old: имя объекта для копирования
    :param file_dir_name_new: новое имя объекта
    :return: Результат операции копирования файла/папки
    """
    if not os.path.exists(file_dir_name_old):
        return 'Нет такого файла или директории'
    if os.path.exists(file_dir_name_new):
        if input(f'{file_dir_name_new} уже существует. Хотите его заменить на {file_dir_name_old}?: ') != 'Да':
            return 'Вы отменили копирование'
    if file_dir_name_old == file_dir_name_new:
        return 'Новое имя не должно совпадать со старым'
    if os.path.isfile(file_dir_name_old):
        shutil.copy(file_dir_name_old, file_dir_name_new)
        return f'Файл {file_dir_name_old} скопирован в {file_dir_name_new}'
    else:
        shutil.copytree(file_dir_name_old, file_dir_name_new, dirs_exist_ok=True)
        return f'Папка {file_dir_name_old} скопирована в {file_dir_name_new}'


def change_dir(change_dir_name):
    """
    Функция  11. смена рабочей директории
    :param change_dir_name: имя новой директории
    :return: Результат операции
    """
    if os.path.isdir(change_dir_name):
        os.chdir(change_dir_name)
        return f'Текущая директория сменена на: {os.getcwd()}'
    else:
        return f'Директории {change_dir_name} не существует'


if __name__ == '__main__':
    while True:
        print('Текущая директория:', os.getcwd())
        # Прорисовка меню
        for key, value in main_menu.items():
            print(f'{key}. {value}')
        # Проверка корректности ввода
        key_input = 0

        key_input_ = input('Введите номер пункта меню: ')
        # Проверка на число
        if key_input_.isdigit() and int(key_input_) in main_menu:
            key_input = int(key_input_)
            if key_input == 1:
                result = new_dir(input('Введите имя новой папки: '))
                print(result)
            elif key_input == 2:
                result = del_file_dir(input('Введите имя удаляемой папки или файла: '))
                print(result)
            elif key_input == 3:
                result = copy_file_dir(input('Введите имя объекта для копирования: '),
                                       input('Введите новое имя объекта: '))
                print(result)
            elif key_input == 4:
                list(print(i) for i in os.listdir())
            elif key_input == 5:
                result = list(filter(lambda x: os.path.isdir(x), os.listdir()))
                list(print(i) for i in result)
            elif key_input == 6:
                result = list(filter(lambda x: os.path.isfile(x), os.listdir()))
                list(print(i) for i in result)
            elif key_input == 7:
                print(f'My OS is {sys.platform} ({os.name})')
            elif key_input == 8:
                print('Автор программы - Ничук Олег')
            elif key_input == 9:
                victory.quiz()
            elif key_input == 10:
                acc_all, history_acc_purchase = use_functions.bank_acc(acc_all, history_acc_purchase)
            elif key_input == 11:
                result = change_dir(input('Введите имя новой директории: '))
                print(result)
            elif key_input == 12:
                print('До новых встреч')
                break
        else:
            print('Неверный пункт меню')

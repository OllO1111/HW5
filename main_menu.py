
import os, shutil, sys
import victory
import use_functions

# Пререквизиты
acc_all = 1000 # Начальный счет
# Главное меню
main_menu = {1:'создать папку',
            2:'удалить (файл/папку)',
            3:'копировать (файл/папку)',
            4:'просмотр содержимого рабочей директории',
            5:'посмотреть только папки',
            6:'посмотреть только файлы',
            7:'просмотр информации об операционной системе',
            8:'создатель программы',
            9:'играть в викторину',
            10:'мой банковский счет',
            11:'смена рабочей директории',
            12:'выход'}

# Функция  1. создать папку
def new_dir():
    new_dir_name = input('Введите имя новой папки: ')
    if not os.path.isdir(new_dir_name):
        os.mkdir(new_dir_name)
        print(f'Папка {new_dir_name} создана')
    else:
        print(f'Папка {new_dir_name} уже есть')

# Функция  2. удалить (файл/папку)
def del_file_dir():
    del_dir_name = input('Введите имя новой папки: ')
    if os.path.isfile(del_dir_name):
        os.remove(del_dir_name)
        print(f'Файл {del_dir_name} удален')
    elif os.path.isdir(del_dir_name):
        if len(os.listdir(del_dir_name)) == 0:
            os.rmdir(del_dir_name)
            print(f'Директория {del_dir_name} удалена')
        else:
            if input(f'Директория {del_dir_name} не пустая! Действитеьно ее удалить?: ') == 'Да':
                os.removedirs(del_dir_name)
                print(f'Директория {del_dir_name} удалена со всем содержимым')
    else:
        print(f'Файла/Директории {del_dir_name} не существует')

# Функция  3. копировать (файл/папку)
def copy_file_dir():
    copy_dir_name_old = input('Введите имя объекта для копирования: ')
    if not os.path.exists(copy_dir_name_old):
        print('Нет такого файла или директории')
        return
    copy_dir_name_new = input('Введите новое имя: ')
    if os.path.exists(copy_dir_name_new):
        if input(f'{copy_dir_name_new} уже существует. Хотите его заменить новым?: ') != 'Да':
            return
    if copy_dir_name_old == copy_dir_name_new:
        print('Новое имя не должно совпадать со старым')
        return
    if os.path.isfile(copy_dir_name_old):
        shutil.copy(copy_dir_name_old, copy_dir_name_new)
        print(f'Файл {copy_dir_name_old} скопирован в {copy_dir_name_new}')
    else:
        shutil.copytree(copy_dir_name_old, copy_dir_name_new, dirs_exist_ok=True)
        print(f'Папка {copy_dir_name_old} скопирована в {copy_dir_name_new}')

# Функция 4. просмотр содержимого рабочей директории
def list_curr_dir():
    for i in os.listdir():
        print(i)

# Функция 5. посмотреть только папки
def list_curr_dir_dirs():
    for i in os.listdir():
        if os.path.isdir(i):
            print(i)

# Функция 6. посмотреть только файлы
def list_curr_dir_files():
    for i in os.listdir():
        if os.path.isfile(i):
            print(i)


# Функция  11. смена рабочей директории
def change_dir():
    change_dir_name = input('Введите имя новой директории: ')
    if os.path.isdir(change_dir_name):
        os.chdir(change_dir_name)
        print('Текущая деректория:', os.getcwd())
    else:
        print('Такой папкм не существует')

while True:
    print('Текущая деректория:', os.getcwd())
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
            new_dir()
        elif key_input == 2:
            del_file_dir()
        elif key_input == 3:
            copy_file_dir()
        elif key_input == 4:
            list_curr_dir()
        elif key_input == 5:
            list_curr_dir_dirs()
        elif key_input == 6:
            list_curr_dir_files()
        elif key_input == 7:
            print('My OS is', sys.platform, '(', os.name, ')')
        elif key_input == 8:
            print('Автор программы - Ничук Олег')
        elif key_input == 9:
            victory.quiz()
        elif key_input == 10:
            acc_all = use_functions.bank_acc(acc_all)
        elif key_input == 11:
            change_dir()
        elif key_input == 12:
            print('До новых встреч')
            break
    else:
        print('Неверный пункт меню')




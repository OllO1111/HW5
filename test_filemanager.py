import filemanager
import os

import victory, bank_account


def test_filemanager_new_dir():
    """Тест Функция  1. создать папку"""
    folder = 'test_folder'
    if not os.path.isdir(folder):
        assert filemanager.new_dir(folder) == f'Папка {folder} создана'
        os.rmdir(folder)
    else:
        assert filemanager.new_dir(folder) == f'Папка {folder} уже есть'


def test_filemanager_del_file_dir():
    """Тест Функция  2. удалить (файл/папку)"""
    folder = 'test_folder'
    if not os.path.isdir(folder):
        os.mkdir(folder)
        assert filemanager.del_file_dir(folder) == f'Директория {folder} удалена'


def test_filemanager_copy_file_dir():
    """Тест Функция  3. копировать (файл/папку)"""
    folder = 'test_folder'
    folder_new = 'test_folder_new'
    if not os.path.isdir(folder) and not os.path.isdir(folder_new):
        os.mkdir(folder)
        assert filemanager.copy_file_dir(folder, folder_new) == f'Папка {folder} скопирована в {folder_new}'
        os.rmdir(folder)
        os.rmdir(folder_new)


def test_filemanager_change_dir():
    """Тест Функция  11. смена рабочей директории"""
    folder = 'test_folder'
    if not os.path.isdir(folder):
        os.mkdir(folder)
        temp_dir = os.getcwd()
        assert filemanager.change_dir(folder) == f'Текущая директория сменена на: {os.getcwd()}'
        os.chdir(temp_dir)
        os.rmdir(folder)

# Тестируем Чистые функции:

def test_victory_date_str():
    """Тест Преобразуем дату в строку в victory.date_str"""
    assert victory.date_str('07.01.2024') == 'семь январь 2024 год'
    assert victory.date_str('25.06.1956') == 'двадцать пять июнь 1956 год'
    assert victory.date_str('13.12.1022') == 'тринадцать декабрь 1022 год'

def test_bank_account_account_increase():
    """Тест 1. пополнение счета в bank_account.account_increase"""
    assert bank_account.account_increase(2000, 258) == 2258
    assert bank_account.account_increase(4530, 56) == 4586
    assert bank_account.account_increase(25, 2589) == 2614

def test_bank_account_purchase():
    """Тест 2. покупка в bank_account.purchase"""
    assert bank_account.purchase({}, 2000, 258, 'food') == ({'food': 258}, 1742, 'Покупка совершена')
    assert bank_account.purchase({'car': 155568}, 1359, 594, 'food') == ({'car': 155568, 'food': 594}, 765, 'Покупка совершена')
    assert bank_account.purchase({'car': 155568, 'food': 594}, 765, 1565, 'notebook') == ({'car': 155568, 'food': 594}, 765, 'Неверная сумма')

def test_filemanager_dir_save():
    assert filemanager.dir_save('file1,file2', 'dir1,dir2', 'test') == 'files: file1,file2\ndirs: dir1,dir2'

def bank_account_bank_save_load():
    bank_account.bank_save({"acc": 684, "history_purchase": {"food": 10, "dress": 20, "car": 60, "computer": 10, "scooter": 40}},test)
    assert bank_account.bank_load(test) == 684, {"food": 10, "dress": 20, "car": 60, "computer": 10, "scooter": 40}
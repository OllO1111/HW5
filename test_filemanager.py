import filemanager
import os


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
    """Функция  11. смена рабочей директории"""
    folder = 'test_folder'
    if not os.path.isdir(folder):
        os.mkdir(folder)
        temp_dir = os.getcwd()
        assert filemanager.change_dir(folder) == f'Текущая директория сменена на: {os.getcwd()}'
        os.chdir(temp_dir)
        os.rmdir(folder)

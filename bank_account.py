"""
Программа "Личный счет"
"""
import json
import os


def bank_save(bank_str, bank_file):
    """
    сохранение счета и истории операций в файл
    :param bank_str: что сохраняем
    :param bank_file: куда сохраняем
    :return:
    """
    with open(bank_file, 'w') as f:
        json.dump(bank_str, f)


def bank_load(bank_file):
    """
    чтение счета и истории операций из файла
    :param bank_file: файл откуда читаем
    :return: возвращаем счет и историю операций
    """
    with open(bank_file, 'r') as f:
        bank_str = json.load(f)
    return bank_str['acc'], bank_str['history_purchase']


def account_increase(acc_internal, acc_inc):
    """
    1. пополнение счета
    :param acc_internal: Основной счет
    :param acc_inc: Сумма пополнения
    :return: Основной счет
    """
    return acc_internal + acc_inc


def purchase(history, acc_internal, acc_dec, acc_dec_name):
    """
    2. покупка
    :param history: История покупок
    :param acc_internal: Основной счет
    :param acc_dec: Сумма покупки
    :param acc_dec_name: Что покупаем
    :return: История покупок, Основной счет, результат операции
    """
    if acc_internal >= acc_dec:
        acc_internal -= acc_dec
        history[acc_dec_name] = acc_dec
        return history, acc_internal, 'Покупка совершена'
    else:
        return history, acc_internal, 'Неверная сумма'


def bank_acc(dir_main):
    """
    Основная функция ведения счета
    :param dir_main:
    :return: Основной счет, История покупок
    """
    # Пререквизиты
    bank_file = dir_main + '\\bank_account.json'  # Файл ведения счета
    if os.path.isfile(bank_file):
        acc, history_purchase = bank_load(bank_file)  # Начальный счет читаем из файла
    else:
        acc = 0  # Начальный счет
        history_purchase = {}  # История покупок
    while True:
        print(f'Ваш счет {acc} тугриков')
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню ')
        if choice == '1':
            acc = account_increase(acc, int(input('На сколько хотите пополнить счет? ')))
        elif choice == '2':
            history_acc, acc, result = purchase(history_purchase, acc,
                                                int(input('На сколько хотите совершить покупку? ')),
                                                input('что купим? '))
            print(result)
        elif choice == '3':
            print('Ваши покупки:')
            for key, value in history_purchase.items():
                print(key, value)
        elif choice == '4':
            bank_save({'acc': acc, 'history_purchase': history_purchase}, bank_file)
            break
        else:
            print('Неверный пункт меню')
    return


if __name__ == '__main__':
    bank_acc(os.getcwd())

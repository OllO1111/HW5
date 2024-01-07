"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход

1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню

2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню

3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню

4. выход
выход из программы

При выполнении задания можно пользоваться любыми средствами

Для реализации основного меню можно использовать пример ниже или написать свой
"""


def account_increase(acc_internal, acc_inc):
    return acc_internal + acc_inc


def purchase(history, acc_internal, acc_dec, acc_dec_name):
    """
    2. покупка
    :param history: История покупок
    :param acc_internal: Основной счет
    :param acc_dec: Сумма покупки
    :param acc_dec_name: Что покупаем
    :return:
    """
    if acc_internal >= acc_dec:
        acc_internal -= acc_dec
        history[acc_dec_name] = acc_dec
        return history, acc_internal, 'Покупка совершена'
    else:
        return history, acc_internal, 'Неверная сумма'


def print_history(history):
    print('Ваши покупки:')
    for key, value in history.items():
        print(key, value)


def bank_acc(acc, history_acc):
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
            history_acc, acc, result = purchase(history_acc, acc, int(input('На сколько хотите совершить покупку? ')),
                                                input('что купим? '))
            print(result)
        elif choice == '3':
            print_history(history_acc)
        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')
    return acc, history_acc


if __name__ == '__main__':
    bank_acc(2000, {})

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
history = {}

def account_change(reason, summ):
    history[reason] = summ
def account_increase(acc_internal):
    acc_inc = int(input('На сколько хотите пополнить счет? '))
    acc_internal += acc_inc
    #account_change('Пополнение', acc_inc)
    return acc_internal
def purchase(acc_internal):
    acc_dec = int(input('На сколько хотите совершить попкупку? '))
    if acc_internal >= acc_dec:
        acc_dec_name = input('что купим? ')
        acc_internal -= acc_dec
        account_change(acc_dec_name, ~acc_dec)
    else:
        print('Неверная сумма')
    return acc_internal
def print_history():
    print('Ваши покупки:')
    for key, value in history.items():
        print(key, value)

def bank_acc(acc):
    while True:
        print(f'Ваш счет {acc} тугриков')
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню ')
        if choice == '1':
            acc = account_increase(acc)
        elif choice == '2':
            acc = purchase(acc)
        elif choice == '3':
            print_history()
        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')
    return acc

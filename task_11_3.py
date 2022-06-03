'''3. Создать собственный класс-исключение, который должен проверять содержимое списка на
наличие только чисел. Проверить работу исключения на реальном примере. Запрашивать у
пользователя данные и заполнять список необходимо только числами. Класс-исключение
должен контролировать типы данных элементов списка.'''

class NotDigitError(Exception):
    def __init__(self, txt):
        self.txt = txt

my_list = []
while True:
    try:
        val = input("Enter a number ")
        if val == 'stop':
            break
        elif not val.isdigit():
            raise NotDigitError("You enter not a number.")
        else:
            my_list.append(val)
    except NotDigitError as err:
        print(err)

print(*my_list)

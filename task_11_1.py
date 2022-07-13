'''1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый — с
декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип
к типу «Число». Второй — с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на
реальных данных.'''

class Data:
    def __init__(self, data):
        if Data.validation(Data.transform(data)):
            self.data = data
        else:
            self.data = ''

    @classmethod
    def transform(cls, data):
        return list(map(int, data.split('-')))

    @staticmethod
    def validation(data):
        if data[0] <= 0 or data[0] > 31:
            print('Wrong day value')
        elif data[1] <= 0 or data[1] > 12:
            print('Wrong month value')
        elif data[2] < 1900 or data[2] > 2022:
            print('Wrong year value')
        else:
            return True

d = Data('12-12-2021')
print(d.data)
d = Data('33-12-2021')
print(d.data)
d = Data('11-44-2021')
print(d.data)
d = Data('11-10-4444444')
print(d.data)

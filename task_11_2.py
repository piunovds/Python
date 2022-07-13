'''2. Создать собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
Проверить его работу на данных, вводимых пользователем. При вводе нуля в качестве
делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
'''
import random
class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt
try:
    a, b = random.randint(-10, 10), random.randint(-1, 2)
    if b == 0:
        raise MyError("Division by zero is not allowed.")
    print(a / b)
except MyError as err:
    print(err)

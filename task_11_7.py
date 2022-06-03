'''7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта.
Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров.'''
class Complex:
    def __init__(self, *args):
        if len(args) == 2:
            self.re = args[0]
            self.im = args[1]
        elif len(args) == 1:
            self.re = args[0]
            self.im = 0
        else:
            self.re = 0
            self.im = 0
    
    def __str__(self):
        if self.re == 0 and self.im == 0:
            return f'0'
        elif self.re == 0:
            return f'{self.im}i'
        elif self.im == 0:
            return f'{self.re}'
        elif self.im < 0:
            return f'{self.re} - {-self.im}i'
        else:
            return f'{self.re} + {self.im}i'

    def __mul__(self, other):
        return Complex(self.re*other.re - self.im*other.im, self.re*other.im + self.im*other.re)

    def __add__(self, other):
        return Complex(self.re + other.re, self.im + other.im)

f = Complex()
g = Complex(2,-5)
h = Complex(-1,-2)
print(f)
print(h*g)
print(h+g)

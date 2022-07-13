'''
2. Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта — одежда,
которая может иметь определённое название. К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды
существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма(2*H + 0.3).
Проверить работу этих методов на реальных данных. Выполнить общий подсчёт расхода ткани.
Проверить на практике полученные на этом уроке знания. Реализовать абстрактные классы для основных классов проекта и
проверить работу декоратора @property.
'''
from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, value):
        self.size = value
    
    @abstractmethod
    def fabric_need(self):
        pass

class Coat(Clothes):
    @property
    def fabric_need(self):
        print(f'{self.size/6.5 + 0.5:.2f} meters of fabric are needed to sew a coat')
        return self.size/6.5 + 0.5

class Suit(Clothes):
    @property
    def fabric_need(self):
        print(f'{2*self.size + 0.3:.2f} meters of fabric are needed to sew a suit')
        return 2*self.size + 0.3

ct = Coat(66)
st = Suit(2)
print(f'Total cost of fabric = {ct.fabric_need + st.fabric_need:.2f}')

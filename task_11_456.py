'''4. Начать работу над проектом «Склад оргтехники». Создать класс, описывающий склад. А также
класс «Оргтехника», который будет базовым для классов-наследников. Эти классы —
конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить
параметры, общие для приведённых типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.
5. Продолжить работу над предыдущим заданием. Разработать методы, которые отвечают за
приём оргтехники на склад и передачу в определённое подразделение компании. Для
хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
можно использовать любую подходящую структуру (например, словарь).
6. Продолжить работу над предыдущим заданием. Реализовать механизм валидации вводимых
пользователем данных. Например, для указания количества принтеров, отправленных на
склад, нельзя использовать строковый тип данных.'''
from abc import ABC, abstractmethod

class Stock:
    def __init__(self, name, adress):
        self.name = name
        self.adress = adress
        self._dict = {}
    
    def __str__(self):
        return f"Stock: {self.name}, adress: {self.adress}"
    
    @property    
    def get_info(self):
        print(self)
        for key, val in self._dict.items():
            print(f"{key}: {len(val)}")

    def add_to_stock(self, equipment):
        self._dict.setdefault(equipment.group_name, []).append(equipment)
 
    def extract_from_stock(self, group_name, n=1, destination='Stock2'):
        try:
            n = int(n)
        except ValueError:
            print("You enter not a number")
            n = 0
        for _ in range(n):
            if self._dict[group_name]:
                self._dict.setdefault(group_name).pop()
        if len(self._dict.setdefault(group_name)) == 0:
            self._dict.pop(group_name)

class OfficeEquipment(ABC):
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.group = self.__class__.__name__
    @abstractmethod
    def __str__(self):
        pass
    @property
    def group_name(self):
        return f'{self.group}'

class Printer(OfficeEquipment):
    def __init__(self, brand, model, year, p_type='laser'):
        super().__init__(brand, model, year)
        self.p_type = p_type
 
    def __str__(self):
        return f'Printer {self.brand} {self.model} {self.p_type} {self.year}year '

class Scaner(OfficeEquipment):
    def __init__(self, brand, model, year, p_type='tablet'):
        super().__init__(brand, model, year)
        self.p_type = p_type
 
    def __str__(self):
        return f'Scaner {self.brand} {self.model} {self.p_type} {self.year}year '

class Mfu(OfficeEquipment):
    def __init__(self, brand, model, year, p_type='color'):
        super().__init__(brand, model, year)
        self.p_type = p_type
 
    def __str__(self):
        return f'Multifunction device {self.brand} {self.model} {self.p_type} {self.year}year '

s1 = Stock('Stock #1', 'Mocow, Gruzinskaya street, 55')
print(s1)
print(s1.get_info)
pr1 = Printer('Conica Minolta', 'c-250', 2015)
pr2 = Printer('Conica Minolta', 'c-340', 2016)
pr3 = Printer('Conica Minolta', 'c-570', 2017)
sc1 = Scaner('HP', 'd1250', 2020)
sc2 = Scaner('HP', 'd3450', 2022)
mfu1 = Mfu('Canon', 'ab56-90', 2021, 'black&white')

s1.add_to_stock(pr1)
s1.add_to_stock(pr2)
s1.add_to_stock(pr3)
s1.add_to_stock(sc1)
s1.add_to_stock(sc2)
s1.add_to_stock(mfu1)
print(s1.get_info)

s1.extract_from_stock("Printer", "6")
print(s1.get_info)

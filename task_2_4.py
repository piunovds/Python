# Дан список, содержащий искажённые данные с должностями и именами сотрудников. Известно, что имя сотрудника всегда в конце строки. Сформировать из этих имён и вывести на экран фразы вида: 'Привет, Игорь!' Подумать, как получить имена сотрудников из элементов списка, как привести их к корректному виду. Можно ли при этом не создавать новый список?

my_list = ['инженер-конструктор Igor', 'главный бухгалтер MARINA', 'токарь высшего разряда nIKOLAY', 'директор aelita']

for name in my_list:
    print(f"Hi, {name.split(' ')[-1].title()}")

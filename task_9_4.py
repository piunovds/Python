"""
4. Реализуйте базовый класс Car.
+ у класса должны быть следующие атрибуты: speed, color, name, is_police(булево).
+ А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
+ Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
+ добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
+ для классов TownCar и WorkCar переопределите метод show_speed.
+ При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
+ Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.
"""

class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Car ({self.name}) rides')

    def stop(self):
        print(f'Car ({self.name}) stopped')

    def show_speed(self):
        print(f'Current car speed is {self.speed}')

    def turn(self, direction):
        print(f'The {self.color} car turned to the {direction}')

class TownCar(Car):
    def show_speed(self):
        print(f'Current TownCar ({self.name}) speed is {self.speed} km/h')
        if self.speed > 60:
            print(f'WARNING! Current speed is over 60 km/h')
        
class WorkCar(Car):
    def show_speed(self):
        print(f'Current WorkCar ({self.name}) speed is {self.speed} km/h')
        if self.speed > 40:
            print(f'WARNING! Current speed is over 40 km/h')
        
class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        
class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


tc = TownCar(88, 'Blue', 'BMW')
wc = WorkCar(100, 'Yellow', 'Mers')
pc = PoliceCar(150, 'White', 'PPPP')
tc.go()
wc.stop()
tc.turn('left')
tc.name = 'BMWWW'
print(tc.name, wc.name, tc.speed, wc.speed, tc.color, wc.color)
tc.show_speed()
wc.show_speed()

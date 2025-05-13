"""
4. Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости.
"""


class Car:
    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = f'Цвет автомобиля: {color}'
        self.speed = speed
        self.is_police = f'Автомобиль полиции: {is_police}'

    def do(self):
        return f'Автомобиль {self.name} поехал'

    def stop(self):
        return f'Автомобиль {self.name} остановился'

    def turn_right(self):
        return f'Автомобиль {self.name} повернул направо'

    def turn_left(self):
        return f'Автомобиль {self.name} повернул налево'

    def show_speed(self):
        print(f'Моя скорость = {self.speed} км/ч')


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed <= 60:
            return 'Сообщения: нет'
        else:
            return f'Сообщения: У Вас превышения скорости на {self.speed - 60} км/ч'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed <= 40:
            return 'Сообщения: нет'
        else:
            return f'Сообщения: У Вас превышения скорости на {self.speed - 40} км/ч'


class PoliceCar(Car):
    def __init__(self, *args):
        super().__init__(*args,is_police=True)


# --------------Вывод: --------------


car_town = TownCar('BMW', 'Чёрный', 59)
print(car_town.name)
print(car_town.color)
print(car_town.show_speed())
print(car_town.turn_left())

print('-' * 25)

car_work = WorkCar('Toyota', 'Белый', 45)
print(car_work.name)
print(car_work.show_speed())
print(car_work.is_police)
print(car_work.stop())

print('-' * 25)

car_police = PoliceCar('Ford', 'Синий', 60)
print(car_police.name)
print(car_police.is_police)


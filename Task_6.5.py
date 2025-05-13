"""
5. Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    title = 'Концелярская принадлежность'

    def draw(self):
        print('Запуск отрисовки :\n')


class Pen(Stationery):
    title = 'Ручка'

    def draw(self):
        print(f'{self.title} рисует')


class Pencil(Stationery):
    title = 'Карандаш'

    def draw(self):
        print(f'{self.title} рисует')


class Handle(Stationery):
    title = 'Маркер'

    def draw(self):
        print(f'{self.title} рисует')


Stationery = Stationery()
print(Stationery.title)
Stationery.draw()
# Ручка
pen = Pen()
pen.draw()
# Карандаш
pencil = Pencil()
pencil.draw()
# Маркер
handle = Handle()
handle.draw()

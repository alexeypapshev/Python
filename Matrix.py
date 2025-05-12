"""
1. Реализовать класс Matrix (матрица).
Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин,
расположенных в виде прямоугольной схемы.

Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов
класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой
матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""


# import random
#
# list_example = [[random.randrange(0, 10) for x in range(3)] for y in range(4)]
# print(list_example)


class Matrix:

    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        return str('\n'.join(['\t'.join([str(el) for el in i]) for i in self.my_list]))

    def __add__(self, other):
        if len(self.my_list) == len(other.my_list):
            for i in range(len(self.my_list)):
                for j in range(len(other.my_list[i])):
                    self.my_list[i][j] += other.my_list[i][j]
            return self
        else:
            return 'Матрицы не равны друг другу'


first_matrix = Matrix([[8, 8, 2], [9, 3, 8], [4, 9, 1]])
second_matrix = Matrix([[3, 7, 4], [5, 5, 9], [4, 9, 1]])


print(f'--first_matrix--\n{first_matrix}')
print(f'--second_matrix--\n{second_matrix}')
print(f'--first_matrix + second_matrix--\n{first_matrix + second_matrix}')

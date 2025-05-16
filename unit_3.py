import sys

# def foo():
"""
    Напишите программу, которая создает объект, 
    увеличивает и уменьшает счетчик ссылок, 
    а затем выводит количество ссылок на объект.
"""
my_obj = []
print(f'Количество ссылок: {sys.getrefcount(my_obj) - 1}')
new_obj = my_obj
print(f'Количество ссылок: {sys.getrefcount(my_obj) - 1}')
del new_obj
print(f'Количество ссылок: {sys.getrefcount(my_obj) - 1}')



"""
Напишите программу, 
которая создает объекты с циклическими ссылками, 
а затем освобождает память с помощью сборщика мусора.
"""
import gc

class A:
    def __init__(self):
        self.ref = None

a = A()
b = A()
a.ref = b
b.ref = a

gc.collect()
print("Циклические ссылки успешно удалены")
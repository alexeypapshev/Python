
# Напишите функцию, которая принимает два числа и выполняет их деление. 
# Если деление невозможно (например, деление на ноль), функция должна зафиксировать ошибку в лог с трассировкой стека.

import logging

logging.basicConfig(level=logging.ERROR)

def divide(a: int, b: int):
    try:
        result = a / b
        print(f'Результат: {result}')
    except ZeroDivisionError:
        logging.exception('Ошибка деления')
        # print('Ошибка деления')

"""
Запуск функций
divide(10, 5)
divide(10, 2)        
divide(1, 0)        
"""

# Создайте класс пользовательского исключения InvalidDataError, которое будет выбрасываться, если переданные данные пустые. 
# Напишите функцию, которая проверяет входные данные и выбрасывает это исключение, если они пустые, с фиксацией ошибки в лог.

class InvalidDataError(Exception):
    pass

def check_data(data: str):
    try:
        if not data:
            raise InvalidDataError('Данные пусты')
        print('Данные корректны')
    except InvalidDataError:
        logging.exception('Ошибка: Данные пусты')
        print("Ошибка: Данные пусты")

"""
Пример работы функции
check_data("Hello")
check_data("")
"""

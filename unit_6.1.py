# Напишите функцию, которая принимает число и возвращает его квадратный корень. 
# Если число отрицательное — выбросьте исключение ValueError, если это не число — выбросьте исключение TypeError. 
# Реализуйте обработку обоих исключений.

def num_squ(num: int) -> int:
    try:
        if num < 0:
            raise ValueError("Число не должно быть отрицательным")
        
        elif type(num) != int:
            raise TypeError("Введённое значени не является числом")
        
        else:
            print(f'Квадратный корень числа {num} = {num ** 2}')

    except(ValueError, TypeError) as e:
        print(f"Произошла ошибка: {e}")

        
# num_squ(5)
# num_squ(-5)
# num_squ('kdlakdpa')
# num_squ(5)


# Напишите функцию, которая принимает строку и пытается преобразовать её в число. 
# Если строка не содержит числа, выбросьте исключение ValueError,
# а затем перехватите его и выбросьте RuntimeError, сохраняя цепочку исключений.

def convert_to_number(string):
    try:
        return int(string)
    except ValueError as e:
        raise RuntimeError("Ошибка преобразования строки") from e

# Пример вызова
a = input()
try:
    convert_to_number(a)
except RuntimeError as e:
    print(f"Ошибка: {e}")
    # print(f"Исходная ошибка: {e.__cause__}") #для просмотра ошибки

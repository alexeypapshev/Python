# Создайте пользовательское исключение NegativeNumberError, которое будет выбрасываться при передаче отрицательного числа в функцию. 
# Реализуйте обработку этого исключения.

class NegativeNumberError(Exception):
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return f"Ошибка: Передано отрицательное число {self.value}"


def check_number(x):
    if x < 0:
        raise NegativeNumberError(x)
    return f"Число корректно: {x}"

# a = int(input())

# try:
#     check_number(a)
# except NegativeNumberError as e:
#     print(e)


class DivisionByZeroError(Exception):
    def __init__(self, dividened):
        self.dividened = dividened

    def __str__(self):
        return f'Ошибка: Нельзя делить {self.dividened} на ноль'
    


def check_zero(num1, num2):
    if num2 == 0:
        raise DivisionByZeroError(num1)
    return num1 / num2

nums = input().split()

try:
    check_zero(int(nums[0]), int(nums[1]))
except DivisionByZeroError as f:
    print(f)

    


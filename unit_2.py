def fib(n, cache={}):
    if n in cache:
        return cache[n]
    if n <= 1:
        return n
    cache[n] = fib(n - 1) + fib(n - 2)
    return cache[n]

# print(fib(5))  


def sum_num(num: int) -> int:
    sum = 0
    for i in str(num):
        sum += int(i)

    return sum
# print(sum_num(1234))

def sum_of_digits(num: int) -> int:
    if num == 0:
        return 0
    
    else:
        return (num % 10) + sum_of_digits(num // 10)

# print(sum_of_digits(int(input())))

def fib(n: int) -> int: 
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

# print(fib(int(input())))


# Факториал числа
def fact(num: int) -> int:
    if num == 0 or num == 1:
        return 1
    return num * fact(num - 1)

# print(fact(int(input())))

# Возведение в степень
def squ(num1: int, num2: int) -> int:
    if num1 == 0 or num2 == 0:
        return 1
    
    return num1 * squ(num1, num2-1)

# num1, num2 = map(int, input().split())

# print(squ(num1, num2))  

def find_minimum(n, lst):
    if len(lst) == 1:
        return lst[0]
    else:
        current_min = find_minimum(n, lst[1:])
         
    if lst[0] < current_min:
        return lst[0]
    return current_min

# Пример использования функции
# print(find_minimum(input(), list(map(int, input().split()))))

# другой способ
def find_min_recursive(arr, n):
    if n == 1:
        return arr[0]
    return min(arr[n - 1], find_min_recursive(arr, n - 1))

# n = int(input())
# arr = list(map(int, input().split()))
# print(find_min_recursive(arr, n))




# НАЙТИ СУММУ ЗНАЧЕНИЙ
def find_equals_recursive(arr, n):
    if n == 1:
        return arr[0]
    return arr[n - 1] + find_equals_recursive(arr, n - 1)

# n = int(input())
# arr = list(map(int, input().split()))
# print(find_equals_recursive(arr, n))

# Напишите рекурсивную функцию для вычисления n-го числа Фибоначчи.

def number_fib(num: int) -> int:
    if num <=1:
        return num
    return number_fib(num - 1) + number_fib(num - 2)

# print(number_fib(int(input())))


# Напишите рекурсивную функцию, которая проверяет, является ли строка палиндромом.

def palindrom(word: str) -> str:
    if len(word) <= 1:
        return 'Да'
    
    if word[0] != word[-1]:
        return 'Нет'
    
       # Рекурсивно проверяем подстроку без первого и последнего символов
    return palindrom(word[1:-1])


print(palindrom())

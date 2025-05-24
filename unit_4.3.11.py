# Напишите программу с использованием многозадачности, которая считает факториал для чисел от 1 до 5. 
# Каждая задача должна выполнять вычисление факториала для одного числа и выводить результат.


import threading


def func_factorial(num: int) -> int:
    if num == 0 or num == 1:
        result = 1
    
    else:
        result = 1
        for i in range(2, num + 1):
            result *= i

    print(f'Факториал числа {num} равен {result}')



threads = []
for i in range(1, 6):
    t = threading.Thread(target=func_factorial, args=(i,))
    t.start()
    threads.append(t)


for i in threads:
    t.join()  

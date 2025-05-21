"""
Условие: Напишите программу, которая создает 4 процесса. 
Каждый процесс должен вычислить квадрат своего номера и вывести результат.

Квадрат 1 = 1
Квадрат 2 = 4
Квадрат 3 = 9
Квадрат 4 = 16
"""

import multiprocessing

def worker(num: int):
    print(f'Квадрат {num} = {num ** 2}')


if __name__ == '__main__':
    processes = []
    for i in range(1,5):
        p = multiprocessing.Process(target=worker, args=(i,))
        p.start()
        processes.append(p)
        # Ждем завершения всех процессов
    for p in processes:
        p.join()

# Напишите программу, которая создает два потока. 
# Первый поток должен выполнить задачу через 2 секунды, второй — через 3 секунды. 
# Выведите информацию о том, какой поток завершился первым.

"""
import threading
import time
unit_4.3.py
lock = threading.Lock()

def worker(num):
    time.sleep(num)
    print(f"Задача {num} завершена")

threads = []

# Запускаем первый поток
t1 = threading.Thread(target=worker, args=(1,))
t1.start()
threads.append(t1)

# Запускаем второя поток
time.sleep(3)
t2 = threading.Thread(target=worker, args=(2,))
t2.start()
threads.append(t2)


for t in threads:
    t.join()

"""

#Напишите асинхронную программу, которая запускает две задачи. 
# Первая задача должна ждать 2 секунды, вторая — 3 секунды. 
#Выведите информацию о том, когда каждая из задач завершится.

"""
import asyncio

async def task_1():
    await asyncio.sleep(2)
    print("Задача 1 завершена")


async def task_2():
    await asyncio.sleep(3)
    print("Задача 2 завершена")


async def main():
    # task1 = asyncio.create_task(task_1())
    # task2 = asyncio.create_task(task_2())

    await task_1()
    await task_2()

asyncio.run(main())

"""

#Напишите программу, которая запускает 4 потока, каждый из которых будет вычислять квадрат своего индекса от 1 до 4. 
#После выполнения всех потоков выведите результаты.

"""
import threading
import time

def worker(num: int):
    print(f'Квадрат числа {num} равен {num ** 2}')

threads = []

for i in range(1,5):
    t = threading.Thread(target=worker, args=(i,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()
"""

# Напишите программу, которая использует многозадачность для выполнения трех функций: 
# одна функция должна ждать 2 секунды, вторая — 1 секунду, третья — 4 секунды. 
# Выведите, в каком порядке функции завершатся.

"""
import asyncio

async def foo_1():
    await asyncio.sleep(2)
    print('Задача 1 завершена')

async def foo_2():
    await asyncio.sleep(1)
    print('Задача 2 завершена')

async def foo_3():
    await asyncio.sleep(4)
    print('Задача 3 завершена')

async def main():
    task1 = asyncio.create_task(foo_1())
    task2 = asyncio.create_task(foo_2())
    task3 = asyncio.create_task(foo_3())

    await task1
    await task2
    await task3

asyncio.run(main())

# Второй способ, используя многопоточность
import threading
import time

def task_1():
    time.sleep(2)
    print("Задача 1 завершена")

def task_2():
    time.sleep(1)
    print("Задача 2 завершена")

def task_3():
    time.sleep(4)
    print("Задача 3 завершена")

thread_1 = threading.Thread(target=task_1)
thread_2 = threading.Thread(target=task_2)
thread_3 = threading.Thread(target=task_3)

thread_1.start()
thread_2.start()
thread_3.start()

thread_1.join()
thread_2.join()
thread_3.join()

"""

#Напишите асинхронную программу, которая одновременно выполняет несколько операций: 
#три задачи, каждая из которых будет ждать по 1 секунде, выводя сообщение после завершения.

import asyncio

async def task():
    await asyncio.sleep(1
    
    )
    print('Задача завершена')

async def main():
    tasks= [task() for _ in range(3)]

    await asyncio.gather(*tasks)

asyncio.run(main())
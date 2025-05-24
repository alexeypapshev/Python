# Напишите асинхронную программу, которая поочередно выполняет пять задач, 
# каждая из которых должна выводить информацию о своём завершении.


import asyncio

async def worker(num: int):
    print(f'Задача {num} завершена')

async def main():
    for i in range(1, 6):
        await worker(i)

asyncio.run(main())

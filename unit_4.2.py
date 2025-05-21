import asyncio

async def my_coroutine():
    print("Начало корутины")
    await asyncio.sleep(5)
    print("Конец корутины")

# asyncio.run(my_coroutine())


async def read_file():
    with open("example.txt", "r") as file:
        data = await asyncio.to_thread(file.read)
    print(data)

# asyncio.run(read_file())


async def task_1():
    await asyncio.sleep(15)  
    print("Задача 1 завершена")

async def task_2():
    await asyncio.sleep(10)
    print("Задача 2 завершена")

async def main():
    task1 = asyncio.create_task(task_1())
    task2 = asyncio.create_task(task_2())
    
    await task1
    await task2

# asyncio.run(main())     


"""
Условие: Используя библиотеку aiohttp, создайте программу, 
которая выполняет асинхронные запросы к трем веб-страницам и выводит их статус-коды.
"""

import aiohttp
import asyncio

async def fetch_status(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                print(f"Статус код страницы {url}: {response.status}")

    except aiohttp.ClientConnectorError:
        print(f"Ошибка соединения для {url}")

async def main():
    urls = ["https://www.google.com", "https://www.github.com", "https://www.github.com/nonexistent-page-12"]
    tasks = [fetch_status(url) for url in urls]
    await asyncio.gather(*tasks)

asyncio.run(main())
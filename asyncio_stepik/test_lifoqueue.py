import asyncio

# При выводе в консоль можно использовать ANSI коды
RED = '\033[31m'
YELLOW = '\033[33m'
GREEN = '\033[32m'
END = '\033[0m'  # Возврат к настройкам


async def customer(queue):
    while not queue.empty():
        await asyncio.sleep(.5)
        elem = queue.get_nowait()
        print(f'Из очереди получен элемент_{elem}')

    print(f'{YELLOW}Очередь опустошена{END}')

    try:
        elem = queue.get_nowait()
        print(f'Из очереди получен элемент_{elem}')  # Принт не сработает
    except asyncio.QueueEmpty:
        print(f'{RED}Попытка получить элемент из пустой очереди методом get_nowait() вызвала asyncio.QueueEmpty{END}')


async def producer(queue):
    for i in range(5):
        await asyncio.sleep(.5)
        queue.put_nowait(i)
        print(f'В очередь поставлен элемент_{i}')
        if queue.full():  # Если очередь заполнена
            print(f'{YELLOW}Очередь заполнена{END}')
            try:
                queue.put_nowait(i + 1)
                print(f'В очередь поставлен элемент_{i}')  # Принт не сработает
            except asyncio.QueueFull:
                print(
                    f'{RED}Попытка поместить элемент в заполненную очередь методом put_nowait() вызвала asyncio.QueueFull{END}')
                print(f'{GREEN}Запускаем процесс получения элементов из очереди{END}')
                await customer(queue)


async def main():
    queue = asyncio.LifoQueue(5)
    print(f'{GREEN}Емкость созданной очереди: {queue.maxsize} элементов{END}')
    prod = asyncio.create_task(producer(queue))
    await prod
    print('End')


asyncio.run(main())

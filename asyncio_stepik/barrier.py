import asyncio


# определяем корутину worker, принимающую объект класса asyncio.Barrier
async def worker(barrier: asyncio.Barrier, num):

    # выводим на экран сообщение о том, что работник ждет прибытия других
    print(f"worker_{num} ждет на барьере")

    # ожидаем, пока все работники достигнут барьера
    await barrier.wait()

    # выводим сообщение о том, что работник прошел барьер
    print(f"worker_{num} прошел барьер")

#определяем корутину main
async def main():

    # создаем объект класса asyncio.Barrier, ожидающий 3 корутины
    barrier = asyncio.Barrier(5)

    # создаем список задач, каждая из которых вызывает корутину worker с объектом barrier в качестве аргумента
    tasks = [asyncio.create_task(worker(barrier, num)) for num in range(3)]

    # выводим сообщение о том, что ждем, пока все работники достигнут барьера
    print("Ждем, пока worker's пройдут барьер")

    # ожидаем, пока все работники достигнут барьера
    await barrier.wait()

    # выводим сообщение о том, что все работники прошли барьер
    print("Все worker's прошли барьер")

    # отменяем все задачи в списке tasks
    [task.cancel() for task in tasks]

#запускаем корутину main с помощью метода run() из библиотеки asyncio
asyncio.run(main())
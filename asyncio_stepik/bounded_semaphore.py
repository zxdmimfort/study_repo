import asyncio
import random

# Создаем экземпляр Semaphore максимум c двумя разрешениями

# Поочередно выполните код с разным типом семафора, чтобы понять в чем разница

# semaphore = asyncio.Semaphore(2)
semaphore = asyncio.BoundedSemaphore(2)


async def acquire(semaphore: asyncio.Semaphore):
    print(f"Value before acquire: {semaphore._value}")
    await semaphore.acquire()
    print(f"Value after acquire: {semaphore._value}")


def release(semaphore: asyncio.Semaphore):
    print(f"Value before release: {semaphore._value}")
    semaphore.release()
    print(f"Value after release: {semaphore._value}")
    
    
async def my_coroutine(id):
    print(f'Корутина {id} хочет получить семафор')
    await acquire(semaphore)
    print(f'Корутина {id} получила семафор')
    await asyncio.sleep(random.random())
    release(semaphore)
    print(f'Корутина {id} отпустила семафор')
    release(semaphore)
    print(f'||||||| {id} отпустила семафор еще раз')


# Запускаем несколько корутин
async def main():
    await asyncio.gather(my_coroutine(1), my_coroutine(2), my_coroutine(3))


asyncio.run(main())
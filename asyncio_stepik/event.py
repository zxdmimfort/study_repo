import asyncio

# Создаем экземпляр Event
event = asyncio.Event()

async def waiter():
    print('waiter: ожидаем события')
    await event.wait()
    print('waiter: событие произошло')

async def setter():
    print('setter: засыпаем')
    await asyncio.sleep(1)
    print('setter: просыпаемся и устанавливаем событие')
    event.set()

async def main():
    # Запускаем waiter и setter параллельно
    await asyncio.gather(waiter(), setter())

asyncio.run(main())

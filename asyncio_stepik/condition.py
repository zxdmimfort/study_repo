import asyncio

# Создаем экземпляр Condition
condition = asyncio.Condition()

async def consumer(condition):
    async with condition:
        print('consumer: ждем условия')
        await condition.wait()
        print('consumer: условие выполнено')

async def producer(condition):
    print('producer: засыпаем')
    await asyncio.sleep(1)
    print('producer: просыпаемся и устанавливаем условие')
    async with condition:
        condition.notify_all()

async def main():
    # Запускаем consumer и producer параллельно
    await asyncio.gather(consumer(condition), producer(condition))

asyncio.run(main())

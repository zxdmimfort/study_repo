import asyncio


async def session_to_bd(condition: asyncio.Condition, name: str):
    async with condition:
        print(f"Пользователь {name} ожидает доступа к базе данных")
        await condition.wait()
        print(f"Пользователь {name} подключился к БД")
        await asyncio.sleep(1)
        print(f"Пользователь {name} отключается от БД")
        condition.notify()
        await asyncio.sleep(0.5)


async def start_first_session(condition: asyncio.Condition):
    await asyncio.sleep(2)
    async with condition:
        condition.notify()


async def main():
    condition = asyncio.Condition()
    users = ['Alice', 'Bob', 'Charlie', 'Dave', 'Eva', 'Frank', 'George', 'Helen', 'Ivan', 'Julia']
    
    sessions = [asyncio.create_task(session_to_bd(condition, name)) for name in users]
    controller = start_first_session(condition)
    await asyncio.gather(*sessions, controller)


asyncio.run(main())

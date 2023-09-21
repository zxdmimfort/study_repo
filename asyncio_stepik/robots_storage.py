import asyncio


async def move(name: str, id: int, lock: asyncio.Lock):
    async with lock:
        global counter
        print(f"Робот {name}({id}) передвигается к месту A")
        counter += 1
        print(f"Робот {name}({id}) достиг места A. Место A посещено {counter} раз")


async def main():
    robot_names = ['Электра', 'Механикс', 'Оптимус', 'Симулакр', 'Футуриус']
    lock = asyncio.Lock()
    tasks = [move(name, i, lock) for i, name in enumerate(robot_names)]
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    counter = 0
    asyncio.run(main())

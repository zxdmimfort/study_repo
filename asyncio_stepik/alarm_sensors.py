import asyncio
import random


async def sensor(sensor_id: int, ip: str, event: asyncio.Event):
    print(f"Датчик {sensor_id} IP-адрес {ip} настроен и ожидает срабатывания")
    await event.wait()
    print(f'Датчик {sensor_id} IP-адрес {ip} активирован, "Wee-wee-wee-wee"')
    


async def main():
    event = asyncio.Event()
    ip = ["192.168.0.3", "192.168.0.1", "192.168.0.2", "192.168.0.4", "192.168.0.5"]
    tasks = [asyncio.create_task(sensor(i, ip, event)) for i, ip in enumerate(ip)]
    await asyncio.sleep(5 * random.random())
    event.set()
    print("Датчики зафиксировали движение")
    await asyncio.gather(*tasks)


asyncio.run(main())

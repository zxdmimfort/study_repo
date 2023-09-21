import requests


dict_url = "https://raw.githubusercontent.com/nefelsay/asyncio/main/call_company.py"
response = requests.get(url=dict_url)

with open('data_company.py', 'wt') as f:
    f.write(response.text)

import asyncio
from data_company import data # type: ignore


async def call_company(comp_info: dict):
    name: str = comp_info["Name"]
    time: int = comp_info["call_time"]
    phone: str = comp_info["Phone"]

    try:
        await asyncio.wait_for(asyncio.sleep(time), timeout=5)
        print(f"Company {name}: {phone} дозвон успешен")
    except asyncio.TimeoutError:
        # Ловим ошибку wait_for по timeout
        print(f"{name} отлетает по таймауту")
    except asyncio.CancelledError:
        # А тут ловим ошибки отмены задачи, если кто-то решит забрать result()
        print(f"{name} canceled")


async def main():
    tasks = [asyncio.create_task(call_company(company_info)) for company_info in data]
    _, pending = await asyncio.wait(tasks, timeout=10)
    for task in pending:
        task.cancel()
    await asyncio.gather(*pending)


asyncio.run(main())

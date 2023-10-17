import asyncio
import json
import time
import aiofiles
from aiocsv.readers import AsyncDictReader
import os


async def write_json(path: str, obj: dict):
    async with aiofiles.open(path, 'w+', encoding='utf-8') as afp:
        await afp.write(json.dumps(obj, ensure_ascii=False, indent=4))


async def process_csv_file(path: str, semaphore: asyncio.Semaphore):
    async with semaphore:
        async with aiofiles.open(path, encoding='cp1251') as afp:
            used, new = 0, 0
            async for row in AsyncDictReader(afp, delimiter=';', quotechar='"'):
                if row['Состояние авто'] == 'Б/У':
                    used += int(row['Стоимость авто'])
                    continue
                new += int(row['Стоимость авто'])
        return used, new


async def process_directory(json_path: str, csv_path: str, semaphore: asyncio.Semaphore):
    csv_paths = []
    start_time = time.time()
    for folder, _, files in os.walk(csv_path):
        for file in files:
            csv_paths.append(f"{folder}/{file}")
    print(time.time() - start_time)
    
    tasks = [process_csv_file(csv_path, semaphore) for csv_path in csv_paths]
    csv_reses = await asyncio.gather(*tasks)

    used_all_price, new_all_price = 0, 0
    for used_price, new_price in csv_reses:
        used_all_price += used_price
        new_all_price += new_price
    await write_json(json_path + 'prices_auto.json',
                     {"Б/У": used_all_price,
                      "Новый": new_all_price,})


async def main(json_path: str, csv_path: str, semaphore: asyncio.Semaphore):
    autos = await process_directory(json_path, csv_path, semaphore)


if __name__ == "__main__":
    base_dir = './asyncio_stepik/aiofiles/'
    csv_dir = 'auto/'
    semaphore = asyncio.Semaphore(1000)
    asyncio.run(main(base_dir, base_dir + csv_dir, semaphore))

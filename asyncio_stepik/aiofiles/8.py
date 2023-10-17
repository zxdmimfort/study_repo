import asyncio
import datetime
import itertools
import aiofiles
import aiofiles.os as aos
from aiocsv.writers import AsyncDictWriter
import json


async def write_csv(obj: list[dict], path: str):
    async with aiofiles.open(path, mode='w', encoding='utf-8-sig') as afp:
        print(list(obj[0].keys()))
        writer = AsyncDictWriter(afp, fieldnames=list(obj[0].keys()), delimiter=';')
        await writer.writeheader()
        await writer.writerows(obj)


async def process_json(path: str, semaphore: asyncio.Semaphore) -> list[dict]:
    async with semaphore:
        async with aiofiles.open(path, encoding='utf-8') as afp:
            content = await afp.read()
        json_obj = json.loads(content)
        res = []
        for record in json_obj:
            if record['HTTP-статус'] == 200:
                record['Время и дата'] = datetime.datetime.strptime(record['Время и дата'], "%Y-%m-%d %H:%M:%S")
                print(record['Время и дата'])
                res.append(record)
    return res


async def process_directory(path: str, semaphore: asyncio.Semaphore) -> list[dict]:
    files = [file.path for file in await aos.scandir(path) if file.is_file()]
    tasks = [process_json(file, semaphore) for file in files]
    results = sorted(list(itertools.chain.from_iterable(await asyncio.gather(*tasks))), key=lambda record: record['Время и дата'])
    for record in results:
        record['Время и дата'] = record['Время и дата'].strftime("%d.%m.%Y %H:%M:%S")
    return results


async def main(out_path: str, in_path: str, semaphore: asyncio.Semaphore):
    filtered = await process_directory(in_path, semaphore)
    await write_csv(filtered, out_path + 'bad_logs.csv')


if __name__ == "__main__":
    base_dir = './asyncio_stepik/aiofiles/'
    json_dir = 'logs/'
    semaphore = asyncio.Semaphore(1000)
    asyncio.run(main(base_dir, base_dir + json_dir, semaphore))

    
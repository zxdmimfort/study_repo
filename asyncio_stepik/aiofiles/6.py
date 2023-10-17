import itertools
import os
import asyncio
import time
from aiocsv.readers import AsyncDictReader
import json
import aiofiles


async def write_to_json(students: list[dict], path: str):
    students.sort(key=lambda person: person['Телефон для связи'])
    async with aiofiles.open(path + '100_students.json', 'w+', encoding='utf-8') as json_file:
        await json_file.write(json.dumps(students, indent=4, ensure_ascii=False))


async def a_read_csv(csv_file: str, semaphore: asyncio.Semaphore):
    res = []
    async with semaphore:
        async with aiofiles.open(csv_file, encoding='utf-8-sig') as a_csv_file:
            async for person in AsyncDictReader(asyncfile=a_csv_file, delimiter=','):
                if person['Балл ЕГЭ'] == '100':
                    res.append(person)
    return res


async def process_directory(csv_dir: str):
    csv_paths = []
    for folder, _, files in os.walk(csv_dir):
        for file in files:
            csv_paths.append(f"{folder}/{file}")
    students = await asyncio.gather(*[a_read_csv(path, semaphore) for path in csv_paths])
    return list(itertools.chain.from_iterable(students))


async def main(base_dir: str, csv_dir: str, semaphore: asyncio.Semaphore):
    students = await process_directory(csv_dir)
    await write_to_json(students, base_dir)


if __name__ == "__main__":
    start_time = time.time()
    semaphore = asyncio.Semaphore(1000)
    base_dir = './asyncio_stepik/aiofiles/'
    csv_dir = 'region_student/'
    asyncio.run(main(base_dir, base_dir + csv_dir, semaphore))
    print(time.time() - start_time)

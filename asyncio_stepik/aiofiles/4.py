import asyncio
from aiocsv.readers import AsyncReader
import aiofiles
import os


async def read_csv_file(path: str, semaphore: asyncio.Semaphore):
    async with semaphore:
        async with aiofiles.open(path, mode='r') as csv_file:
            async for row in AsyncReader(csv_file):
                return int(row[0])


async def main(base_dir: str):
    semaphore = asyncio.Semaphore(500)
    folders = os.walk(base_dir)
    files = [f"{folder}/{files[0]}" for folder, _, files in folders if len(files) == 1]
    tasks = [read_csv_file(path, semaphore) for path in files]
    nums = await asyncio.gather(*tasks)
    print(sum(nums))


if __name__ == "__main__":
    base_dir = './asyncio_stepik/aiofiles/5000folder'
    asyncio.run(main(base_dir))
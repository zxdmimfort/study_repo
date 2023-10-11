import asyncio
import time
import aiofiles
import aiofiles.os as aos
import aiocsv
import csv


async def aread_csv(path: str, semaphore: asyncio.Semaphore):
    async with semaphore:
        async with aiofiles.open(path, mode='r') as csv_file:
            async for row in aiocsv.AsyncReader(csv_file):
                return int(row[0])


def read_csv(path: str):
    with open(path, mode='r') as csv_file:
        for row in csv.reader(csv_file):
            return int(row[0])


async def main(csv_dir: str):
    semaphore = asyncio.Semaphore(500)
    paths = [file.path for file in await aos.scandir(csv_dir) if file.is_file()]
    # nums = await asyncio.gather(*[aread_csv(path, semaphore) for path in paths])
    nums = [read_csv(path) for path in paths]
    
    print(sum(nums))


if __name__ == "__main__":
    csv_dir = './asyncio_stepik/aiofiles/5000csv'
    start_time = time.time()
    asyncio.run(main(csv_dir))
    print(time.time() - start_time)

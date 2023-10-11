import time
import aiofiles
from aiofiles import os
import asyncio




async def read_txt_file(path: str, semaphore: asyncio.Semaphore):
    async with semaphore:
        async with aiofiles.open(path, mode='r') as f:
            num = int(await f.read())
        if num % 2 == 0:
            return num
        return 0
        


async def main():
    semaphore = asyncio.Semaphore(20000)
    base_path = './asyncio_stepik/aiofiles/files'
    files = await os.scandir(path=base_path)
    tasks = [read_txt_file(file.path, semaphore) for file in files if file.is_file() and file.name.endswith('.txt')]
    nums = await asyncio.gather(*tasks)
    print(sum(nums))

    


if __name__ == '__main__':
    start_time = time.perf_counter()
    asyncio.run(main())
    print(time.perf_counter() - start_time)

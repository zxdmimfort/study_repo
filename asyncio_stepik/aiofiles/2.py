import asyncio
import aiofiles
from aiofiles import os as aos
import os
import json

async def read_file(path: str, res: dict):
    async with aiofiles.open(path, 'r') as f:
        lines = [line.strip() for line in await f.readlines()]
    for line in lines:
        header, msg = line.split(': ')
        _, name = header.split(' - ')
        res[name] = res.get(name, 0) + len(msg) * 0.03
            

async def main(directory: str):
    cnt_chars = {}
    files = await aos.scandir(directory)
    tasks = [read_file(file.path, cnt_chars) for file in files if file.is_file()]
    await asyncio.gather(*tasks)
    res = {k: str(round(v, 2)) + 'р'
           for k, v in sorted(cnt_chars.items(), key=lambda kv: kv[1], reverse=True)}
    print(json.dumps(res, ensure_ascii=False, indent=4))
    
    


if __name__ == "__main__":
    base_directory = "./asyncio_stepik/aiofiles/chat_log"
    asyncio.run(main(base_directory))
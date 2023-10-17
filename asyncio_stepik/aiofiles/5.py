from aiocsv.readers import AsyncDictReader
import asyncio
import aiofiles
import json


async def process_csv_to_json(csv_path: str, json_path: str):
    res = []
    
    async with aiofiles.open(csv_path, encoding='utf-8-sig') as a_csv_file:
        async for row in AsyncDictReader(a_csv_file, delimiter=';'):
            res.append(row)

    print(res[0])
    
    with open(json_path, 'w+', encoding='utf-8') as json_file:
        json.dump(res, json_file, indent=4, ensure_ascii=False)


async def main(csv_file, json_file):
    await process_csv_to_json(csv_file, json_file)


if __name__ == "__main__":
    base_dir = './asyncio_stepik/aiofiles/'
    csv_file = 'address_1000000.csv'
    json_file = 'address.json'
    asyncio.run(main(base_dir + csv_file, base_dir + json_file))
    
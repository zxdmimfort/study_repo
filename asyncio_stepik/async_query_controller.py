import asyncio
import random


class QueryController:
    def __init__(self, users: list[str], connection_limit: int) -> None:
        self._users = users
        self._semaphore = asyncio.Semaphore(connection_limit)
        self._complete_cnt = 0

    def inc_return_complete_query(self):
        self._complete_cnt += 1
        return self._complete_cnt

    async def query_run(self, user: str):
        async with self._semaphore:
            print(f"Пользователь {user} делает запрос")
            await asyncio.sleep(random.random())
            print(f"Запрос от пользователя {user} завершен")
            print(f"Всего запросов: {self.inc_return_complete_query()}")

    async def controller(self):
        queries = [asyncio.create_task(self.query_run(user)) for user in self._users]
        await asyncio.gather(*queries)

    def run(self):
        asyncio.run(self.controller())


if __name__ == "__main__":
    users = [
        "sasha",
        "petya",
        "masha",
        "katya",
        "dima",
        "olya",
        "igor",
        "sveta",
        "nikita",
        "lena",
        "vova",
        "yana",
        "kolya",
        "anya",
        "roma",
        "nastya",
        "artem",
        "vera",
        "misha",
        "liza",
    ]
    controller = QueryController(users, 3)
    controller.run()
